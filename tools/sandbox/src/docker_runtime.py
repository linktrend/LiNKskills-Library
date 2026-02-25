from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any, Callable

import docker

AuditCallback = Callable[[str, str, str], None]


class DockerRuntime:
    """Ephemeral Docker command runtime with conservative defaults."""

    def __init__(
        self,
        image: str = "python:3.11-slim",
        mem_limit: str = "512m",
        network_disabled: bool = True,
        audit_callback: AuditCallback | None = None,
    ) -> None:
        self.image = image
        self.mem_limit = mem_limit
        self.network_disabled = network_disabled
        self.audit_callback = audit_callback
        self.client = docker.from_env()

    def run(self, command: str, cwd: str | Path | None = None) -> dict[str, Any]:
        """Run a shell command inside an ephemeral container and return outputs."""
        workdir_host = Path(cwd or Path.cwd()).expanduser().resolve()
        self._audit("sandbox.run", "start", command)
        container = None

        try:
            self.client.images.pull(self.image)
            container = self.client.containers.create(
                image=self.image,
                command=["/bin/sh", "-lc", command],
                working_dir="/workspace",
                volumes={str(workdir_host): {"bind": "/workspace", "mode": "rw"}},
                mem_limit=self.mem_limit,
                network_disabled=self.network_disabled,
                tty=False,
                stdin_open=False,
                auto_remove=False,
                detach=True,
            )
            container.start()
            wait_result = container.wait()
            exit_code = int(wait_result.get("StatusCode", 1))
            stdout = container.logs(stdout=True, stderr=False).decode("utf-8", errors="replace")
            stderr = container.logs(stdout=False, stderr=True).decode("utf-8", errors="replace")

            status = "success" if exit_code == 0 else "error"
            self._audit("sandbox.run", status, command)
            return {
                "status": status,
                "command": command,
                "image": self.image,
                "network_disabled": self.network_disabled,
                "cwd": str(workdir_host),
                "stdout": stdout,
                "stderr": stderr,
                "exit_code": exit_code,
            }
        except Exception as exc:
            self._audit("sandbox.run", "error", command)
            return {
                "status": "error",
                "code": "SANDBOX_EXEC_FAILED",
                "message": str(exc),
                "command": command,
                "image": self.image,
                "cwd": str(workdir_host),
                "network_disabled": self.network_disabled,
                "stdout": "",
                "stderr": str(exc),
                "exit_code": 1,
            }
        finally:
            if container is not None:
                try:
                    container.remove(force=True)
                except Exception:
                    pass

    def _audit(self, action: str, status: str, resource_id: str) -> None:
        if self.audit_callback is None:
            return
        try:
            self.audit_callback(action, status, resource_id)
        except Exception:
            return


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="LiNKskills Sandbox CLI")
    parser.add_argument("--version", action="version", version="sandbox 1.0.0")
    parser.add_argument("--json", action="store_true", help="Emit deterministic JSON output")
    parser.add_argument("command", type=str, help="Command string to run in container")
    parser.add_argument(
        "--allow-network",
        action="store_true",
        help="Enable outbound network access (disabled by default)",
    )
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    runtime = DockerRuntime(network_disabled=not args.allow_network)
    result = runtime.run(command=args.command)

    payload = {
        "status": result.get("status", "error"),
        "output": {
            "stdout": result.get("stdout", ""),
            "stderr": result.get("stderr", ""),
            "exit_code": result.get("exit_code", 1),
        },
        "path": result.get("cwd", ""),
    }

    print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
    if result.get("status") != "success":
        raise SystemExit(1)


if __name__ == "__main__":
    main()
