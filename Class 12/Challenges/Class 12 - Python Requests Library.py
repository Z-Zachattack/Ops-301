#!/usr/bin/env python3

# Script Name:                  Ops-301d10 - Class 12
# Author:                       Zachariah Woodbridge
# Date of latest revision:      12 Dec 2023
# Purpose:                      Ops Challenge: requests

# I used chatGPT for learning colorama and cleaning up the status_messages dictionary.

# Imports
import requests
from colorama import Fore, Style

# Main

# Selects an address
address = input("Enter the destination URL(example: google.com): ")
url = f"https://{address}"


# Selects an HTTP Method
http_method = input("Select an HTTP Method (get, post, put, delete, head, patch, options): ")

# Asks for confirmation
print("you have selected the following URL:", Fore.GREEN + url, Style.RESET_ALL, 
"\nwith the following HTTP Method:", Fore.GREEN + http_method, Style.RESET_ALL)
confirmation = input("Do you want to proceed? (y/n): ")

if confirmation.lower() != "y":
    print("Request cancelled.")
    exit()

# Sends the request
response = requests.request(http_method, url)

# Print the status code
status_code = response.status_code
print(f"{Fore.BLUE}\nResponse:", Style.RESET_ALL)
print("Status Code:", Fore.YELLOW + str(status_code), Style.RESET_ALL)

# Translate the status code into plain terms
status_messages = {
    200: f"{Fore.GREEN}OK",
    201: f"{Fore.GREEN}Created",
    204: f"{Fore.RED}No Content",
    400: f"{Fore.RED}Bad Request",
    401: f"{Fore.RED}Unauthorized",
    403: f"{Fore.RED}Forbidden",
    404: f"{Fore.YELLOW}Not Found",
    500: f"{Fore.YELLOW}Internal Server Error"
}
# Print the message
if status_code in status_messages:
    message = status_messages[status_code]
    print(Fore.WHITE +"Message:", message, Style.RESET_ALL)
input("Press Enter to continue...")

# Print the response headers
print(f"{Fore.BLUE}\nResponse Headers:")
for header, value in response.headers.items():
    print(f'{Fore.WHITE}' + header + ":", f'{Fore.YELLOW}' + value, Style.RESET_ALL)
# Exit
