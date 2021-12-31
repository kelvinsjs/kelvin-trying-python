import requests

url = 'https://www.pinterest.com/oauth/'

params = {
    'response_type': 'code',
    'redirect_uri': 'https://mysite.com/',
    'client_id': '1473296',
    'scope': 'boards:read,pins:read',
    'state': '12345ABc'
}

response = requests.get(url, params=params)
print(response.url)