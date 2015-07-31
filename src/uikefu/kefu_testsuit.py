# -*- coding: utf-8 -*-
#encoding:utf-8 
import unittest, time, re 
import HTMLTestRunner
from kefu_dingdanpingjia import *
from kefu_fankuizongliebiao import *
from kefu_usallyqueryfunction import *
from kefu_tagmanagement import *
from kefu_changyonghuifu import *
from kefu_dingdanliebiao import *

from kefu_myuserfeedback import *
from kefu_myfeedback_nobackcustomer import *
from kefu_myfeedback_myprocessingcustomer import *
from kefu_myfeedback_filteredcustomer import *
from kefu_myfeedback_answeredcustomer import *
from kefu_myfeedback_allcustomer import *

if __name__ == '__main__':  
    suite = unittest.TestSuite()  
    #suite.addTest(MyTest('test_method_a'))  
    #suite.addTest(MyTest('test_method_b'))  
    suite.addTest(KefuChangyonghuifu('test_kefu_changyonghuifu'))
    suite.addTest(KefuDingdanliebiao('test_kefu_dingdanliebiao'))
    suite.addTest(KefuDingdanpingjia('test_kefu_dingdanpingjia'))
    suite.addTest(KefuFankuizongliebiao('test_kefu_fankuizongliebiao'))
    
    suite.addTest(KefuUsallyqueryfunction('test_kefu_usallyqueryfunction')) 
    suite.addTest(KefuTagmanagement('test_kefu_tagmanagement')) 
    #suite.addTest(CaiwuShitikaQuery('test_caiwu_shitika_query'))
    
    suite.addTest(KefuMyuserfeedback('test_kefu_myuserfeedback'))
    suite.addTest(KefuMyfeedbackNobackcustomer('test_kefu_myfeedback_nobackcustomer'))
    suite.addTest(KefuMyfeedbackMyprocessingcustomer('test_kefu_myfeedback_myprocessingcustomer'))
    suite.addTest(KefuMyfeedbackFilteredcustomer('test_kefu_myfeedback_filteredcustomer'))
    suite.addTest(KefuMyfeedbackAnsweredcustomer('test_kefu_myfeedback_answeredcustomer'))
    suite.addTest(KefuMyfeedbackAllcustomer('test_kefu_myfeedback_allcustomer'))
        
    #outfile=open("c://edaixi_testdata//report.html",'wb')
    #filename = 'G:\\seleniums\\result.html'
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime
    #fp = file("/usr/edaixi_report/"+currenttime+"caiwu_test_report.html", 'wb')
    fp = file("c:\\edaixi_testdata\\"+currenttime+"kefu_test_report.html", 'wb')
    #fp = file("c:\\edaixi_testdata\\20150717caiwu_test_report.html", 'wb')
    
    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="edaixi uikefu testing result",description="201507 luke")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    htmlRunner.run(suite)
    fp.close()
    
    #unittest.TextTestRunner(verbosity=2).run(suite) 
    
def test_kefu_suite():
    suite = unittest.TestSuite()  

    suite.addTest(KefuChangyonghuifu('test_kefu_changyonghuifu'))
    suite.addTest(KefuDingdanliebiao('test_kefu_dingdanliebiao'))
    suite.addTest(KefuDingdanpingjia('test_kefu_dingdanpingjia'))
    suite.addTest(KefuFankuizongliebiao('test_kefu_fankuizongliebiao'))
    
    suite.addTest(KefuUsallyqueryfunction('test_kefu_usallyqueryfunction')) 
    suite.addTest(KefuTagmanagement('test_kefu_tagmanagement')) 
    #suite.addTest(CaiwuShitikaQuery('test_caiwu_shitika_query'))
    
    suite.addTest(KefuMyuserfeedback('test_kefu_myuserfeedback'))
    suite.addTest(KefuMyfeedbackNobackcustomer('test_kefu_myfeedback_nobackcustomer'))
    suite.addTest(KefuMyfeedbackMyprocessingcustomer('test_kefu_myfeedback_myprocessingcustomer'))
    suite.addTest(KefuMyfeedbackFilteredcustomer('test_kefu_myfeedback_filteredcustomer'))
    suite.addTest(KefuMyfeedbackAnsweredcustomer('test_kefu_myfeedback_answeredcustomer'))
    suite.addTest(KefuMyfeedbackAllcustomer('test_kefu_myfeedback_allcustomer'))
        
    #outfile=open("c://edaixi_testdata//report.html",'wb')
    #filename = 'G:\\seleniums\\result.html'
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime
    #fp = file("/usr/edaixi_report/"+currenttime+"caiwu_test_report.html", 'wb')
    fp = file("c:\\edaixi_testdata\\"+currenttime+"kefu_test_report.html", 'wb')
    #fp = file("c:\\edaixi_testdata\\20150717caiwu_test_report.html", 'wb')
    
    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="edaixi uikefu testing result",description="201507 luke")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    htmlRunner.run(suite)
    fp.close()
  
    