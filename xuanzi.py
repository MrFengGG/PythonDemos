import urllib.request
import http.cookiejar

url = "http://www.weibo.com/u/1858002662?c=spr_sinamkt_buy_hyww_weibo_p113&is_all=1"
cjar = http.cookiejar.CookieJar()
'''
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding:gzip, deflate, sdch
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:max-age=0
Connection:keep-alive
Cookie:SCF=AhGAKFK_OZxeh17d4f8-WejRFx8O2C728eCHEAJK1RDv-l3XGksOK9Bsc2g6XKg7EFfItJhGMw6i0OxdKzj5a6w.; SUB=_2AkMuQdiUdcPxrAZSmPsQy2rlaolH-jydlLFiAn7uJhIyOhh77m8WqSWBrst8yUaPw7F08iiuDkvrEV_0UQ..; TC-Page-G0=0dba63c42a7d74c1129019fa3e7e6e7c; _s_tentry=-; UOR=,www.weibo.com,spr_sinamkt_buy_hyww_weibo_p113; Apache=5490222630016.164.1496128033617; SINAGLOBAL=5490222630016.164.1496128033617; ULV=1496128033694:1:1:1:5490222630016.164.1496128033617:; TC-V5-G0=28bf4f11899208be3dc10225cf7ad3c6
Host:www.weibo.com
Upgrade-Insecure-Requests:1
User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36
'''
req = urllib.request.Request(url)
req.add_header("Accept","text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8")
#req.add_header("Accept-Encoding","gzip, deflate, sdch")
req.add_header("Accept-Language","zh-CN,zh;q=0.8")
req.add_header("Cache-Control","max-age=0")
req.add_header("Connection","keep-alive")
req.add_header("Cookie","SCF=AhGAKFK_OZxeh17d4f8-WejRFx8O2C728eCHEAJK1RDv-l3XGksOK9Bsc2g6XKg7EFfItJhGMw6i0OxdKzj5a6w.; SUB=_2AkMuQdiUdcPxrAZSmPsQy2rlaolH-jydlLFiAn7uJhIyOhh77m8WqSWBrst8yUaPw7F08iiuDkvrEV_0UQ..; TC-Page-G0=0dba63c42a7d74c1129019fa3e7e6e7c; _s_tentry=-; UOR=,www.weibo.com,spr_sinamkt_buy_hyww_weibo_p113; Apache=5490222630016.164.1496128033617; SINAGLOBAL=5490222630016.164.1496128033617; ULV=1496128033694:1:1:1:5490222630016.164.1496128033617:; TC-V5-G0=28bf4f11899208be3dc10225cf7ad3c6")
req.add_header("Host","www.weibo.com")
req.add_header("Upgrade-Insecure-Requests","1")
req.add_header("User-Agent","Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36")
opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cjar))
urllib.request.install_opener(opener)
data = urllib.request.urlopen(req).read()
text = data.decode("utf-8","ignore")
file = open("f:\\xuanzijuertu2.html","wb")
file.write(data)
file.close()
