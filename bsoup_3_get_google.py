import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

user_agent = UserAgent()
headers = {"user-agent": user_agent.chrome}

google_page = requests.get("https://www.google.com", headers=headers).content

bsoup = BeautifulSoup(google_page, "lxml")

print(bsoup.prettify().encode("UTF-8"))

