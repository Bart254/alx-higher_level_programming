#!/usr/bin/python3
""" Displaying error code with urllib
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            data = response.read()
            data = data.decode('utf-8')
            print(data)
    except urllib.error.HTTPError as error:
        print(error.code)
