from selenium import webdriver

browser = webdriver.Chrome()
browser.get("http://www.bilibili.com")

js = "var q=document.body.scrollTop=100000"
browser.execute_script(js)
browser.save_screenshot("f:\\bilibili.png")