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

## Python package structure

The repository now includes a small Python package under `src/fake_codespace`:

- `src/fake_codespace/app.py` — demo application entry point
- `src/fake_codespace/auth.py` — authentication helpers and token handling
- `src/fake_codespace/utils.py` — formatting and normalization utilities
- `tests/` — simple pytest coverage for auth, utils, and app behavior

### Running the package demo

Inside the container or local environment run:

```bash
python3 run_demo.py alice wonderland
```

### Run tests

```bash
pytest
```
