# -*- coding: utf-8 -*-
#encoding:utf-8 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
#from org.openqa.selenium.chrome import ChromeDriver

class Opsbanmianfenxiaoxiandan(unittest.TestCase):
    def setUp(self):
        #driver = ChromeDriver()
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
    
    def test_ops_banmianfenxiaoxiandan(self):
        driver = self.driver

        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"版面管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"顶部banner图片").click()
        time.sleep(2)
        driver.back()
        driver.find_element_by_link_text(u"版面管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"大功能按钮管理").click()
        time.sleep(2)
        driver.back()
        driver.find_element_by_link_text(u"版面管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"小功能按钮管理").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"分销系统").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"限单管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"洗衣").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"洗鞋").click()
        #driver.find_element_by_css_selector("ul.dropdown-menu > li > a").click()
        #driver.find_element_by_link_text(u"权限管理").click()
        print driver.title

        #self.assert_(driver.title, u"e袋洗城市运营后台")
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
