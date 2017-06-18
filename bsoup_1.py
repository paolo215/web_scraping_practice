from bs4 import BeautifulSoup
import requests

url = "http://example.com"

# HTTP Get request
response = requests.get(url)

# Extract source code
data = response.text

# Create BeautifulSoup object
soup = BeautifulSoup(data, "html.parser")

# Extract all a tags into a list
aTags = soup.find_all("a")


# Print all links 
for tag in aTags:
    print(tag.get("href"))



