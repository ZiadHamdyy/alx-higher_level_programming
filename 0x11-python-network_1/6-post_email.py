#!/usr/bin/python3
"""
Takes in a URL and an email address, sends a POST request to the passed
URL with the email as a parameter, and displays the body of the response
"""


import requests
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    data = {'email': email}

    try:
        response = requests.post(url, data=data)
        response.raise_for_status()  # Check for HTTP errors

        print(f"Your email is: {email}")
        print(response.text)

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
