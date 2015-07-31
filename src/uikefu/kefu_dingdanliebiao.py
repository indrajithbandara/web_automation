# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class KefuDingdanliebiao(unittest.TestCase):
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
    
    def test_kefu_dingdanliebiao(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rdt1")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("abc123")
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"订单列表").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"新建订单").click()
        time.sleep(1)
        Select(driver.find_element_by_id("new_order_form_good")).select_by_visible_text(u"洗衣")
        time.sleep(1)
        driver.find_element_by_id("new_order_form_totalnum").clear()
        driver.find_element_by_id("new_order_form_totalnum").send_keys("12")
        driver.find_element_by_id("new_order_form_username").clear()
        driver.find_element_by_id("new_order_form_username").send_keys("1111122ssss")
        driver.find_element_by_id("new_order_form_tel").clear()
        driver.find_element_by_id("new_order_form_tel").send_keys("17811119992")
        driver.find_element_by_id("new_order_form_address").clear()
        driver.find_element_by_id("new_order_form_address").send_keys("beijingchaoyang")
        driver.find_element_by_id("new_order_form_washing_date").send_keys("9")
        #driver.find_element_by_link_text("9").click()
        time.sleep(1)
        Select(driver.find_element_by_id("new_order_form_washing_time")).select_by_visible_text("14:00-16:00")
        time.sleep(1)
        driver.find_element_by_id("new_order_form_remark").clear()
        driver.find_element_by_id("new_order_form_remark").send_keys("1wqwqw")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_xpath("//div[@id='container']/div[2]/div/div/div/button").click()
        time.sleep(1)
        driver.find_element_by_id("order_form_tel").clear()
        driver.find_element_by_id("order_form_tel").send_keys("18711119999")
        driver.find_element_by_id("order_form_remark").clear()
        driver.find_element_by_id("order_form_remark").send_keys("1wqwqw22222")
        driver.find_element_by_id("order_form_address_song").clear()
        driver.find_element_by_id("order_form_address_song").send_keys("beijingchaoyang222")
        #driver.find_element_by_name("commit").click()

        Select(driver.find_element_by_id("order_form_washing_time")).select_by_visible_text("22:00-24:00")
        #driver.find_element_by_name("commit").click()
        driver.find_element_by_id("order_form_washing_date").send_keys("14")
        #driver.find_element_by_link_text("14").click()
        driver.find_element_by_name("commit").click()
        
        time.sleep(3)
        
    
        print driver.title
        
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
