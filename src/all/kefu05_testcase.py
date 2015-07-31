# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class Kefu05Testcase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://kefu05.edaixi.cn:81/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_kefu05_testcase(self):
        driver = self.driver
        driver.get(self.base_url + "/")

        driver.find_element_by_link_text(u"登陆").click()
        print driver.title,"UI Testing starting......"
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys("rdt1")
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys("abc123")
        driver.find_element_by_id("login-submit").click()
        
        driver.find_element_by_link_text(u"反馈总列表").click()
        driver.find_element_by_link_text(u"已回复").click()
        driver.find_element_by_link_text(u"所有").click()
        driver.find_element_by_link_text(u"已过滤").click()
        driver.find_element_by_link_text(u"处理").click()
        driver.find_element_by_link_text(u"发 券").click()
        
        driver.find_element_by_link_text(u"发 券").click()
        self.assertEqual(u"确认发券吗？", self.close_alert_and_get_its_text())
        
        driver.find_element_by_link_text(u"我的用户反馈").click()
        driver.find_element_by_link_text(u"处理").click()
        driver.find_element_by_link_text(u"发 券").click()
        driver.find_element_by_link_text(u"发 券").click()
        self.assertEqual(u"确认发券吗？", self.close_alert_and_get_its_text())
        driver.find_element_by_link_text(u"订单列表").click()
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"新建订单").click()
        Select(driver.find_element_by_id("new_order_form_good")).select_by_visible_text(u"洗衣")
        driver.find_element_by_id("new_order_form_totalnum").clear()
        driver.find_element_by_id("new_order_form_totalnum").send_keys("1")
        driver.find_element_by_id("new_order_form_coupon_sn").clear()
        driver.find_element_by_id("new_order_form_coupon_sn").send_keys("111222")
        driver.find_element_by_id("new_order_form_username").clear()
        driver.find_element_by_id("new_order_form_username").send_keys("testuser")
        driver.find_element_by_id("new_order_form_tel").clear()
        driver.find_element_by_id("new_order_form_tel").send_keys("18611110002")
        driver.find_element_by_id("new_order_form_address").clear()
        driver.find_element_by_id("new_order_form_address").send_keys("beijingjiangtailu")
        driver.find_element_by_id("new_order_form_washing_date").click()
        driver.find_element_by_link_text("23").click()
        Select(driver.find_element_by_id("new_order_form_washing_time")).select_by_visible_text("18:00-20:00")
        driver.find_element_by_id("new_order_form_remark").clear()
        driver.find_element_by_id("new_order_form_remark").send_keys("111")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"订单列表").click()
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"标签管理").click()
        driver.find_element_by_id("add_tag_1").click()
        driver.find_element_by_id("tag_name").clear()
        driver.find_element_by_id("tag_name").send_keys("tag1")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_id("add_tag").click()
        driver.find_element_by_id("tag_name").clear()
        driver.find_element_by_id("tag_name").send_keys("tagcomment1")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"常用回复").click()
        driver.find_element_by_id("content").clear()
        driver.find_element_by_id("content").send_keys("hell i love u")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_css_selector("div.col-md-5 > form > div.input-group > #content").clear()
        driver.find_element_by_css_selector("div.col-md-5 > form > div.input-group > #content").send_keys("love")
        driver.find_element_by_css_selector("div.col-md-5 > form > div.input-group > span.input-group-btn > input[name=\"commit\"]").click()
        driver.find_element_by_link_text(u"删除").click()
        self.assertRegexpMatches(self.close_alert_and_get_its_text(), u"^确定删除[\s\S]$")
        time.sleep(2)
        #driver.find_element_by_link_text(u"工单").click()
        #driver.find_element_by_link_text(u"工单列表").click()
        driver.find_element_by_link_text(u"常用查询").click()
        driver.find_element_by_link_text(u"优惠券查询").click()
        driver.find_element_by_link_text(u"常用查询").click()
        driver.find_element_by_link_text(u"实体卡查询").click()
        driver.find_element_by_link_text(u"常用查询").click()
        driver.find_element_by_link_text(u"电子卡查询").click()
        driver.find_element_by_link_text(u"常用查询").click()
        driver.find_element_by_link_text(u"电子卡查询").click()
        driver.find_element_by_link_text(u"常用查询").click()
        
        driver.find_element_by_link_text(u"用户查询").click()
        driver.find_element_by_link_text(u"常用查询").click()
        driver.find_element_by_link_text(u"充值码查询").click()
        driver.find_element_by_link_text(u"常用查询").click()
        driver.find_element_by_link_text(u"衣物查询").click()
        driver.find_element_by_link_text(u"常用查询").click()
        driver.find_element_by_xpath("//div[@id='container']/table/tbody/tr/th[3]").click()
        driver.find_element_by_link_text(u"常用查询").click()
        driver.find_element_by_link_text(u"充值码查询").click()
        driver.find_element_by_link_text(u"常用查询").click()
        driver.find_element_by_link_text(u"快递员查询").click()
        driver.find_element_by_link_text(u"常用查询").click()
        driver.find_element_by_link_text(u"发送短信").click()
        driver.find_element_by_id("sms_form_tel").clear()
        driver.find_element_by_id("sms_form_tel").send_keys("18701524517")
        driver.find_element_by_id("sms_form_sms").clear()
        driver.find_element_by_id("sms_form_sms").send_keys("helloexdaix")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"常用查询").click()
        driver.find_element_by_link_text(u"手机验证码查询").click()
        driver.find_element_by_id("mobile").clear()
        driver.find_element_by_id("mobile").send_keys("187")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"订单评价").click()
        driver.find_element_by_link_text(u"好 评").click()
        driver.find_element_by_link_text(u"中 评").click()
        driver.find_element_by_link_text(u"差 评").click()
        driver.find_element_by_link_text(u"中 评").click()
        driver.find_element_by_link_text(u"好 评").click()
        driver.find_element_by_id("popover_27181").click()
        driver.find_element_by_id("note").clear()
        driver.find_element_by_id("note").send_keys("www")
        driver.find_element_by_name("commit").click()
        driver.find_element_by_link_text(u"中 评").click()
        driver.find_element_by_id("popover_27182").click()
        driver.find_element_by_id("note").clear()
        driver.find_element_by_id("note").send_keys("qqq")
        driver.find_element_by_name("commit").click()
        print driver.title,"UI Testing has been completed."
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
