import requests
import random
import time
from colorama import Fore, Style

# Function to display messages in colors
def colored_message(message, color):
    colors = {
        "green": Fore.GREEN,
        "red": Fore.RED,
        "blue": Fore.BLUE,
        "yellow": Fore.YELLOW,
        "magenta": Fore.MAGENTA
    }
    print(colors.get(color, Fore.WHITE) + message + Style.RESET_ALL)

# Function to send message
def send_message(webhook_url, message):
    payload = {
        "content": message
    }
    try:
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            colored_message(f"[+] Message sent: {message}", "green")
        else:
            colored_message(f"[-] Failed to send message!", "red")
    except requests.exceptions.RequestException as e:
        colored_message(f"[-] Error occurred: {e}", "red")

# Function for random messages
def random_message():
    messages = [    "الهاكر التونسي @everyone @here @everyone @here تم اختراق السرفر@everyone @here تم اختراق السرفر@everyone @here تم اختراق السرفر@everyone @here تم اختراق السرفر@everyone @here تم اختراق السرفر@everyone @here تم اختراق السرفر@everyone @here تم اختراق السرفر@everyone @here تم اختراق السرفر@everyone @here تم اختراق السرفر@everyone @here تم اختراق السرفر@everyone @here تم اختراق السرفر@everyone @here تم اختراق السرفر@everyone @here تم اختراق السرفر@everyone @here تم اختراق السرفر@everyone @here تم اختراق السرفر@everyone @here تم اختراق السرفر@everyone @here تم اختراق السرفر@e تم اختراق السرفر",
    "@everyone @here تم اختراق السرفر عصب ",
    "هل تتحمل النظام؟ @everyone @here تم اختراق السرفر",
    "رسالة عشوائية للاختراق @everyone @here تم اختراق السرفر",
    " @everyone @here تم اختراق السرفر!",
    "@everyone @here تم اختراق السرفر",
    "هل يوجد حماية هنا؟ @everyone @here تم اختراق السرفر",
    "رسالة من البوت @everyone @here تم اختراق السرفر",
    "مفاجأة!",
    "عشوائي جداً @everyone @here تم اختراق السرفر!""Hello!", "How are you?", "Welcome to the server!", "Sent from the tool!"]
    return random.choice(messages)

# Function to start spamming
def start_spamming(webhook_url, num_threads, message_type):
    colored_message(f"[*] Starting to send messages to {webhook_url}", "blue")
    
    for _ in range(num_threads):
        if message_type == 1:
            message = random_message()
        else:
            message = "Fixed message from the tool"
        
        send_message(webhook_url, message)
        time.sleep(1)  # Slight delay between messages to avoid getting blocked

# User Interface
def main():
    print(Fore.CYAN + "===================================")
    print(Fore.CYAN + "      Discord Spammer Tool         ")
    print(Fore.CYAN + "        By haker arnoub            ")
    print(Fore.CYAN + "===================================")

    webhook_url = input(Fore.YELLOW + "[1] Enter your Webhook URL: ")
    try:
        num_threads = int(input(Fore.YELLOW + "[2] Enter number of messages: "))
        message_type = int(input(Fore.YELLOW + "[3] Choose message type:\n    [1] Random\n    [2] Fixed\nChoose (1 or 2): "))
        if message_type not in [1, 2]:
            raise ValueError("Invalid selection!")
    except ValueError as e:
        colored_message(f"[-] Error: {e}", "red")
        return

    start_spamming(webhook_url, num_threads, message_type)

if __name__ == "__main__":
    main()
