#!/usr/bin/python3
"""Posts an email to url
"""
if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys
    request = sys.argv[1]
    email = {'email': sys.argv[2]}
    email = urllib.parse.urlencode(email)
    email = email.encode('ascii')
    url = urllib.request.Request(request, email)
    with urllib.request.urlopen(url) as response:
        data = response.read()
        data = data.decode("UTF-8")
        print(data)
