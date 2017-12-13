import urllib.request
import http.cookiejar
def downloadHtml(url):
    cjar = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor)
    urllib.request.install_opener(opener)
    req = urllib.request.Request(url)
    req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
    data = urllib.request.urlopen(req).read()
    text = data.decode("utf-8","ignore")
    file = open("f:\\xuanzijuertu.html","w")
    print(text)
    file.write(text)
downloadHtml("http://list.jd.com/list.html?cat=9987,653,655&cu=true&utm_source=click.linktech.cn&utm_medium=tuiguang&utm_campaign=t_4_A100216899fds_google&utm_term=9291b36f88fc4730b458f92f45908149&abt=3")