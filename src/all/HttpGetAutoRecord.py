#-*- coding: utf-8 -*-
 
import httplib2,xlrd,xlwt,time,json
from xlutils.copy import copy
 
def Time():
    tim=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    return tim
 
print "test begin: "+Time()
#开始时间
 
oldwb=xlrd.open_workbook(r'C:\edaixi_testdata\url.xls')
oldsh = oldwb.sheet_by_index(0)
nrows=oldsh.nrows
newwb=copy(oldwb)
newsh=newwb.get_sheet(0)
#第一次调用xlrd，xlwt
 
def GetHttpStatus(url):
    try:
        conn= httplib2.Http(disable_ssl_certificate_validation=True)
        Start=time.time()
        req=conn.request(url)
        End=time.time()
        diff= End-Start
        return req[0],diff
    except Exception as err:
        return(err,diff)
#https请求方法,请求时间
 
 
for i in range(1,nrows):
    url1=oldsh.cell_value(i,1)
    url=url1
    status=GetHttpStatus(url)[0]['status']
    reqtime=GetHttpStatus(url)[1]
    newsh.write(i,2,status)
    newsh.write(i,5,Time())
    newsh.write(i,6,reqtime)
    if reqtime < 1.0:
        newsh.write(i,7,'Normal')
    else:
        newsh.write(i,7,'Timeout')
    AC_reusult=oldsh.cell(i,2).value
    EX_reusult=oldsh.cell(i,3).value
    if AC_reusult == EX_reusult:
        newsh.write(i,4,"PASS")
    else:
        newsh.write(i,4,"FAIL")
newwb.save('C:\edaixi_testdata\url.xls')
#将复制过的数据保存在newurl.xls
 
 
print "test over: "+Time()
#结束时间
    