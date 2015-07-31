# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class WuliuZhandianchurukuguanli(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://wuliu03.edaixi.cn/"    
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wuliu_zhandianchurukuguanli(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("test")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        driver.find_element_by_xpath("//li[3]/a/b").click()
        time.sleep(1)
        driver.find_element_by_xpath(u"(//a[contains(text(),'出入库查询')])[2]").click()
        time.sleep(1)
        Select(driver.find_element_by_id("in_out_type")).select_by_visible_text(u"出库")
        time.sleep(1)
        driver.find_element_by_name("commit").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"站点出入库管理").click()
        time.sleep(1)
        driver.find_element_by_xpath(u"(//a[contains(text(),'出库')])[2]").click()
        time.sleep(1)
        driver.find_element_by_id("order_key").clear()
        driver.find_element_by_id("order_key").send_keys("00044050375")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"站点出入库管理").click()
        time.sleep(1)
        driver.find_element_by_css_selector("li.dropdown.open > ul.dropdown-menu > li > a").click()
        driver.find_element_by_id("bagsn").clear()
        driver.find_element_by_id("bagsn").send_keys("00044050375")
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
