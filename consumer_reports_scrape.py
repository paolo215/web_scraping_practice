import requests
from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import os

filename = "consumer_reports.txt"

def prep():
    url = "http://www.consumerreports.org/cro/a-to-z-index/products/index.htm"
    user_agent = UserAgent()
    chrome = user_agent.chrome
    headers = { "headers" : chrome }
    page = requests.get(url, headers=headers)
    with open(filename, "w") as f:
        f.write(page.content)

prep()

fileObj = open(filename, "r")
contents = fileObj.read()
fileObj.close()

bsoup = BeautifulSoup(contents, "lxml")

products = {}

products = {div.div.a.span.string: div.div.a["href"] for div in bsoup.find_all("div", class_="entry-letter")}


for key, value in products.items():
    print(key, value)    



