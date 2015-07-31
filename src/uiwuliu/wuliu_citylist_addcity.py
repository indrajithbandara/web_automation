# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class WuliuCitylistAddcity(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Ie()
        self.driver.implicitly_wait(30)
        self.base_url = "http://wuliu05.edaixi.cn:81"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wuliu_citylist_addcity(self):
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
        driver.find_element_by_link_text(u"新建城市").click()
        
        Select(driver.find_element_by_id("map_city_api_city_id")).select_by_visible_text(u"上海")
        driver.find_element_by_id("map_city_center_lat").clear()
        driver.find_element_by_id("map_city_center_lat").send_keys("1")
        driver.find_element_by_id("map_city_center_lat").clear()
        driver.find_element_by_id("map_city_center_lat").send_keys("0")
        driver.find_element_by_id("map_city_center_lng").clear()
        driver.find_element_by_id("map_city_center_lng").send_keys("-1")
        driver.find_element_by_id("map_city_search_radius").clear()
        driver.find_element_by_id("map_city_search_radius").send_keys("-1")
        driver.find_element_by_id("map_city_search_radius").clear()
        driver.find_element_by_id("map_city_search_radius").send_keys("-2")
        driver.find_element_by_id("map_city_gaode_map_code").clear()
        driver.find_element_by_id("map_city_gaode_map_code").send_keys("qqsq")
        driver.find_element_by_name("commit").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_id("map_city_gaode_map_code").clear()
        driver.find_element_by_id("map_city_gaode_map_code").send_keys("beijing111")
        driver.find_element_by_name("commit").click()
        #driver.find_element_by_link_text(u"返回").click()
        print driver.title
        self.assert_(driver.title, u"物流")
        #assert u"物流" in driver.titles
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
