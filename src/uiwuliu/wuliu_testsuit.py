# -*- coding: utf-8 -*-
#encoding:utf-8 
import unittest, time, re 
import HTMLTestRunner
from wuliu_jiagongdianruku_qianshou import *
from wuliu_jiagongchangchurukuguanli import *
from wuliu_quanxianguanli import *
from wuliu_yue_fuwuzhanchaxun import *
from wuliu_yuechaxun_dingdanchaxun import *
from wuliu_xiadan_wusongshouyi import *
from wuliu_citylist_addcity import *
from wuliu_citylist_diaoduchaxun import *
from wuliu_citylist_diaodupaidan import *
from wuliu_citylist_fuwuzhandianguanli import *
from wuliu_citylist_huafenjibenquyu import *
from wuliu_citylist_huafenkuaidiquyu import *
from wuliu_citylist_huafenshechipinquyu import *
from wuliu_citylist_huafenzhongbaoquyu import *
from wuliu_citylist_jiagongdianguanli import *
from wuliu_citylist_shechipinwuliu import *
from wuliu_citylist_shouyidianguanli import *
from wuliu_citylist_xiaoeguanjiaguanli import *
from wuliu_citylist_ziyinwuliuxinxi import *
from wuliu_zhandianchurukuguanli import *


def test_wuliu_suite():
   
    suite = unittest.TestSuite()  

    suite.addTest(WuliuZhandianchurukuguanli('test_wuliu_zhandianchurukuguanli'))
    suite.addTest(WuliuJiagongdianrukuQianshou('test_wuliu_jiagongdianruku_qianshou'))
    suite.addTest(WuliuJiagongchangchurukuguanli('test_wuliu_jiagongchangchurukuguanli'))
    suite.addTest(WuliuQuanxianguanli('test_wuliu_quanxianguanli'))
    suite.addTest(WuliuXiadanWusongshouyi('test_wuliu_xiadan_wusongshouyi'))
    
    suite.addTest(WuliuFuwuzhanchaxun('test_wuliu_fuwuzhanchaxun'))
    suite.addTest(WuliuCitylistAddcity('test_wuliu_citylist_addcity'))
    suite.addTest(WuiuCitylistDiaoduchaxun('test_wuiu_citylist_diaoduchaxun'))
    suite.addTest(WuiuCityListDiaodupaidan('test_wuiu_citylist_diaodupaidan'))
    suite.addTest(WuiuCitylistFuwuzhandianguanli('test_wuiu_citylist_fuwuzhandianguanli'))
    
    suite.addTest(WuliuCitylisthuafenjibenquyu('test_wuliu_citylist_huafenjibenquyu'))
    suite.addTest(WuliuCitylisthuafenkuaidiquyu('test_wuliu_citylist_huafenkuaidiquyu'))
    suite.addTest(WuliuCitylistHuafenzhongbaoquyu1111('test_wuliu_citylist_huafenzhongbaoquyu1111'))
    suite.addTest(WuliuCitylistHuafenzhongbaoquyu('test_wuliu_citylist_huafenzhongbaoquyu'))
    suite.addTest(WuliuCitylistJiagongdianguanli('test_wuliu_citylist_jiagongdianguanli'))
    
    suite.addTest(WuiuCitylistShechipinwuliu('test_wuiu_citylist_shechipinwuliu'))
    suite.addTest(WuliuCitylistShouyidianguanli('test_wuliu_citylist_shouyidianguanli'))
    suite.addTest(WuiuCitylistXiaoeguanjiaguanli('test_wuiu_citylist_xiaoeguanjiaguanli'))
    suite.addTest(WuiuCitylistZiyinwuliuxinxi('test_wuiu_citylist_ziyinwuliuxinxi'))
    #suite.addTest(WuliuJiagongdianrukuQianshou('test_wuliu_jiagongdianruku_qianshou'))
 
    #outfile=open("c://edaixi_testdata//report.html",'wb')
    #filename = 'G:\\seleniums\\result.html'
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime
    #fp = file("/usr/edaixi_report/"+currenttime+"caiwu_test_report.html", 'wb')
    fp = file("c:\\edaixi_testdata\\"+currenttime+"wuliu_test_report.html", 'wb')
    #fp = file("c:\\edaixi_testdata\\20150717caiwu_test_report.html", 'wb')

    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="edaixi uiwuliu testing result",description="201507 luke")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    htmlRunner.run(suite)
    fp.close()


