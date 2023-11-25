import requests
from termcolor import colored  # for colored printing

def check_http(url):
    try:
        response = requests.get(url)
        print(f"HTTP Status Code for {url}: {response.status_code}")
        if response.status_code == 200:
            print(colored(f"The website {url} is up and running!", 'green'))
        elif response.status_code == 404:
            print(colored(f"Oops! {url} was not found (404 Not Found).", 'red'))
        else:
            print(colored(f"Looks like {url} is having some issues. Status code: {response.status_code}", 'yellow'))
    except requests.RequestException as e:
        print(colored(f"An error occurred: {e}", 'red'))

# Input
url_to_check = input("Please enter the URL you want to check: ")

# Perform HTTP check
check_http(url_to_check)
