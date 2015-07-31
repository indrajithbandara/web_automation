# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import random
class WuiuCitylistZiyinwuliuxinxi(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://wuliu05.edaixi.cn:81"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wuiu_citylist_ziyinwuliuxinxi(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("test")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("test")
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"城市列表").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"自营物流管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"新建自营物流").click()
        time.sleep(1)
        
        code_list = []
        for i in range(10): # 0-9数字
            code_list.append(str(i))
        for i in range(65, 91): # A-Z
            code_list.append(chr(i))
        for i in range(97, 123): # a-z
            code_list.append(chr(i))
        
        myslice = random.sample(code_list, 6)  # 从list中随机获取6个元素，作为一个片断返回
        verification_code = ''.join(myslice)
        print verification_code
        
        driver.find_element_by_id("courier_form_realname").clear()
        driver.find_element_by_id("courier_form_realname").send_keys(u"自营物流"+verification_code)
        driver.find_element_by_id("courier_form_tel").clear()
        driver.find_element_by_id("courier_form_tel").send_keys("18777711117")
        driver.find_element_by_id("courier_form_id_number").clear()
        driver.find_element_by_id("courier_form_id_number").send_keys("152829292201199")
        driver.find_element_by_id("courier_form_bank_name").clear()
        driver.find_element_by_id("courier_form_bank_name").send_keys(u"招行")
        driver.find_element_by_id("courier_form_bank_card").clear()
        driver.find_element_by_id("courier_form_bank_card").send_keys("622571127222421")
        driver.find_element_by_id("courier_form_saofen").click()
        driver.find_element_by_id("courier_form_shouka").click()
        driver.find_element_by_id("courier_form_password").clear()
        driver.find_element_by_id("courier_form_password").send_keys("123")
        time.sleep(2)
        driver.find_element_by_id("courier_form_start_time").click()
        driver.find_element_by_link_text("1").click()
        driver.find_element_by_id("courier_form_end_time").click()
        driver.find_element_by_link_text("10").click()
        driver.find_element_by_name("commit").click()
        driver.find_element_by_name("commit").click()
        driver.find_element_by_id("realname").clear()
        driver.find_element_by_id("realname").send_keys("lukejun")
        driver.find_element_by_name("commit").click()
        time.sleep(1)
        driver.find_element_by_xpath("//div[@onclick=\"$('#action_target').val(33); $('#map_box').css('visibility', 'visible')\"]").click()
        driver.find_element_by_css_selector("div.pull-right > div.pull-right").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_id("courier_form_realname").clear()
        driver.find_element_by_id("courier_form_realname").send_keys("lukejun111")
        driver.find_element_by_name("commit").click()
        time.sleep(2)
        Select(driver.find_element_by_id("status")).select_by_visible_text(u"否")
        driver.find_element_by_css_selector("div.col-md-2.input-group > span.input-group-btn > input[name=\"commit\"]").click()
        print driver.title
        #self.assert_(expr, msg)
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
