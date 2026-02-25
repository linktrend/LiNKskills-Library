# sandbox

## Capability Summary
Ephemeral containerized command runner for controlled execution. Use to execute shell commands inside a temporary Docker container with memory limits and no network by default.

## Commands
- `run "<command>"`
  - Executes the command in `python:3.11-slim` with the current working directory mounted at `/workspace`.

## CLI
- `--help`
- `--version`
- `--json`

## Safety Defaults
- Memory limit: `512m`
- Network: disabled by default
- Containers: removed immediately after execution

## Usage
- `bin/sandbox-run "python3 -V"`
- `bin/sandbox-run --allow-network "pip index versions requests"`
