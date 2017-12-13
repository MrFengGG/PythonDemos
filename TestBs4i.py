from bs4 import BeautifulSoup
import urllib.request

data = urllib.request.urlopen("http://www.bilibili.com").read()
html = data.decode("UTF-8","ignore")
bs = BeautifulSoup(html)
eles = bs.find_all("div",class_="cards")
for ele in eles:
    print(ele.text)
