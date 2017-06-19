from bs4 import BeautifulSoup

def read_file():
    fileObj = open("bsoup_2.html")
    data = fileObj.read()
    fileObj.close()
    return data

bsoup = BeautifulSoup(read_file(), "lxml")


head = bsoup.head

# Returns direct children
# print(head.contents)

# Descendants
for idx, child in enumerate(bsoup.body.descendants):
    print(idx, child)
