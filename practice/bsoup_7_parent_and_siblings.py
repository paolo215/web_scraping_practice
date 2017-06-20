from bs4 import BeautifulSoup

def read_file():
    fileObj = open("bsoup_2.html")
    data = fileObj.read()
    fileObj.close()
    return data

bsoup = BeautifulSoup(read_file(), "lxml")


head = bsoup.head
title = bsoup.title

# Get parent of this tag
parent = title.parent

p = bsoup.p
div = bsoup.div

# Show parents
# for parent in p.parents:
#     print(parent.name)

# Print siblings. First one is \n
# print(div.next_sibling.next_sibling)
# print(div.next_sibling.previous_sibling)

# Go over next siblings
# for sibling in div.next_siblings:
#     print(sibling if sibling != "\n" else "")

# Go over previous siblings
# for sibling in div.previous_siblings:
#     print(subling if sibling != "\n" else "")







