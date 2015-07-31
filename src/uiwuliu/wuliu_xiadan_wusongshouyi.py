# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class WuliuXiadanWusongshouyi(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://wuliu05.edaixi.cn:81" 
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wuliu_xiadan_wusongshouyi(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("test")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"下单").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"取衣收衣").click()
        time.sleep(1)
        driver.find_element_by_id("ordersn_or_tel").clear()
        driver.find_element_by_id("ordersn_or_tel").send_keys("18701524517")
        driver.find_element_by_name("commit").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"送衣收衣").click()
        Select(driver.find_element_by_id("courier_id")).select_by_visible_text(u"李丹")
        driver.find_element_by_id("ordersn").clear()
        driver.find_element_by_id("ordersn").send_keys("963")
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
