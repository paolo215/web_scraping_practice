from bs4 import BeautifulSoup

def read_file():
    fileObj = open("bsoup_2.html")
    data = fileObj.read()
    fileObj.close()
    return data

bsoup = BeautifulSoup(read_file(), "lxml")


head = bsoup.head
body = bsoup.body

# Using tag.contents
# print(head.contents)


# Using tag.children
for child in body.children:
    print(child)
