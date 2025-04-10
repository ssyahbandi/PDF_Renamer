# src/utils.py
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)
LOG_FILE = "log.txt"

def log_message(message, color=Fore.WHITE, include_timestamp=True):
    """Mencetak pesan ke terminal dan menyimpannya ke log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}" if include_timestamp else message
    
    print(f"{color}{log_entry}")
    
    with open(LOG_FILE, "a", encoding="utf-8") as log_file:
        log_file.write(log_entry + "\n")