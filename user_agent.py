import requests
from fake_useragent import UserAgent

user_agent = UserAgent()

headers = {"user-agent": user_agent.chrome}

# GET Request with headers
page = requests.get("https://www.google.com", headers=headers)

# GET Requests with headers and timeout
page = requests.get("https://www.google.com", timeout=3, headers=headers)

