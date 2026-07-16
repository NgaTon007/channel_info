# 🔍 NGA TON - Telegram Channel Analyzer V3

A Python-based Telegram channel analysis tool powered by **Telethon API**.

NGA TON is designed for authorized Telegram channel analysis, message processing, URL detection, and structured report generation.

---

## 🚀 Features

### 📡 Telegram Channel Analysis
- Connect to Telegram using API_ID and API_HASH
- Analyze messages from authorized channels
- Process channel data asynchronously using Telethon

### 🔗 URL & Credential Detection
- Automatically detects HTTP and HTTPS links
- Extracts URLs from message content
- Identifies formatted credentials in public logs
- Stores discovered links and patterns in analysis logs

### 📝 Logging System
- Saves message information automatically
- Records message IDs and message content
- Generates structured output reports

### ⚡ Async Processing
- Built with Python AsyncIO
- Uses Telethon asynchronous client
- Provides stable and efficient message processing

---

# 🛠 Installation

## Requirements

- Python 3.10+
- Telegram API credentials
- Internet connection

---

## Setup

```bash
# Clone repository
git clone https://github.com/NgaTon007/channel_info.git

# Enter project directory
cd channel_info

# Install dependencies
chmod +x install.sh

./install.sh

```
# ⚙ Configuration
Create Telegram API credentials from:
https://my.telegram.org
Required credentials:
 * API_ID
 * API_HASH
# ▶ Usage
Run the application:
```bash
python channel_info.py

```
Enter the required information:
 * API_ID
 * API_HASH
 * Telegram Channel Link
The analyzer will process available messages and save results automatically.
# 📂 Output Structure
```text
output/
│
├── telegram_session.session
│
└── LOG.txt

```
Example log:
```text
MSG_ID: 12345
DATA: Example message content containing credentials admin@gmail.com:password123
LINKS_FOUND: ['[https://example.com](https://example.com)']
CREDS_FOUND: ['admin@gmail.com:password123']
========================================

```
# 🧩 Technologies
 * Python
 * Telethon
 * AsyncIO
 * Regular Expressions
# 🔐 Security Notes
This project is intended for:
 * ✅ Telegram channel research
 * ✅ Data organization
 * ✅ Security learning
 * ✅ Authorized analysis environments
Only analyze Telegram data that you own or have permission to access.
# ⚠ Disclaimer
This project is provided for educational and authorized use only.
Users are responsible for complying with:
 * Telegram Terms of Service
 * Privacy regulations
 * Applicable laws
The developer is not responsible for misuse of this software.
# 👤 Author
**NGA TON FROM LOD** Security Research & Development
