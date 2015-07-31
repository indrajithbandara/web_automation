# -*- coding: utf-8 -*-
#encoding:utf-8 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re

class OpsCategoryguanli(unittest.TestCase):
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
    
    def test_ops_categoryguanli(self):
        driver = self.driver

        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"类目管理").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"类目上线申请").click()
        time.sleep(2)
        driver.back()
        driver.find_element_by_link_text(u"价格体系管理").click()
        #time.sleep(2)
        #driver.find_element_by_link_text(u"新建").click()
        time.sleep(2)
        #Select(driver.find_element_by_id("position_to_role_role_key")).select_by_visible_text(u"市场专员")
        #time.sleep(1)
        #driver.find_element_by_name("commit").click()
        
        #time.sleep(2)
        #driver.find_element_by_link_text(u"编辑").click()
        #Select(driver.find_element_by_id("position_to_role_role_key")).select_by_visible_text(u"营销中心负责人")
        #time.sleep(1)
        #driver.find_element_by_name("commit").click()
        #driver.find_element_by_xpath(u"(//a[contains(text(),'删除')])[6]").click()
        #self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确认删除岗位角色映射[\s\S]$")
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
