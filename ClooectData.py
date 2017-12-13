import urllib.request
import bs4;
import re;



def download_html(url,proxy = None,user_agent="Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.94 Safari/537.36"):
    opener = urllib.request.build_opener()
    headers = {"User-agent":user_agent}
    if proxy:
        proxy_support = urllib.request.ProxyHandler(proxy)
        opener.add_handler(proxy_support)
    urllib.request.install_opener(opener)
    request = urllib.request.Request(url,headers=headers)
    content = urllib.request.urlopen(request)
    html = content.read().decode()
    return html

def parser(html):
    doc = bs4.BeautifulSoup(html,"lxml")
    lists = doc.find_all("div",class_="list-info");
    for list in lists:
        messages = list.find_all("p",class_="baseinfo")
        for message in messages:
            inner_message = message.find_all("span");
            print("房间数量:",inner_message[0].text.replace(" ",""))
            print("房间大小:",inner_message[1].text.replace(" ",""))
            print("房间方向:",inner_message[2].text.replace(" ",""))
            print("")




if __name__ =="__main__":
    html = download_html("http://zz.58.com/ershoufang/pn1/")
    parser(html)