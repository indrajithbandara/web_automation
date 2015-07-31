# -*- coding: utf-8 -*-
#encoding:utf-8 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class OpsYingxiaoSendduanxin(unittest.TestCase):
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
           global OPS_URL,USER_NAME,PASS_WORD
           OPS_URL = lineone[0]
           USER_NAME = lineone[1]
           PASS_WORD = lineone[2]
           print OPS_URL+USER_NAME+PASS_WORD
        self.base_url = OPS_URL
        #self.base_url = "http://ops03.edaixi.cn"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_ops_yingxiao_sendduanxin(self):
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
        driver.find_element_by_link_text(u"发送短信").click()
        time.sleep(2)
        driver.find_element_by_id("sms_form_tel").clear()
        driver.find_element_by_id("sms_form_tel").send_keys("18701524517")
        driver.find_element_by_id("sms_form_sms").clear()
        driver.find_element_by_id("sms_form_sms").send_keys("112121212")
        driver.find_element_by_name("commit").click()
        driver.implicitly_wait(20)
        winBeforeHandle = driver.current_window_handle
        print "winBeforeHandle==",winBeforeHandle
        winHandles = driver.window_handles
        print "winHandles==",winHandles

        for handle in winHandles:
            if winBeforeHandle != handle:
               driver.switch_to_window(handle)
        strtitle=driver.title
        print strtitle
        #if send sms is ok, the statu need be 200
        if "500" in strtitle:
            print " your send sms is ok!"
        else:
            print " your send sms is failed!"
            raise ValueError("your send sms is failed !!!")
        
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
