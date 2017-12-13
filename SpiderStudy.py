import urllib.request

def downloadHtml(link):
    try:
        headers = ("User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36")
        opener = urllib.request.builder_opener()
        opener.addheaders = [headers]
        data = opener.open(link).read()
        peint(data)
    except:urllib.
