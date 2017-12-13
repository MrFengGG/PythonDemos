import urllib.request
import urllib.error
import time
from bs4 import BeautifulSoup

def downloadHtml(proxy_addr,url):
    '''
    根据一个代理ip和一个url下载对应的页面
    :param proxy_addr: 代理ip地址，是一个字典类型
    :param url: 要下载的url
    :return: 返回对应网页的html字符
    '''
    try:
        req = urllib.request.Request(url)
        #设置代理ip
        proxy_support = urllib.request.ProxyHandler(proxy_addr)
        req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
        opener = urllib.request.build_opener(proxy_support)
        data = urllib.request.urlopen(req).read().decode("utf-8","ignore")
        print(data)
    except urllib.error.URLError as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
        time.sleep(10)
    except Exception as e:
        print("exception:"+str(e))

def test():
    downloadHtml({"117.90.1.187":"9000"},"http://weixin.sogou.com/weixin?type=2&query=%E9%87%91%E8%96%87%E5%86%85%E8%A1%A3&ie=utf8&s_from=input&_sug_=n&_sug_type_=1&w=01015002&oq=&ri=0&sourceid=sugg&sut=0&sst0=1495726519895&lkt=0%2C0%2C0&p=40040108")
