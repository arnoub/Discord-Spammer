import requests
import threading
import time
import random
from colorama import Fore, Style, init

init(autoreset=True)

banner = f"""{Fore.RED}
██████╗ ██╗███████╗ █████╗  █████╗ ██████╗ 
██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗
{Fore.WHITE}██████╔╝██║█████╗  ███████║███████║██║  ██║
██╔═══╝ ██║██╔══╝  ██╔══██║██╔══██║██║  ██║
{Fore.GREEN}██║     ██║███████╗██║  ██║██║  ██║██████╔╝
╚═╝     ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ 
{Style.BRIGHT}{Fore.YELLOW}        BY HAKER ARNOUB
"""

def send_message(webhook_url, content):
    data = {"content": content}
    headers = {
        "Content-Type": "application/json",
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Linux; Android 10; Mobile)",
            "DiscordBot (https://github.com/discord)"
        ])
    }
    try:
        response = requests.post(webhook_url, json=data, headers=headers)
        if response.status_code == 204:
            print(Fore.GREEN + f"[+] Sent: {content}")
        else:
            print(Fore.RED + f"[-] Failed: {response.status_code}")
    except Exception as e:
        print(Fore.RED + f"[!] Error: {e}")

def spam_loop(webhook_url, messages, count, delay):
    def thread_func():
        for _ in range(count):
            content = random.choice(messages)
            send_message(webhook_url, content)
            time.sleep(random.uniform(delay - 0.2, delay + 0.2))

    threads = []
    for _ in range(5):  # عدد الـ Threads
        t = threading.Thread(target=thread_func)
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

def main():
    print(banner)
    webhook_url = input(Fore.CYAN + "[1] Enter Webhook URL: ")

    try:
        total = int(input(Fore.CYAN + "[2] Number of messages to send: "))
    except:
        print(Fore.RED + "[-] Invalid number!")
        return

    try:
        delay = float(input(Fore.CYAN + "[3] Base delay between messages (e.g. 0.5): "))
    except:
        delay = 0.5

    print(Fore.CYAN + "[4] Message type:")
    print("    [1] Random messages")
    print("    [2] Static message")
    print("    [3] Custom input messages")
    msg_type = input("[?] Choose 1/2/3: ")

    messages = []
    if msg_type == '1':
        messages = [
            "This is a powerful test!",
            "Boosted Spammer Active!",
            "Haker Arnoub was here.",
            "Watch your server lag!",
            "You can't stop this bot!",
            "Auto-messages loaded!"
        ]
    elif msg_type == '2':
        msg = input("Enter your static message: ")
        messages = [msg]
    elif msg_type == '3':
        print("Enter custom messages (type 'done' to finish):")
        while True:
            line = input("- ")
            if line.lower() == 'done':
                break
            messages.append(line)
    else:
        print(Fore.RED + "[-] Invalid choice!")
        return

    spam_loop(webhook_url, messages, total, delay)

if __name__ == "__main__":
    main()
