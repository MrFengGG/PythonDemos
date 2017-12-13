import urllib.request

def test():
    data = urllib.request.urlopen("http://api.map.baidu.com/staticimage/v2?ak=3ghFUCcGettQOEa1PpLGzyrXAkeuIDCD&center=116.403874,39.914888&width=300&height=200&zoom=11 ").read()
    file = open("f://1.png","wb")
    file.write(data)
    file.close()

if __name__=="__main__":
    test();
