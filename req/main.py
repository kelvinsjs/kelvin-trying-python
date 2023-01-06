import json
import requests
import requests_raw

requests_raw.monkey_patch_all()
session = requests.Session()
res = session.raw(url='https://knu.ua', data=b"GET /cookies/set/name/value HTTP/1.1\r\nHost: knu.ua\r\n\r\n")
print(res)
