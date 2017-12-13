import urllib.request
import urllib.parse
import json
import time
while True:
    
    url= "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc&sessionFrom=dict2.index"

    text = input("请输入需要翻译的内容(输入exit结束):")
    if text == "exit":
        print("程序退出")
        break
    head = {}
    head["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    data = { }
    data["type"] = "AUTO"
    data["i"] = text
    data["doctype"] = "json"
    data["xmlVersion"] = "1.8"
    data["keyfrom:fanyi"] = "web"
    data["ue"] = "UTF-8"
    data["action"] = "FY_BY_CLICKBUTTON"
    data["typoResult"] = "true"
    data = urllib.parse.urlencode(data).encode("utf-8")

    req = urllib.request.Request(url,data,head)
    response = urllib.request.urlopen(req)

    html = response.read().decode("utf-8")
    target = json.loads(html)

    result = target["translateResult"][0][0]["tgt"]
    print(result)


