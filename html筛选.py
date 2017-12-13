import urllib.request
response = urllib.request.urlopen("http://m15637142735.blog.163.com/blog/static/27100401020173129625255/#")
html = response.read()

print(html)

