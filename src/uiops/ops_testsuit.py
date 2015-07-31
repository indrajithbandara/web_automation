# -*- coding: utf-8 -*-
#encoding:utf-8 
import unittest, time, re 
import HTMLTestRunner
import StringIO
from uiops.ops_banmianfenxiaoxiandan import *
from uiops.ops_categoryguanli import *
from uiops.ops_yunfeiguanli import *
from uiops.ops_yiwuguanli import *
from ops_yingxiao_sendyouhuiquan import *
from ops_yingxiao_sendduanxin import *

if __name__ == '__main__':  
    suite = unittest.TestSuite()  
    #suite.addTest(MyTest('test_method_a'))  
    #suite.addTest(MyTest('test_method_b'))  
   
    suite.addTest(Opsbanmianfenxiaoxiandan('test_ops_banmianfenxiaoxiandan'))
    suite.addTest(OpsCategoryguanli('test_ops_categoryguanli'))
    #suite.addTest(Ops('test_ops'))
    suite.addTest(OpsYiwuguanli('test_ops_yiwuguanli'))
    suite.addTest(OpsYunfeiguanli('test_ops_yunfeiguanli'))

    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime
    fp = file("c:\\edaixi_testdata\\"+currenttime+"ops_test_report.html", 'wb')
    #fp = file("/usr/edaixi_report/"+currenttime+"ops_test_report.html", 'wb')
    #Greante test report
    #fp = file("c:\\edaixi_testdata\\20150717ops_test_report.html", 'wb')

    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="edaixi uiops testing result",description="201507 luke")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    htmlRunner.run(suite)
    fp.close()
    
def test_ops_suite():
    suite = unittest.TestSuite()  

    suite.addTest(Opsbanmianfenxiaoxiandan('test_ops_banmianfenxiaoxiandan'))
    suite.addTest(OpsCategoryguanli('test_ops_categoryguanli'))
    #suite.addTest(Ops('test_ops'))
    suite.addTest(OpsYiwuguanli('test_ops_yiwuguanli'))
    suite.addTest(OpsYingxiaoSendyouhuiquan('test_ops_yingxiao_sendyouhuiquan'))

    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime
    fp = file("c:\\edaixi_testdata\\"+currenttime+"ops_test_report.html", 'wb')
    #fp = file("/usr/edaixi_report/"+currenttime+"ops_test_report.html", 'wb')
    #Greante test report
    #fp = file("c:\\edaixi_testdata\\20150717ops_test_report.html", 'wb')

    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="edaixi uiops testing result",description="201507 luke")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    htmlRunner.run(suite)
    fp.close()

