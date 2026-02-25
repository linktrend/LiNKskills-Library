from __future__ import annotations

import argparse
import base64
import hashlib
import json
import os
import sys
from pathlib import Path
from typing import Any, Callable

from cryptography.fernet import Fernet, InvalidToken

AuditCallback = Callable[[str, str, str], None]


class VaultError(RuntimeError):
    """Base exception for vault operations."""


class MissingMasterKeyError(VaultError):
    """Raised when LSL_MASTER_KEY is unavailable."""


class VaultStore:
    """Encrypted key/value storage backed by a single binary blob."""

    def __init__(
        self,
        data_path: str | Path,
        master_key: str | None = None,
        audit_callback: AuditCallback | None = None,
    ) -> None:
        self.data_path = Path(data_path).expanduser().resolve()
        self.audit_callback = audit_callback

        resolved_master_key = (master_key or os.getenv("LSL_MASTER_KEY", "")).strip()
        if not resolved_master_key:
            self._audit("vault.master_key", "error", "LSL_MASTER_KEY")
            raise MissingMasterKeyError(
                "LSL_MASTER_KEY is required for vault operations"
            )

        digest = hashlib.sha256(resolved_master_key.encode("utf-8")).digest()
        fernet_key = base64.urlsafe_b64encode(digest)
        self._fernet = Fernet(fernet_key)

    def set_from_file_or_string(self, key: str, source: str) -> dict[str, Any]:
        """Store a value; source can be a literal string or local file path."""
        if not key.strip():
            self._audit("vault.set", "error", "<empty-key>")
            raise VaultError("Key must be a non-empty string")

        source_path = Path(source).expanduser()
        if source_path.exists() and source_path.is_file():
            value = source_path.read_text(encoding="utf-8")
            source_type = "file"
            source_ref = str(source_path.resolve())
        else:
            value = source
            source_type = "string"
            source_ref = "inline"

        payload = self._load_payload()
        payload[key] = value
        self._save_payload(payload)
        self._audit("vault.set", "success", key)
        return {
            "status": "success",
            "key": key,
            "source_type": source_type,
            "source_ref": source_ref,
        }

    def get_value(self, key: str) -> str:
        """Return a decrypted value by key."""
        payload = self._load_payload()
        if key not in payload:
            self._audit("vault.get", "error", key)
            raise KeyError(f"Vault key not found: {key}")
        self._audit("vault.get", "success", key)
        return str(payload[key])

    def list_keys(self) -> list[str]:
        """List known keys without exposing values."""
        payload = self._load_payload()
        keys = sorted(payload.keys())
        self._audit("vault.list", "success", str(len(keys)))
        return keys

    def _load_payload(self) -> dict[str, Any]:
        if not self.data_path.exists():
            return {}

        encrypted = self.data_path.read_bytes()
        if not encrypted:
            return {}

        try:
            decrypted = self._fernet.decrypt(encrypted)
        except InvalidToken as exc:
            self._audit("vault.decrypt", "error", str(self.data_path))
            raise VaultError("Vault decryption failed. Check LSL_MASTER_KEY.") from exc

        try:
            parsed = json.loads(decrypted.decode("utf-8"))
        except json.JSONDecodeError as exc:
            self._audit("vault.parse", "error", str(self.data_path))
            raise VaultError("Vault payload is not valid JSON") from exc

        if not isinstance(parsed, dict):
            self._audit("vault.parse", "error", str(self.data_path))
            raise VaultError("Vault payload root must be an object")

        return parsed

    def _save_payload(self, payload: dict[str, Any]) -> None:
        self.data_path.parent.mkdir(parents=True, exist_ok=True)
        serialized = json.dumps(payload, sort_keys=True, separators=(",", ":")).encode(
            "utf-8"
        )
        encrypted = self._fernet.encrypt(serialized)
        self.data_path.write_bytes(encrypted)

    def _audit(self, action: str, status: str, resource_id: str) -> None:
        if self.audit_callback is None:
            return
        try:
            self.audit_callback(action, status, resource_id)
        except Exception:
            # Audit failures must not break secure storage operations.
            return


def default_data_path() -> Path:
    return Path(__file__).resolve().parents[1] / "data" / "vault.bin"


def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="LiNKskills Vault CLI")
    parser.add_argument(
        "--version",
        action="version",
        version="vault 1.0.0",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit deterministic JSON output",
    )

    subparsers = parser.add_subparsers(dest="command", required=True)

    set_parser = subparsers.add_parser("set", help="Store an encrypted value")
    set_parser.add_argument("key", type=str)
    set_parser.add_argument("value_source", type=str)

    get_parser = subparsers.add_parser("get", help="Read and decrypt a stored value")
    get_parser.add_argument("key", type=str)

    subparsers.add_parser("list", help="List available keys")
    return parser


def main() -> None:
    parser = _build_parser()
    args = parser.parse_args()

    try:
        vault = VaultStore(data_path=default_data_path())
        if args.command == "set":
            result = vault.set_from_file_or_string(args.key, args.value_source)
            payload = {"status": "success", "output": result, "path": str(default_data_path())}
            print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
            return
        if args.command == "get":
            value = vault.get_value(args.key)
            payload = {
                "status": "success",
                "output": {"key": args.key, "value": value},
                "path": str(default_data_path()),
            }
            print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
            return

        keys = vault.list_keys()
        payload = {
            "status": "success",
            "output": {"keys": keys},
            "path": str(default_data_path()),
        }
        print(json.dumps(payload, sort_keys=True, separators=(",", ":")))
    except Exception as exc:
        print(
            json.dumps(
                {
                    "status": "error",
                    "output": str(exc),
                    "path": str(default_data_path()),
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
        raise SystemExit(1) from exc


if __name__ == "__main__":
    main()
