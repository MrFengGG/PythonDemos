import urllib.request
import urllib.parse
import http.cookiejar

url = "http://bbs.chinaunix.net/member.php?mod=logging&action=login&loginsubmit=yes&loginhash=LB6kU"
postdata = urllib.parse.urlencode({
    "username":"15637142735",
    "password":"f43312626"
}).encode("UTF-8")
req = urllib.request.Request(url,postdata)
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
cjar = http.cookiejar.CookieJar()
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
data = urllib.request.urlopen(req).read()
text = data.decode("gbk","ignore")
file = open("f:\\login.html","w")
file.write(text)
url2 = "http://bbs.chinaunix.net/"
req2 = urllib.request.Request(url2,postdata)
req2.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
data = urllib.request.urlopen(req2).read()
file = open("f:\\log2.html","wb")
file.write(data)
file.close()

<a bpfilter="page" href="/u/1858002662?pids=Pl_Official_MyProfileFeed__22&amp;is_search=0&amp;visible=0&amp;is_all=1&amp;is_tag=0&amp;profile_ftype=1&amp;page=4#feedtop" class="page next S_txt1 S_line1" suda-uatrack="key=tblog_profile_v6&amp;value=weibo_page">下一页</a>