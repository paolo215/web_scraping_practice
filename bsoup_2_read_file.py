from bs4 import BeautifulSoup

def read_file():
    fileObj = open("bsoup_2.html", "r")
    data = fileObj.read()
    fileObj.close()
    return data

# Get contents
html = read_file()

# BeautifulSoup(html contents, parser)
bsoup = BeautifulSoup(html, "lxml")

# Prettify
print(bsoup.prettify())