if __name__ == '__main__':  
    suite = unittest.TestSuite()  
    #suite.addTest(MyTest('test_method_a'))  
    #suite.addTest(MyTest('test_method_b'))  
   
    suite.addTest(WuliuZhandianchurukuguanli('test_wuliu_zhandianchurukuguanli'))
    suite.addTest(WuliuJiagongdianrukuQianshou('test_wuliu_jiagongdianruku_qianshou'))
    suite.addTest(WuliuJiagongchangchurukuguanli('test_wuliu_jiagongchangchurukuguanli'))
    suite.addTest(WuliuQuanxianguanli('test_wuliu_quanxianguanli'))
    suite.addTest(WuliuXiadanWusongshouyi('test_wuliu_xiadan_wusongshouyi'))
    suite.addTest(WuliuFuwuzhanchaxun('test_wuliu_fuwuzhanchaxun'))
    suite.addTest(WuliuCitylistAddcity('test_wuliu_citylist_addcity'))
    suite.addTest(WuiuCitylistDiaoduchaxun('test_wuiu_citylist_diaoduchaxun'))
    suite.addTest(WuiuCityListDiaodupaidan('test_wuiu_citylist_diaodupaidan'))
    suite.addTest(WuiuCitylistFuwuzhandianguanli('test_wuiu_citylist_fuwuzhandianguanli'))
    suite.addTest(WuliuCitylisthuafenjibenquyu('test_wuliu_citylist_huafenjibenquyu'))
    suite.addTest(WuliuCitylisthuafenkuaidiquyu('test_wuliu_citylist_huafenkuaidiquyu'))
    suite.addTest(WuliuCitylistHuafenzhongbaoquyu1111('test_wuliu_citylist_huafenzhongbaoquyu1111'))
    suite.addTest(WuliuCitylistHuafenzhongbaoquyu('test_wuliu_citylist_huafenzhongbaoquyu'))
    suite.addTest(WuliuCitylistJiagongdianguanli('test_wuliu_citylist_jiagongdianguanli'))
    suite.addTest(WuiuCitylistShechipinwuliu('test_wuiu_citylist_shechipinwuliu'))
    suite.addTest(WuliuCitylistShouyidianguanli('test_wuliu_citylist_shouyidianguanli'))
    suite.addTest(WuiuCitylistXiaoeguanjiaguanli('test_wuiu_citylist_xiaoeguanjiaguanli'))
    suite.addTest(WuiuCitylistZiyinwuliuxinxi('test_wuiu_citylist_ziyinwuliuxinxi'))
    #suite.addTest(WuliuJiagongdianrukuQianshou('test_wuliu_jiagongdianruku_qianshou'))
 
    #outfile=open("c://edaixi_testdata//report.html",'wb')
    #filename = 'G:\\seleniums\\result.html'
    currenttime=time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())
    print currenttime
    #fp = file("/usr/edaixi_report/"+currenttime+"caiwu_test_report.html", 'wb')
    fp = file("c:\\edaixi_testdata\\"+currenttime+"wuliu_test_report.html", 'wb')
    #fp = file("c:\\edaixi_testdata\\20150717caiwu_test_report.html", 'wb')

    htmlRunner= HTMLTestRunner.HTMLTestRunner(stream=fp,title="edaixi uiwuliu testing result",description="201507 luke")
    #suite =  unittest.TestLoader().loadTestsFromTestCase(MyTest)  
    htmlRunner.run(suite)
    fp.close()
# unittest.TextTestRunner(verbosity=2).run(suite) 