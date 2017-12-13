import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


def is_element_exist(driver,id):
    try:
        s = driver.find_element_by_class_name(id)
        return True
    except:
        return False
def login(account, passwd, url):
    # 如果driver没加入环境变量中，那么就需要明确指定其路径
    # 验证于2017年4月11日
    # 直接登陆新浪微博

    #driver = webdriver.PhantomJS("E:/phantomjs-2.1.1-windows/bin/phantomjs.exe")
    driver = webdriver.Chrome()
    driver.maximize_window()
    # locator = (By.)
    driver.get(url)
    print('开始登陆')
    name_field = driver.find_element_by_id('loginname')
    name_field.clear()
    name_field.send_keys("15271183269")
    password_field = driver.find_element_by_class_name('password')
    password_field.clear()
    password_field.send_keys("f43312626")



    submit = driver.find_element_by_xpath('//*[@id="pl_login_form"]/div/div[3]/div[6]/a/span')
    submit.click()
    driver.save_screenshot("f:\\test1.png")
    time.sleep(5)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'WB_miniblog')))
    source = driver.page_source
    file = open("f:/weibo.html","w",encoding="utf-8")
    file.write(source)
    if is_login(source):
        print('登录成功')


    driver.get("http://www.weibo.com/u/1858002662?c=spr_sinamkt_buy_hyww_weibo_p113")
    driver.save_screenshot("f:\\pre1.png")
    js = "var q=document.body.scrollTop=1000000"
    while True:
        driver.execute_script(js)
        time.sleep(1)

        if is_element_exist(driver,"W_pages"):
            break
    a = driver.page_source
    file = open("f:/xuanzi5.html","w",encoding="utf-8")
    file.write(a)
    driver.save_screenshot("f:\\now.png")
    file.close
    driver.quit()


def is_login(source):
    rs = re.search("CONFIG\['islogin'\]='(\d)'", source)
    if rs:
        return int(rs.group(1)) == 1
    else:
        return False


if __name__ == '__main__':
    url = 'http://weibo.com/login.php'
    #name_input = input('请输入你的账号\n')
    #passwd_input = input('请输入你的密码\n')
    login("15271183269","f43312626", url)