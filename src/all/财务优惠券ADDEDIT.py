# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class ADDEDIT(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://caiwu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_a_d_d_e_d_i_t(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rdt4")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("abc123")
        driver.find_element_by_id("login-submit").click()
        
        #driver.find_element_by_link_text(u"优惠券").click()
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child(2).dropdown a.dropdown-toggle").click()
       #driver.find_element_by_link_text(u"优惠券列表").click()
        driver.find_element_by_css_selector("ul.nav.navbar-nav li:nth-child(2).dropdown ul.dropdown-menu li:first-child a").click()
        
        driver.find_element_by_link_text(u"新 建").click()
        driver.find_element_by_id("coupon_list_form_title_alias").clear()
        driver.find_element_by_id("coupon_list_form_title_alias").send_keys(u"优惠券添加新测试")
        driver.find_element_by_id("coupon_list_form_title").clear()
        driver.find_element_by_id("coupon_list_form_title").send_keys(u"优惠券添加新测试账户")
        driver.find_element_by_id("coupon_list_form_totalnum").clear()
        driver.find_element_by_id("coupon_list_form_totalnum").send_keys("12")
        driver.find_element_by_id("coupon_list_form_least_price").clear()
        driver.find_element_by_id("coupon_list_form_least_price").send_keys("100")
        driver.find_element_by_id("coupon_list_form_coupon_price").clear()
        driver.find_element_by_id("coupon_list_form_coupon_price").send_keys("100")
        Select(driver.find_element_by_id("coupon_list_form_coupon_type")).select_by_visible_text(u"实体优惠码")
        driver.find_element_by_id("coupon_list_form_exclusive_channels_1").click()
        driver.find_element_by_id("coupon_list_form_exclusive_channels_3").click()
        driver.find_element_by_id("coupon_list_form_exclusive_channels_2").click()
        driver.find_element_by_id("coupon_list_form_starttime").click()
        driver.find_element_by_link_text("27").click()
        driver.find_element_by_id("coupon_list_form_endtime").click()
        driver.find_element_by_link_text("30").click()
        driver.find_element_by_id("coupon_list_form_apply_department").clear()
        driver.find_element_by_id("coupon_list_form_apply_department").send_keys(u"技术测试部")
        driver.find_element_by_id("coupon_list_form_applicant").clear()
        driver.find_element_by_id("coupon_list_form_applicant").send_keys(u"崔俊")
        Select(driver.find_element_by_id("coupon_list_form_category_id")).select_by_visible_text(u"洗衣")
        Select(driver.find_element_by_id("coupon_list_form_coupon_group_id")).select_by_visible_text("testyouhuiquangrup")
        driver.find_element_by_id("coupon_list_form_channel").clear()
        driver.find_element_by_id("coupon_list_form_channel").send_keys(u"网上")
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
