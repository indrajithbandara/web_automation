# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import random
class WuliuCitylistShouyidianguanli(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://wuliu05.edaixi.cn:81"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wuliu_citylist_shouyidianguanli(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("test")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("login-submit").click()
        
                 #get a random str and send to bianma filed
        code_list = []
        for i in range(10): # 0-9数字
            code_list.append(str(i))
        for i in range(65, 91): # A-Z
            code_list.append(chr(i))
        for i in range(97, 123): # a-z
            code_list.append(chr(i))
        
        myslice = random.sample(code_list, 6)  # 从list中随机获取6个元素，作为一个片断返回
        verification_code = ''.join(myslice)
        print verification_code
        
        
        time.sleep(2)
        driver.find_element_by_link_text(u"城市列表").click()
        time.sleep(1)
         
        driver.find_element_by_link_text(u"收衣店管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"新建收衣店").click()
        time.sleep(1)
        driver.find_element_by_id("outlet_form_title").clear()
        driver.find_element_by_id("outlet_form_title").send_keys(u"收衣店"+verification_code)
        driver.find_element_by_id("outlet_form_tel").clear()
        driver.find_element_by_id("outlet_form_tel").send_keys("13511110022")
        Select(driver.find_element_by_id("outlet_form_area")).select_by_visible_text(u"海淀区")
        driver.find_element_by_id("outlet_form_address").clear()
        driver.find_element_by_id("outlet_form_address").send_keys("haidianyiyuan")
        driver.find_element_by_name("commit").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_id("outlet_form_title").clear()
        driver.find_element_by_id("outlet_form_title").send_keys("shouyiqwqwq11122")
        driver.find_element_by_name("commit").click()
        time.sleep(1)
        driver.find_element_by_id("title").clear()
        driver.find_element_by_id("title").send_keys(u"收衣店")
        driver.find_element_by_name("commit").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
