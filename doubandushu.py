import urllib.request
import urllib.parse
import re
import threading
from bs4 import BeautifulSoup

URL = "https://book.douban.com/subject_search?search_text=%s&cat=10000"
DOMAIN = "https://book.douban.com"


def save_text(text, filename):
    try:
        file = open(filename, 'w')
        file.write(text)
        file.close()
    except Exception as e:
        print("存储失败", str(e))


class html_Downloader:
    def __init__(self,
                 user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",
                 proxy=None):
        self.user_agent = user_agent
        self.proxy = proxy

    def get_search_url(self, content):
        search_str = ""
        search_str = urllib.parse.quote(content)
        url = URL % search_str
        return url

    def download_html(self, url):
        request = urllib.request.Request(url)
        request.add_header("User-Agent", self.user_agent)
        if self.proxy:
            opener = urllib.request.build_opener(urllib.requet.ProxyHandler(proxy))
        else:
            opener = urllib.request.build_opener()
        try:
            response = opener.open(request)
            code = response.code
            html = response.read().decode()
        except Exception as e:
            print("下载错误", str(e))
            html = ""
            print("code;", code)
        return html

    def parse(self,html):
        book={}
        doc = BeautifulSoup(html, "lxml")
        eles = doc.find_all("li",class_="subject-item")
        for ele in eles:
            book_name = ele.find_all("a")
            book_name = "".join(book_name[1]["title"])
            grade_box = ele.find_all("div", class_="star clearfix")
            grade = grade_box[0].find("span", class_="rating_nums")
            count = grade_box[0].find("span", class_="pl")
            number = re.compile(r"(\d+).+")
            if grade:
                douban = round(float(grade.text), 2)
            else:
                douban = 0
            if count:
                per_num = count.text
            else:
                per_num = "无人评价"
            book[book_name] = [douban, per_num]
        next_page = doc.find("span", class_="next")
        if next_page:
            next_url = DOMAIN+next_page.find("link")["href"]
            print(next_url)
        else:
            next_url = None
        return next_url,book
mylock = threading.Lock()
Book={}
Queue=[]
is_ok = []
def search(name):
    D = html_Downloader()
    url = D.get_search_url(name)
    mylock.acquire()
    if url not in Queue:
        Queue.append(url)
    mylock.release()
    while Queue:
        url = Queue.pop()
        html = D.download_html(url)
        next_url,book = D.parse(html)
        Book.update(book)
        mylock.acquire()
        if next_url and next_url not in Queue:
            Queue.append(next_url)
        mylock.acquire()
    print("完毕")

if __name__=="__main__":
    t1 = threading.Thread(target=search,args = (u"编程",))
    t2 = threading.Thread(target=search,args = (u"编程",))
    t3 = threading.Thread(target=search,args = (u"编程",))
    t1.start()
    t2.start()
    t3.start()