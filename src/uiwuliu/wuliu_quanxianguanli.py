# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class WuliuQuanxianguanli(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://wuliu05.edaixi.cn:81"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wuliu_quanxianguanli(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("test")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("login-submit").click()
        time.sleep(1)
        
        driver.find_element_by_link_text(u"权限管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"编辑权限").click()
        time.sleep(1)
        driver.find_element_by_id("worker_is_shouyidian").click()
        time.sleep(1)
        driver.find_element_by_id("worker_is_jiagongdian").click()
        #time.sleep(1)
        #driver.find_element_by_id("worker_is_admin").send_keys("3").click()
        #driver.find_element_by_link_text("3").click()
        #driver.find_element_by_id("name").clear()
        #driver.find_element_by_id("name").send_keys(u"黄陆洋")
        driver.find_element_by_name("commit").click()
        print driver.title
        self.assert_(driver.title, u"物流")
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
