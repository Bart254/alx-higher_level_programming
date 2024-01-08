#!/usr/bin/python3
"""Uses requests module for accessing webpages
"""
if __name__ == "__main__":
    import requests
    url = "https://alx-intranet.hbtn.io/status"
    response = requests.get(url)
    data = response.text
    print("Body response:")
    print(f'\t- type: {type(data)}')
    print(f'\t- content: {data}')
