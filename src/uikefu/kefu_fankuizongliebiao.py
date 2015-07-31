# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class KefuFankuizongliebiao(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        try:
           file=open('C:/edaixi_testdata/userdata_kefu.txt','r')
        except IOError:
           print "The file don't exsit,please check it."
           exit()
        for line in file.readlines():
           lineone=line.split()
           global OPS_URL,USER_NAME,PASS_WORD
           KEFU_URL = lineone[0]
           USER_NAME = lineone[1]
           PASS_WORD = lineone[2]
           print KEFU_URL+USER_NAME+PASS_WORD
        self.base_url = KEFU_URL
        #self.base_url = "http://kefu03.edaixi.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_kefu_fankuizongliebiao(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rdt1")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("abc123")
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"反馈总列表").click()
        driver.find_element_by_link_text(u"已回复").click()
        driver.find_element_by_link_text(u"所有").click()
        driver.find_element_by_link_text(u"已过滤").click()
        driver.find_element_by_link_text(u"处理").click()
        driver.find_element_by_link_text(u"待回复").click()
        driver.find_element_by_link_text(u"调度").click()
        driver.find_element_by_link_text(u"已回复").click()
        driver.find_element_by_link_text(u"已处理").click()
        driver.find_element_by_link_text(u"已过滤").click()
        driver.find_element_by_link_text(u"发 券").click()
        time.sleep(1)
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
