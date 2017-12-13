import urllib.request
response = urllib.request.urlopen("http://mimg.xmeise.com/thumb/m/allimg/170406/1-1F406134U2,c_fill,h_100,w_100.jpg")
img = response.read()
try:
    with open("f:/image.jpg","wb") as out:
        out.write(img)
except:
    print("保存失败")
