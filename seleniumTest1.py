import bs4
import urllib.request
import re

class spider:
    def htmldownloader(self,url):
        data = urllib.request.urlopen(url).read()
        text = data.decode("gbk","ignore")
        return text
    def htmlparser():
        return;

def test():
    s = spider()
    print(s.htmldownloader("http://www.dytt8.net/html/gndy/dyzz/20170530/54108.html"))
        
if __name__ == "__main__":
    test()
