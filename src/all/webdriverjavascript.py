#coding=utf-8
from selenium import webdriver
import time
    
driver = webdriver.Firefox()
driver.get("http://passport.kuaibo.com/login/?referrer=http%3A%2F%2Fvod.kuaibo.com%2F%3Ft%3Dhome")
    
#给用户名的输入框标红
js="var q=document.getElementById(\"user_name\");q.style.border=\"1px solid red\";"
#调用js
driver.execute_script(js)
time.sleep(3)
    
driver.find_element_by_id("user_name").send_keys("username")
driver.find_element_by_id("user_pwd").send_keys("password")
driver.find_element_by_id("dl_an_submit").click()
time.sleep(3)
    
driver.quit()