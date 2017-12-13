import urllib.request
import urllib.error
import urllib.parse
import queue
import datetime
import time
import re
from DiskCache import DiskCache

from bs4 import BeautifulSoup

def download(url, headers, proxy, num_retries, data=None):
    print("正在下载", url)

    request = urllib.request.Request(url, data, headers)
    opener = urllib.request.build_opener(urllib.request.ProxyHandler(proxy))

    try:
        response = opener.open(url)
        html = response.read()
        code = response.code
    except urllib.error.URLError as e:
        print("下载出现错误", e.reason)
        html = ""
        if hasattr(e, "code"):
            code = e.code
            if num_retries > 0 and 500 <= code < 600:
                return download(url, headers, proxy, num_retries - 1, data)
        else:
            code = None
    return html

def normalize(seed_url,link):
    '''
    用于将绝对路径转换为相对路径
    '''
    link,no_need = urllib.parse.urldefrag(link)
    return urllib.parse.urljoin(seed_url,link)

def same_domain(url1,url2):
    '''
    判断域名书否相同
    '''
    return urllib.parse.urlparse(url1).netloc == urllib.parse.urlparse(url2).netloc

def get_links(html):
    '''
    获得一个页面上的所有链接
    '''
    bs = BeautifulSoup(html,"lxml")
    link_labels = bs.find_all("a")
    #for link in link_labels:
    return [link_label.get('href',"default") for link_label in link_labels]

def link_crawler(seed_url,link_regex=".*",delay=5,max_depth=-1,max_urls=-1,headers=None,user_agent="wswp",proxy=None,num_retries=1):
    '''
    用于爬取网站所有链接的爬虫
    :param seed_url: 种子url
    :param link_regex: 需要爬取链接的正则表达式
    :param delay: 爬取网页的延时
    :param max_depth: 爬取网页的深度。默认为最深
    :param max_urls: 爬取网页的数量，默认为最大
    :param headers: 请求头，默认没有
    :param user_agent: 访问的主机名。默认python
    :param proxy: 代理ip，默认没有
    :param num_retries: 出错重新下载的次数
    '''
    crawl_queue = queue.deque([seed_url])

    seen = {seed_url:0}

    num_urls = 0
    throttle = Throttle(delay)

    headers = headers or {}
    if user_agent:
        headers["user-agent"] = user_agent

    while crawl_queue:
        url = crawl_queue.pop()
        print("提出一个url目前队列中有" + str(len(crawl_queue)) + "个链接等待爬取")

        throttle.wait(url)
        html = download(url,headers,proxy = proxy,num_retries = num_retries)
        links = []

        depth = seen[url]
        if depth != max_depth:
            if link_regex:
                links.extend(link for link in get_links(html) if re.match(link_regex,link))
        '''
        linkst = get_links(html)
        for link in linkst:
            print(re.match(link_regex,link))
        return
        '''
        for link in links:
            link = normalize(seed_url,link)
            if link not in seen:
                seen[link] = depth + 1
                print("已遍历" + str(len(seen))+"个链接"+link)
                if same_domain(seed_url,link):
                    crawl_queue.append(link)
                    print("加入一个url目前队列中有"+str(len(crawl_queue))+"个链接等待爬取")
                else:
                    print(link+"不符合要求")
        num_urls += 1
        if num_urls == max_urls:
            break
    print("所有链接下载完毕")
class Throttle:
    '''
    按照延时,请求,代理IP等下载网页,处理网页中的link的类
    '''

    def __init__(self,delay):
        self.delay = delay
        self.domains = {}

    def wait(self,url):
        '''
        每下载一个html之间暂停的时间
        
        '''
        #获得域名
        domain = urllib.parse.urlparse(url).netloc
        #获得上次访问此域名的时间
        las_accessed = self.domains.get(domain)

        if self.delay > 0 and las_accessed is not None:
            #计算需要强制暂停的时间 = 要求的间隔时间 - (现在的时间 - 上次访问的时间)
            sleep_secs = self.delay - (datetime.datetime.now() - las_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        #存储此次访问域名的时间
        self.domains[domain] = datetime.datetime.now()

if __name__ == "__main__":
    link_crawler('http://www.bilibili.com',num_retries=1,delay=0.5)




