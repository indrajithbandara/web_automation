# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import time, MySQLdb, sys

class WuliuJiagongdianrukuQianshou(unittest.TestCase):
    

    try:
        file=open('C:/edaixi_testdata/userdata_wuliu.txt','r')
    except IOError:
        print "The file don't exsit,please check it."
        exit()
    for line in file.readlines():
        lineone=line.split()
        global WULIU_URL,USER_NAME,PASS_WORD
        WULIU_URL = lineone[0]
        USER_NAME = lineone[1]
        PASS_WORD = lineone[2]
        
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)

        self.base_url =WULIU_URL
        #self.base_url = "http://wuliu03.edaixi.cn/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_wuliu_jiagongdianruku_qianshou(self):
        driver = self.driver
        
        driver.get(self.base_url + "/")
        driver.find_element_by_link_text(u"登录").click()
        driver.find_element_by_id("username").clear()
        driver.find_element_by_id("username").send_keys(USER_NAME)
        driver.find_element_by_id("password").clear()
        driver.find_element_by_id("password").send_keys(PASS_WORD)
        driver.find_element_by_id("login-submit").click()
        time.sleep(2)
        driver.find_element_by_link_text(u"加工店出入库管理").click()
        time.sleep(1)
        driver.find_element_by_link_text(u"入库签收").click()
        time.sleep(1)
        #54.223.190.242
        conn=MySQLdb.connect(host="54.223.190.242",user="testuser",passwd="testedaixi",db="rongchain04",charset="utf8")    
        cursor = conn.cursor()
        
        n = cursor.execute("SELECT bagsn FROM ims_washing_order WHERE status_delivery=1 AND bagsn IS NOT NULL order by id") 
        for row in cursor.fetchall():
            for rowbagsn in row:      
                print "===rowbagsn is ",rowbagsn  
        print rowbagsn
        
        driver.find_element_by_id("bagsn").clear()
        driver.find_element_by_id("bagsn").send_keys(rowbagsn)
        
        n = cursor.execute("SELECT bagsn FROM ims_washing_order WHERE status_delivery=1 AND bagsn IS NOT NULL")      
        
        listbagsn =[]
        for i in xrange(cursor.rowcount):
             row= cursor.fetchone()
             rowstr =''.join(row)
             listbagsn.append(rowstr)
        print listbagsn

        if rowbagsn in listbagsn:
            driver.find_element_by_name("commit").click()
            print driver.title           
        else:
            raise ValueError("This record is exsit in datatbase,please select other one.!")
        
        cursor.close()
        conn.close()
        
    
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
        file.close()
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)
        

if __name__ == "__main__":
    unittest.main()
