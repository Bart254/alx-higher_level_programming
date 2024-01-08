#!/usr/bin/python3
""" Displays the header of of X-Request-Id
"""
if __name__ == "__main__":
    import urllib.request
    import sys
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.info()['X-Request-Id'])
