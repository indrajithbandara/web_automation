# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
#http://selenium-python.readthedocs.org/en/latest/api.html#module-selenium.webdriver.common.action_chains
class CaiwuTestcase01Caiwuordermanagement(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://caiwu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_caiwu_testcase01_caiwuordermanagement(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rdt4")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("abc123")
        driver.find_element_by_id("login-submit").click()
        driver.find_element_by_link_text(u"财务单管理").click()
        driver.find_element_by_id("settlement_search_form_ordersn").clear()
        driver.find_element_by_id("settlement_search_form_ordersn").send_keys("040300362586")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text("040300362586").click()
        driver.find_element_by_id("remark_content").clear()
        driver.find_element_by_id("remark_content").send_keys("hello,testing")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text("10017095").click()
        driver.find_element_by_link_text(u"充 值").click()
        driver.find_element_by_id("icard_recharge_form_money").clear()
        driver.find_element_by_id("icard_recharge_form_money").send_keys("100")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"退 款").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), r"^确认退款[\s\S]$")
        driver.find_element_by_link_text(u"充 值").click()
        driver.find_element_by_id("icard_recharge_form_money").clear()
        driver.find_element_by_id("icard_recharge_form_money").send_keys("1000")
        driver.find_element_by_id("icard_recharge_form_zhenqian").clear()
        driver.find_element_by_id("icard_recharge_form_zhenqian").send_keys("1000")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"扣 款").click()
        driver.find_element_by_id("icard_koukuan_form_money").clear()
        driver.find_element_by_id("icard_koukuan_form_money").send_keys("10")
        driver.find_element_by_id("btnOn").click()
        driver.find_element_by_link_text(u"更多").click()
    
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
