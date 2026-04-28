#!/bin/bash
set -e

echo "Setting up fake Codespace environment..."
mkdir -p ~/.vscode-server/extensions
if [[ -f "/workspace/requirements.txt" ]]; then
  python3 -m pip install --user -r /workspace/requirements.txt
else
  python3 -m pip install --user pygments
fi

echo "Fake Codespace setup complete."
