import requests
import socket
from termcolor import colored  # برای چاپ رنگی

def check_http(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(colored(f"The website {url} is up and running!", 'green'))
        else:
            print(colored(f"Looks like {url} is having some issues. Status code: {response.status_code}", 'red'))
    except requests.RequestException:
        print(colored(f"Oops! Couldn't reach {url}.", 'red'))

def check_tcp(host, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(5)  # زمان محدودیت اتصال
        s.connect((host, port))
        print(colored(f"The TCP connection to {host}:{port} is successful!", 'green'))
    except socket.error:
        print(colored(f"Could not connect to {host}:{port}.", 'red'))
    finally:
        s.close()

# ورودی‌ها
url_to_check = input("Please enter the URL you want to check: ")
host_to_check = input("Please enter the host you want to check: ")
port_to_check = int(input("Please enter the port you want to check: "))

# اجرای توابع چک
check_http(url_to_check)
check_tcp(host_to_check, port_to_check)
