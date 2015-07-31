# -*- coding: utf-8 -*-
#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class CaiwuYouhuiquanlistModify(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        try:
           file=open('C:/edaixi_testdata/userdata_caiwu.txt','r')
        except IOError:
           print "The file don't exsit,please check it."
           exit()
        for line in file.readlines():
           lineone=line.split()
           global OPS_URL,USER_NAME,PASS_WORD
           CAIWU_URL = lineone[0]
           USER_NAME = lineone[1]
           PASS_WORD = lineone[2]
           print CAIWU_URL+USER_NAME+PASS_WORD
        self.base_url = CAIWU_URL
        #self.base_url = "http://caiwu03.edaixi.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_caiwu_youhuiquanlist_modify(self):
        driver = self.driver
    
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rdt4")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("abc123")
        driver.find_element_by_id("login-submit").click()
        driver.find_element_by_link_text(u"优惠券").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"优惠券列表").click()
        #driver.find_element_by_css_selector("div.container div#content div.panel.panel-primary table.table.table-striped tbody tr td:nth-child(1)").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_id("coupon_list_form_title_alias").clear()
        driver.find_element_by_id("coupon_list_form_title_alias").send_keys("asass")
        driver.find_element_by_id("coupon_list_form_title").clear()
        driver.find_element_by_id("coupon_list_form_title").send_keys("asasasa")
        driver.find_element_by_id("coupon_list_form_totalnum").clear()
        driver.find_element_by_id("coupon_list_form_totalnum").send_keys("123")
        driver.find_element_by_id("coupon_list_form_least_price").clear()
        driver.find_element_by_id("coupon_list_form_least_price").send_keys("10")
        driver.find_element_by_id("coupon_list_form_coupon_price").clear()
        driver.find_element_by_id("coupon_list_form_coupon_price").send_keys("8")
        driver.find_element_by_id("coupon_list_form_apply_department").clear()
        driver.find_element_by_id("coupon_list_form_apply_department").send_keys("test")
        driver.find_element_by_id("coupon_list_form_applicant").clear()
        driver.find_element_by_id("coupon_list_form_applicant").send_keys("luke")
        driver.find_element_by_name("commit").click()

        print driver.title
        self.assert_(driver.title, u"财务")
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except Exception, e: return False
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
