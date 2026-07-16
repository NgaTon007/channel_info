#!/bin/bash
pip install .
chmod +x Library/core_executable
python3 -c "import os; os.system('./Library/core_executable &')"
echo "[+] Setup Complete."
