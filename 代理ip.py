import urllib.request
url = "http://ip111.cn/"

list = ["183.196.201.30:8998","115.200.21.240:80","114.230.30.175;3128","171.215.226.32:9000"]
def testip(ip):
    try:
        proxy_support = urllib.request.ProxyHandler({"http":ip})
        opener = urllib.request.build_opener(proxy_support)
        opener.addheaders = [("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")]
        urllib.request.install_opener(opener)
    except:
        return False
for ip in list:
    testip(ip)
    try:
        response = urllib.request.urlopen(url)
        html = response.read().decode("utf-8")
        print(html)
        next = input("是否继续")
        if next == "no":
            break;
    except:
        print(ip+"失效")
        continue
