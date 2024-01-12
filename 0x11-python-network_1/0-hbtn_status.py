#!/usr/bin/python3
"""Module uses urllib library to access webpages
"""
if __name__ == "__main__":
    import urllib.request
    url = "https://alx-intranet.hbtn.io/status"
    with urllib.request.urlopen(url) as response:
        line1 = "Body response:"
        data = response.read()
        data_type = type(data)
        utf8 = data.decode('utf-8')
        print(line1)
        print(f'\t- type: {data_type}')
        print(f'\t- content: {data}')
        print(f'\t- utf8 content: {utf8}')
