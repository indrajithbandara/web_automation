# -*- coding: utf-8 -*-
#encoding:utf-8 
'''
Created on 2015年7月20日
http://selenium-python.readthedocs.org/en/latest/api.html#module-selenium.webdriver.common.action_chains
@author: edaixicuijun
'''
import logging
import unittest, time, re 
from uiwuliu.wuliu_testsuit import *
from uiops.ops_testsuit import *
from uikefu.kefu_testsuit import *
from uicaiwu.caiwu_testsuit import *

if __name__ == '__main__':  
    
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime
    
    
    logging.basicConfig(level=logging.DEBUG,  
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',  
                    datefmt='%a, %d %b %Y %H:%M:%S',  
                    filename='c:\\edaixi_testdata\\'+currenttime+'-edaixi-test.log',  
                    filemode='w')  
  
    #logging.debug('debug message')  
    #logging.info('info message')  
    #logging.warning('warning message')  
    #logging.error('error message')  
    #logging.critical('critical message')
    
    start_currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    logging.info('info message start_currenttime'+start_currenttime)  

    logging.debug("starting excute uiops all testcases...")
    test_ops_suite()
    logging.debug("completed excute uiops all testcases...")
    
    logging.debug("starting excute uikefu all testcases...")
    test_kefu_suite()
    logging.debug("completed excute uikefu all testcases...")
    
    logging.debug("starting excute uicaiwu all testcases...")
    test_caiwu_suite()
    logging.debug("completed excute uicaiwu all testcases...")
    
    logging.debug("starting excute uicaiwu all testcases...")
    test_wuliu_suite()
    logging.debug("completed excute uiwuliu all testcases...")
    
    
    end_currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print end_currenttime
    spent_times=end_currenttime-start_currenttime
    logging.debug("All testcase spent time is " +spent_times)
    #print "All testcase spent time is " +spent_times

    