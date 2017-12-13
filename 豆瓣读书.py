import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

URL = "https://book.douban.com/subject_search?search_text=%s&cat=10000"

def save_text(text,filename):
    try:
        file = open(filename,'w')
        file.write(text)
        file.close()
    except  e:
        print("存储失败",str(e))

class html_Downloader:
    def __init__(self,user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36",proxy=None):
        self.user_agent = user_agent
        self.proxy = proxy

    def get_search_url(self,content):
        search_str = ""
        search_str = urllib.parse.quote(content)
        url = URL%search_str
        
        return url
    
    def download_html(self,url):
        request = urllib.request.Request(url)
        request.add_header("User-Agent",self.user_agent)
        if self.proxy:
            opener= urllib.request.build_opener(urllib.requet.ProxyHandler(proxy))
        else:
            opener = urllib.request.build_opener()
        try:
            response = opener.open(request)
            print("code是",response.code)
            html = response.read().decode()
        except Exception as e:
            print("下载错误",str(e))
            html = ""
            print("code;",code)
        print(html)
        return html
    def parser(html):
        doc = BeautifulSoup(html,"lxml")
        ele = doc.findelement
        

if __name__ =="__main__":
    D = html_Downloader()
    url = D.get_search_url("编程")
    D.download_html(url)
    
