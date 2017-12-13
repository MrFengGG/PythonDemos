from selenium import webdriver

#"E:/phantomjs-2.1.1-windows/bin/phantomjs.exe"
browser = webdriver.PhantomJS("E:/phantomjs-2.1.1-windows/bin/phantomjs.exe")
browser.get("http://weibo.com/login.php")
username = browser.find_element_by_id("loginname")
