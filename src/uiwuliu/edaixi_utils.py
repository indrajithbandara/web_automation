#-*- coding:utf-8 -*-  
#encoding:utf-8
#mysqldb      
import time, MySQLdb, sys    
import random,datetime
import threading,thread,multiprocessing
import socket
import paramiko


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
#ssh.connect("115.159.23.93", port=int(52087), username="ubnutu", password="PR4haxlB4zTabT9ZsD")
ssh.connect("115.159.231.215", port=int(52087), username="ubnutu", password="PR4haxlB4zTabT9ZsD")
stdin, stdout, stderr = ssh.exec_command("mysql -utest -ptest -Dmysql -e 'SELECT bagsn FROM ims_washing_order WHERE status_delivery=1'")
print stdout.readlines()
ssh.close()


#10.66.110.220
#connect   115.159.23.93

print "this is my utils for pythons."

conn=MySQLdb.connect(host="10.66.110.220",user="test",passwd="test",db="rongchain03",charset="utf8")   
cursor = conn.cursor()
n = cursor.execute("SELECT bagsn FROM ims_washing_order WHERE status_delivery=1")      

print n
listbagsn =[]
for i in xrange(cursor.rowcount):
    row= cursor.fetchone()
    #print row[row.find()] str(row)
    rowstr =''.join(row)
    #print rowstr
    listbagsn.append(rowstr)
    #print row
print listbagsn
print tuple(listbagsn)
