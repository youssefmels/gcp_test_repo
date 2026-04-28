# gcp_test_repo

## Fake Codespace Setup

This repository includes a minimal fake Codespace configuration for local development.

### Files added

- `.devcontainer/devcontainer.json`
- `.devcontainer/Dockerfile`
- `scripts/fake-codespace-setup.sh`

### How to use

1. Open this repository in VS Code.
2. Install the Remote - Containers extension.
3. Reopen in container and let the setup script run.

The container uses a non-root `codespace` user and installs Python plus basic tools.

### Python demo

Run the sample script inside the container:

```bash
python3 hello.py
```

This prints a friendly message and the current Python version.
