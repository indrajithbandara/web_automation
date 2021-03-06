# -*- coding: utf-8 -*-
#encoding:utf-8 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class OpsYingxiaoSendyouhuiquan(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        try:
           file=open('C:/edaixi_testdata/userdata_ops.txt','r')
        except IOError:
           print "The file don't exsit,please check it."
           exit()
        for line in file.readlines():
           lineone=line.split()
           global OPS_URL,USER_NAME,PASS_WORD,UPLOAD_CODE,UPLOAD_FILE
           OPS_URL = lineone[0]
           USER_NAME = lineone[1]
           PASS_WORD = lineone[2]
           UPLOAD_FILE = lineone[3]
           UPLOAD_CODE = lineone[4]
           print OPS_URL+USER_NAME+PASS_WORD+UPLOAD_FILE+UPLOAD_CODE
        self.base_url = OPS_URL
        #self.base_url = "http://ops03.edaixi.cn"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ops_yingxiao_sendyouhuiquan(self):
        driver = self.driver

        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"营销工具").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"发送优惠券").click()
        time.sleep(3)
        #driver.find_element_by_id("send_coupon_form_fan_ids").clear()
        #driver.find_element_by_css_selector("driver")
        driver.find_element_by_id("send_coupon_form_fan_ids").send_keys(UPLOAD_FILE)
        driver.find_element_by_id("send_coupon_form_coupon_id").clear()
        driver.find_element_by_id("send_coupon_form_coupon_id").send_keys(UPLOAD_CODE)
        driver.find_element_by_name("commit").click()
        print driver.title
        self.assert_(driver.title, u"e袋洗城市运营后台")
        file.close()
        
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
