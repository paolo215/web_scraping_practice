from bs4 import BeautifulSoup
import re

def read_file():
    fileObj = open("bsoup_2.html")
    data = fileObj.read()
    fileObj.close()
    return data

bsoup = BeautifulSoup(read_file(), "lxml")

# Searching for tags
# find() and find_all()
# print(bsoup.find("p"))
# print(bsoup.find_all("p"))


# Use regex to find tags
# regex = re.compile("^p")
# for tag in bsoup.find_all(regex):
#    print(tag.name)


# Find multiple tags
# for tag in bsoup.find_all(["p", "div"]):
#     print(tag.name)


def has_class(tag):
    return tag.has_attr("class")

# Pass in function
# for tag in bsoup.find_all(has_class):
#     print(tag.name)



# Passing in attrs
# print(bsoup.find_all("p", attrs={"style" : "color: red;"}))



# Search tag with given string
tags = bsoup.find_all(string=re.compile("First"))

# Use kwargs
tags = bsoup.find_all(class_="first")


# Recursive search
title = bsoup.find_all("title", recursive=True)



