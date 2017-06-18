from bs4 import BeautifulSoup

def read_file():
    fileObj = open("bsoup_2.html")
    data = fileObj.read()
    fileObj.close()
    return data

bsoup = BeautifulSoup(read_file(), "lxml")

# bsoup.tag accesses the first tag
meta = bsoup.meta
div = bsoup.div


# Access attribute
print(meta.get("charset"))

body = bsoup.body
body["style"] = "some style"

print(body["style"])


# Access multi valud attributes (i.e. classes)
print(body["class"])
