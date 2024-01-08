#!/usr/bin/python3
""" Displays header value X-Request-Id using requests module
"""
if __name__ == "__main__":
    import sys
    import requests
    url = sys.argv[1]
    response = requests.get(url)
    print(response.headers['X-Request-Id'])
