from selenium import webdriver
import time
import urllib.request

'''
browser = webdriver.PhantomJS("E:/phantomjs-2.1.1-windows/bin/phantomjs.exe")      #用PhantomJS
browser.maximize_window()                   
browser.get("https://www.duitang.com/search/?kw=%E6%96%87%E8%B1%AA%E9%87%8E%E7%8A%AC&type=feed")
time.sleep(10)
file = open("f:\\4.html","w",encoding="utf-8")
file.write(browser.page_source)
file.close()
browser.quit()
'''
html = urllib.request.urlopen("https://www.duitang.com/search/?kw=%E6%96%87%E8%B1%AA%E9%87%8E%E7%8A%AC&type=feed").read()
file = open("f:\\5.html","wb")
file.write(html)
file.close()

