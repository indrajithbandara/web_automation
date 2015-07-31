# -*- coding: utf-8 -*-
#encoding:utf-8 
import time,os,re
import ConfigParser
import socket
import datetime
import time

'''
Created on 2015年7月22日
http://selenium-python.readthedocs.org/en/latest/api.html#module-selenium.webdriver.common.action_chains
@author: edaixicuijun
'''

time.strftime('%Y%m%d')



print time.strftime('%Y-%m-%d %H:%M:%S')
file=open('C:/edaixi_testdata/userinterface_data.txt','r')
dictobj={}

for line in file:
    key,value=line.split(",")
    dictobj[key]=value
#print dictobj
print dictobj["hearurl"].strip('\n')+dictobj["contenturl"]
print dictobj["contenturl"]
print dictobj["contenturl"]

file.close()




'''
cf = ConfigParser.ConfigParser()
cf.read("config.ini")

s = cf.sections()
#print 'section:', s
o = cf.options("db")
#print 'options:', o

v = cf.items("db")
#print 'db:', v
db_host = cf.get("db", "db_host")
db_port = cf.get("db", "db_port")
db_user = cf.get("db", "db_user")
db_pass = cf.get("db", "db_pass")
#print "db_host:", db_host
#print "db_port:", db_port
#print "db_user:", db_user
#print "db_pass:", db_pass
#cf.set("db", "db_pass", "zhang3")
#cf.write(open("test.conf", "w"))
 
cf.add_section('liuqing')
cf.set('liuqing', 'int', '15')
cf.set('liuqing', 'bool', 'true')
cf.set('liuqing', 'float', '3.1415')
cf.set('liuqing', 'baz', 'fun')
cf.set('liuqing', 'bar', 'Python')
cf.set('liuqing', 'foo', '%(bar)s is %(baz)s!')
cf.write(open("test.conf", "w"))

cf.remove_option('liuqing', 'int')
cf.remove_section('liuqing')
cf.write(open("test.conf", "w"))
'''



myname = socket.getfqdn(socket.gethostname())
myaddr = socket.gethostbyname(myname)
print myaddr