# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class CaiwuHuiyuancardquery(unittest.TestCase):
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
        #self.base_url = CAIWU_URL
        self.base_url = "http://caiwu03.edaixi.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_caiwu_huiyuancardquery(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rdt4")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("abc123")
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"实体卡").click()
        driver.find_element_by_link_text(u"会员卡").click()
        driver.find_element_by_link_text(u"会员卡查询").click()
        time.sleep(2)
        driver.find_element_by_id("cardno").clear()
        driver.find_element_by_id("cardno").send_keys("10941364")
        driver.find_element_by_name("commit").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"充 值").click()
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
        assert u"财务" in driver.title
        driver.find_element_by_id("icard_recharge_form_zhenqian").clear()
        driver.find_element_by_id("icard_recharge_form_zhenqian").send_keys("10")
        driver.find_element_by_id("icard_recharge_form_money").clear()
        driver.find_element_by_id("icard_recharge_form_money").send_keys("10")
        driver.find_element_by_name("commit").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"扣 款").click()
        #get curruent windows handles
        driver.implicitly_wait(20)
        winBeforeHandle = driver.current_window_handle
        print "winBeforeHandle==",winBeforeHandle
        winHandles = driver.window_handles
        print "winHandles==",winHandles
        for handle in winHandles:
            if winBeforeHandle != handle:
               driver.switch_to_window(handle)

        print driver.title
        assert u"财务" in driver.title
        driver.find_element_by_id("icard_koukuan_form_zhenqian").clear()
        driver.find_element_by_id("icard_koukuan_form_zhenqian").send_keys("3")
        driver.find_element_by_id("icard_koukuan_form_money").clear()
        driver.find_element_by_id("icard_koukuan_form_money").send_keys("3")
        driver.find_element_by_id("btnOn").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"退 款").click()
        time.sleep(2)
        print driver.switch_to_alert().text
        #driver.switch_to_alert().accept()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认退款[\s\S]$")
       
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
