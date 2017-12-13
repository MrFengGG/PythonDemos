import urllib.request

def downloadHtml(link):
    try:
        #代理IP
        proxy = {"http":"123.179.128.170:8080"}
        proxy_support = urllib.request.ProxyHandler(proxy)
        headers = ( "User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
        opener = urllib.request.build_opener(proxy_support)
        opener.addheaders = [headers]
        urllib.request.install_opener(opener)
        data = opener.open(link).read()
        text = data.decode('utf-8','ignore')
        print(text)
    except urllib.request.URLError as e:
        print(e.reason)
def dowmloadHtml2(link):
    req = urllib.request.Request(link)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
    data = urllib.request.urlopen(req,timeout=1).read()
    text = data.decode("utf-8","ignore")
    print(text)
downloadHtml("http://blog.csdn.net/weiwei_pig/article/details/51178226")