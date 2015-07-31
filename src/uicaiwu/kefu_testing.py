# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class KefuTesting(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://kefu03.edaixi.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_kefu_testing(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rdt1")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("abc123")
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"订单列表").click()
        
        driver.find_element_by_id("order_search_form_tel").clear()
        driver.find_element_by_id("order_search_form_tel").send_keys("187")
        driver.find_element_by_name("commit").click()
        time.sleep(2)
        driver.find_element_by_link_text("1043530").click()
        driver.find_element_by_xpath("//div[@id='container']/div/div/div/div/button").click()
        driver.find_element_by_id("order_form_address_qu").clear()
        driver.find_element_by_id("order_form_address_qu").send_keys(u"国贸大酒店 国贸111")
        #driver.find_element_by_name("commit").click()
        time.sleep(3)
        Select(driver.find_element_by_id("order_form_washing_time")).select_by_visible_text("08:00-10:00")
        #driver.find_element_by_name("commit").click()
        Select(driver.find_element_by_id("order_form_washing_time")).select_by_visible_text("20:00-22:00")
        #driver.find_element_by_name("commit").click()
        driver.find_element_by_id("order_form_washing_date").click()
        driver.find_element_by_link_text("24").click()
        driver.find_element_by_name("commit").click()
        time.sleep(2)
        driver.find_element_by_link_text("1094 1377").click()
        driver.find_element_by_link_text(u"更多").click()
        driver.find_element_by_link_text("623575").click()
        driver.find_element_by_link_text(u"发 券").click()
        driver.find_element_by_link_text(u"发 券").click()
        self.assertEqual(u"确认发券吗？", self.close_alert_and_get_its_text())
    
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
