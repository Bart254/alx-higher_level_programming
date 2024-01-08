#!/usr/bin/python3
"""Posts into a server using requests module
"""
if __name__ == "__main__":
    import sys
    import requests
    url = sys.argv[1]
    email = {'email':  sys.argv[2]}
    response = requests.post(url, data=email)
    print(response.text)
