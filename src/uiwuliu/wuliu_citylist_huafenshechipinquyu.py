# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class WuliuCitylistHuafenzhongbaoquyu1111(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://wuliu05.edaixi.cn:81"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wuliu_citylist_huafenzhongbaoquyu1111(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("test")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"城市列表").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"划分奢侈品区域").click()
        time.sleep(1)
        driver.find_element_by_id("address_input").clear()
        driver.find_element_by_id("address_input").send_keys("2323232")
        driver.find_element_by_xpath("(//div[@id='add_polygon_btn'])[2]").click()
        driver.find_element_by_id("end_edit_btn").click()
        time.sleep(1)
        driver.find_element_by_id("address_input").clear()
        driver.find_element_by_id("address_input").send_keys("232323223q232wqw")
        driver.find_element_by_id("add_polygon_btn").click()
        time.sleep(1)
        self.assertEqual(u"未选中区域组", self.close_alert_and_get_its_text())
        driver.find_element_by_xpath("//div[@id='map_container']/div/div/div/canvas[2]").click()
        driver.find_element_by_xpath("(//div[@id='add_polygon_btn'])[2]").click()
        driver.find_element_by_id("end_edit_btn").click()
    
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
