import urllib.request
response = urllib.request.urlopen("http://www.dytt8.net/index.htm")
html = response.read()
try:
    with open("f:/1.txt","w") as out:
        print(html,file=out)
except:
        print("获取失败")
