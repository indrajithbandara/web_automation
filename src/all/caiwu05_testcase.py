# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
from selenium.webdriver.support.ui import WebDriverWait 
class Caiwu05Testcase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://caiwu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_caiwu05_testcase(self):
        driver = self.driver
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登陆").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rdt4")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("abc123")
        driver.find_element_by_id("login-submit").click()
        driver.find_element_by_link_text(u"财务单管理").click()
        
        
        Select(driver.find_element_by_id("settlement_search_form_pay_type")).select_by_visible_text(u"现金")
        Select(driver.find_element_by_id("settlement_search_form_pay_status")).select_by_visible_text(u"已付款")
        Select(driver.find_element_by_id("settlement_search_form_caiwu_status")).select_by_visible_text(u"未收款")
        driver.find_element_by_name("commit").click()
        Select(driver.find_element_by_id("settlement_search_form_pay_status")).select_by_visible_text(u"未付款")
        Select(driver.find_element_by_id("settlement_search_form_caiwu_status")).select_by_visible_text(u"已收款")
        driver.find_element_by_name("commit").click()
        Select(driver.find_element_by_id("settlement_search_form_pay_status")).select_by_visible_text(u"已付款")
        Select(driver.find_element_by_id("settlement_search_form_caiwu_status")).select_by_visible_text(u"未收款")
        driver.find_element_by_name("commit").click()        
        
        driver.find_element_by_id("settlement_search_form_ordersn").clear()
        driver.find_element_by_id("settlement_search_form_ordersn").send_keys("040300362586")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text("040300362586").click()
        WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_css_selector("div.container div.info-div div.col-md-6 div.panel.panel-primary.checkout-order div.panel-heading").is_displayed()) 
        
        driver.find_element_by_id("remark_content").clear()
        driver.find_element_by_id("remark_content").send_keys("hello,testing")
        driver.find_element_by_name("commit").click()

        driver.find_element_by_link_text("10017095").click()
        WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_css_selector("div.container").is_displayed()) 

        driver.find_element_by_link_text(u"充 值").click()

        WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_css_selector("div.container").is_displayed())
        driver.find_element_by_id("icard_recharge_form_money").clear()
        driver.find_element_by_id("icard_recharge_form_money").send_keys("1000")
        driver.find_element_by_id("icard_recharge_form_zhenqian").clear()
        driver.find_element_by_id("icard_recharge_form_zhenqian").send_keys("1000")
        driver.find_element_by_name("commit").click()
        WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_css_selector("div.container").is_displayed()) 
       

        driver.find_element_by_link_text(u"扣 款").click()
        driver.find_element_by_id("icard_koukuan_form_money").clear()
        driver.find_element_by_id("icard_koukuan_form_money").send_keys("10")
        driver.find_element_by_id("btnOn").click()
        WebDriverWait(driver, 10).until(lambda the_driver: the_driver.find_element_by_css_selector("div.container").is_displayed()) 
        driver.find_element_by_link_text(u"退 款").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认退款[\s\S]$")
        
        driver.find_element_by_link_text(u"更多").click()
        
        
        driver.find_element_by_link_text(u"优惠券").click()
        driver.find_element_by_link_text(u"优惠券列表").click()
        #driver.find_element_by_link_text(u"新 建").click()
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_link_text(u"生成券").click()
        driver.find_element_by_link_text(u"优惠券").click()
        driver.find_element_by_link_text(u"优惠券列表").click()
        driver.find_element_by_link_text(u"优惠券").click()
        driver.find_element_by_link_text(u"优惠券查询").click()
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"实体卡").click()
        driver.find_element_by_link_text(u"实体卡列表").click()
        driver.find_element_by_link_text(u"实体卡").click()
        driver.find_element_by_link_text(u"实体卡查询").click()
        driver.find_element_by_link_text(u"实体卡").click()
        driver.find_element_by_link_text(u"实体卡列表").click()
        driver.find_element_by_link_text(u"充值卡").click()
        driver.find_element_by_link_text(u"充值卡列表").click()
        driver.find_element_by_link_text(u"新 建").click()
        driver.find_element_by_id("recharge_list_form_title").clear()
        driver.find_element_by_id("recharge_list_form_title").send_keys("testchongzhi")
        driver.find_element_by_id("recharge_list_form_zhenqian").clear()
        driver.find_element_by_id("recharge_list_form_zhenqian").send_keys("11")
        driver.find_element_by_id("recharge_list_form_price").clear()
        driver.find_element_by_id("recharge_list_form_price").send_keys("11")
        driver.find_element_by_id("recharge_list_form_starttime").click()
        driver.find_element_by_link_text("8").click()
        driver.find_element_by_id("recharge_list_form_endtime").click()
        driver.find_element_by_link_text("30").click()
        driver.find_element_by_id("recharge_list_form_apply_department").clear()
        driver.find_element_by_id("recharge_list_form_apply_department").send_keys("ruby")
        driver.find_element_by_id("recharge_list_form_applicant").clear()
        driver.find_element_by_id("recharge_list_form_applicant").send_keys("luke")
        driver.find_element_by_id("recharge_list_form_city").clear()
        driver.find_element_by_id("recharge_list_form_city").send_keys("bejing")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"编辑").click()
        driver.find_element_by_id("recharge_list_form_applicant").clear()
        driver.find_element_by_id("recharge_list_form_applicant").send_keys("luke111")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"分 配").click()
        driver.find_element_by_id("recharge_list_start_num").clear()
        driver.find_element_by_id("recharge_list_start_num").send_keys("111")
        driver.find_element_by_id("recharge_list_end_num").clear()
        driver.find_element_by_id("recharge_list_end_num").send_keys("112")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"充值卡").click()
        driver.find_element_by_link_text(u"充值卡列表").click()
        driver.find_element_by_link_text(u"回 收").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确认回收充值卡[\s\S]$")
        driver.find_element_by_link_text(u"充值卡").click()
        driver.find_element_by_link_text(u"充值卡列表").click()
        driver.find_element_by_link_text(u"导出").click()
        driver.find_element_by_link_text(u"充值卡").click()
        driver.find_element_by_link_text(u"充值卡列表").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"用户").click()
        driver.find_element_by_link_text(u"用户查询").click()

    
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
