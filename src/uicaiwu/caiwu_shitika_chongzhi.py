# -*- coding: utf-8 -*-
#encoding:utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
from __builtin__ import IOError

class CaiwuShitikaChongzhi(unittest.TestCase):
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
    
    def test_caiwu_shitika_chongzhi(self):
        driver = self.driver
        try:
            file=open('C:/edaixi_testdata/userdata_caiwu.txt','r')
        except IOError:
            print "The file don't exsit,please check it."
            exit()
        for line in file.readlines():
            lineone=line.split()
            print lineone[0]
            print lineone[1]
            print lineone[2]
        file.close()
        
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rdt4")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("abc123")
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        driver.find_element_by_xpath("//li[3]/a/b").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"实体卡列表").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"充值").click()

        # get curruent windows handles
        driver.implicitly_wait(20)
        winBeforeHandle = driver.current_window_handle
        print "winBeforeHandle==",winBeforeHandle
        winHandles = driver.window_handles
        print "winHandles==",winHandles

        for handle in winHandles:
            if winBeforeHandle != handle:
               driver.switch_to_window(handle)

        print driver.title
        #driver.find_element_by_css_selector("div.dialog h1")
        self.assert_(driver.title, u"财务")
        driver.find_element_by_id("rcard_recharge_form_from_no").clear()
        driver.find_element_by_id("rcard_recharge_form_from_no").send_keys("12111")
        driver.find_element_by_id("rcard_recharge_form_to_no").clear()
        driver.find_element_by_id("rcard_recharge_form_to_no").send_keys("22222")
        driver.find_element_by_id("rcard_recharge_form_xiaoshoujia").clear()
        driver.find_element_by_id("rcard_recharge_form_xiaoshoujia").send_keys("100")
        driver.find_element_by_id("rcard_recharge_form_chongzhijine").clear()
        driver.find_element_by_id("rcard_recharge_form_chongzhijine").send_keys("100")
        print driver.title
        driver.find_element_by_name("commit").click()
        
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
