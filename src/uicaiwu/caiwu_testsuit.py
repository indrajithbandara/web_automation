# -*- coding: utf-8 -*-
#encoding:utf-8 
import unittest, time, re 
import HTMLTestRunner

from caiwu_huiyuancardquery import *

from caiwu_shitika import *
from caiwu_shitika_modify import *
from caiwu_shitika_query import *
from caiwu_shitika_shengchenka import *
from caiwu_shitika_chongzhi import *

from caiwu_userquery import *

from caiwu_youhuiquangroup import *
from caiwu_youhuiquanlist import *
from caiwu_youhuiquanlist_add import *
from caiwu_youhuiquanlist_export import *
from caiwu_youhuiquanlist_modify import *

if __name__ == '__main__':  
    suite = unittest.TestSuite()  
    #suite.addTest(MyTest('test_method_a'))  
    #suite.addTest(MyTest('test_method_b'))  
    suite.addTest(CaiwuHuiyuancardquery('test_caiwu_huiyuancardquery'))
    suite.addTest(CaiwuUserquery('test_caiwu_userquery'))
    
    suite.addTest(CaiwuShitika('test_caiwu_shitika'))
    suite.addTest(CaiwuShitikaShengchenka('test_caiwu_shitika_shengchenka')) 
    suite.addTest(CaiwuShitikaQuery('test_caiwu_shitika_query'))
    suite.addTest(CaiwuShitikaModify('test_caiwu_shitika_modify'))
    suite.addTest(CaiwuShitikaChongzhi('test_caiwu_shitika_chongzhi'))
    
    suite.addTest(CaiwuYouhuiquangroup('test_caiwu_youhuiquangroup'))
    suite.addTest(CaiwuYouhuiquanlist('test_caiwu_youhuiquanlist'))
    suite.addTest(CaiwuYouhuiquanlistAdd('test_caiwu_youhuiquanlist_add'))
    suite.addTest(CaiwuYouhuiquanlistExport('test_caiwu_youhuiquanlist_export'))
    suite.addTest(CaiwuYouhuiquanlistModify('test_caiwu_youhuiquanlist_modify'))
    

    #outfile=open("c://edaixi_testdata//report.html",'wb')
    #filename = 'G:\\seleniums\\result.html'
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime
    #fp = file("/usr/edaixi_report/"+currenttime+"caiwu_test_report.html", 'wb')
    fp = file("c:\\edaixi_testdata\\"+currenttime+"caiwu_test_report.html", 'wb')
    #fp = file("c:\\edaixi_testdata\\20150717caiwu_test_report.html", 'wb')

    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="edaixi uicaiwu testing result",description="201507 luke")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    htmlRunner.run(suite)
    fp.close()
    
    #unittest.TextTestRunner(verbosity=2).run(suite) 
    
    
def test_caiwu_suite():
    suite= unittest.TestSuite()  

    suite.addTest(CaiwuHuiyuancardquery('test_caiwu_huiyuancardquery'))
    suite.addTest(CaiwuUserquery('test_caiwu_userquery'))
    
    suite.addTest(CaiwuShitika('test_caiwu_shitika'))
    suite.addTest(CaiwuShitikaShengchenka('test_caiwu_shitika_shengchenka')) 
    suite.addTest(CaiwuShitikaQuery('test_caiwu_shitika_query'))
    suite.addTest(CaiwuShitikaModify('test_caiwu_shitika_modify'))
    suite.addTest(CaiwuShitikaChongzhi('test_caiwu_shitika_chongzhi'))
    
    suite.addTest(CaiwuYouhuiquangroup('test_caiwu_youhuiquangroup'))
    suite.addTest(CaiwuYouhuiquanlist('test_caiwu_youhuiquanlist'))
    suite.addTest(CaiwuYouhuiquanlistAdd('test_caiwu_youhuiquanlist_add'))
    suite.addTest(CaiwuYouhuiquanlistExport('test_caiwu_youhuiquanlist_export'))
    suite.addTest(CaiwuYouhuiquanlistModify('test_caiwu_youhuiquanlist_modify'))
    

    #outfile=open("c://edaixi_testdata//report.html",'wb')
    #filename = 'G:\\seleniums\\result.html'
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime
    #fp = file("/usr/edaixi_report/"+currenttime+"caiwu_test_report.html", 'wb')
    fp = file("c:\\edaixi_testdata\\"+currenttime+"caiwu_test_report.html", 'wb')
    #fp = file("c:\\edaixi_testdata\\20150717caiwu_test_report.html", 'wb')

    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="edaixi uicaiwu testing result",description="201507 luke")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    htmlRunner.run(suite)
    fp.close()
 
    