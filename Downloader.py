import urllib.request
import time
import datetime
import re
import socket
import random
from DiskCache import DiskCache

DEFAULT_AGENT = "wswp"
DEFAULT_DELAY = 5
DEFAULT_RETRIES = 1
DEFAULT_TIMEOUT = 60

class Downloader:
    def __init__(self,proxies=None,delay = DEFAULT_DELAY,user_agent = DEFAULT_AGENT,num_retries = DEFAULT_RETRIES,timeout = DEFAULT_TIMEOUT,opener = None,cache=None):
        #设置超时时间
        socket.setdefaulttimeout(timeout)
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
        self.num_retries = num_retries
        self.opener = opener
        self.cache = cache

    def   __call__(self,url):
        '''
        带有缓存功能的下载方法,通过类对象可以直接调用
        '''
        result = None
        if self.cache:
            try:
                result = self.cache[url]
            except KeyError:
                pass
            else:
                #如果是未成功下载的网页,重新下载
                if self.num_retries > 0 and 500<result["code"]<600:
                    result = None
        if result is None:
            #如果页面不存在,下载该页面
            self.throttle.wait(url)
            if self.proxies:
                proxy = random.choice(self.proxies)
            else:
                proxy = None
            headers = {"User-agent":self.user_agent}
            result = self.download(url,headers,proxy = proxy,num_retries = self.num_retries)

            if self.cache:
                #缓存网页
                self.cache[url] = result
        return result["html"]


    def download(self,url,headers,proxy,num_retries,data=None):
        '''
        用于下载一个页面,返回页面和与之对应的状态码
        '''
        print("开始下载",url)
        #构建请求
        request = urllib.request.Request(url,data,headers or {})
        opener = self.opener or urllib.request.build_opener()
        if proxy:
            #如果有代理IP,使用代理IP
            opener = urllib.request.build_opener(urllib.request.ProxyHandler(proxy))
        try:
            #下载网页
            response = opener.open(request)
            html = response.read()
            code = response.code
        except Exception as e:
            print("下载出现错误",str(e))
            html = ''
            if hasattr(e,"code"):
                code =e.code
                print("num"+str(type(num_retries)))
                print(type(code))
                if num_retries > 0 and 500<code<600:
                    #如果错误不是未找到网页,则重新下载num_retries次
                    print("num-1:",num_retries-1)
                    return self.download(url,headers,proxy,num_retries-1,data)
            else:
                code = None
        print(url+"下载完毕")
        return {"html":html,"code":code}


class Throttle:
    '''
    按照延时,请求,代理IP等下载网页,处理网页中的link的类
    '''

    def __init__(self, delay):
        self.delay = delay
        self.domains = {}

    def wait(self, url):
        '''
        每下载一个html之间暂停的时间

        '''
        # 获得域名
        domain = urllib.parse.urlparse(url).netloc
        # 获得上次访问此域名的时间
        las_accessed = self.domains.get(domain)

        if self.delay > 0 and las_accessed is not None:
            # 计算需要强制暂停的时间 = 要求的间隔时间 - (现在的时间 - 上次访问的时间)
            sleep_secs = self.delay - (datetime.datetime.now() - las_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        # 存储此次访问域名的时间
        self.domains[domain] = datetime.datetime.now()