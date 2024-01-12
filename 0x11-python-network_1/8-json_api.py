#!/usr/bin/python3
""" Checks and Returns the JSON formatting of response from requests
"""


if __name__ == "__main__":
    import sys
    import requests
    url = "http://0.0.0.0:5000/search_user"
    if (len(sys.argv) > 1):
        values = {'q': sys.argv[1]}
    else:
        values = {'q': ""}
        print("No result")
        exit()
    response = requests.post(url, data=values)
    try:
        resp_json = response.json()
        print(f"[{resp_json['id']}] {resp_json['name']}")
    except Exception:
        if response.status_code == 204:
            print("No result")
        else:
            print("Not a valid JSON")
