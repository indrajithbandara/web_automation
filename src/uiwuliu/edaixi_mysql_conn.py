#-*- coding:utf-8 -*-  
#encoding:utf-8
#mysqldb      
import time, MySQLdb, sys    
import sys
import threading
import paramiko
import socket
import random
from _ast import Str
#10.66.110.220
#connect   115.159.23.93
'''
try:
    ssh = paramiko.SSHClient()
    ssh.load_system_host_keys()
    ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
    ssh.connect("115.159.23.93", port=int(52087), username="ubnutu", password="PR4haxlB4zTabT9ZsD")
    #ssh.exec_command(comm['alter_auth'])
    #ssh.exec_command(comm['exec_program'])
    
except Exception,e:
    print 'chang file auth or execute the file failed:',e
ssh.close()
    '''
#conn=MySQLdb.connect(host="54.223.190.242",user="root",passwd="wwefa232afYUY",db="wuliu03",charset="utf8")  
#conn = MySQLdb.connect(sshhost = '115.159.23.93', sshuser = 'ubuntu', sshpasswd = 'PR4haxlB4zTabT9ZsD', host = '10.66.110.220:3306', user = 'root', passwd = 'wwefa232afYUY', db = 'rongchain03')  
#conn=MySQLdb.connect(host="testdb.edaixi.cn",user="test",passwd="test",db="rongchain03",charset="utf8") 
conn=MySQLdb.connect(host="54.223.190.242",user="testuser",passwd="testedaixi",db="rongchain04",charset="utf8")   
cursor = conn.cursor()
n = cursor.execute("SELECT bagsn FROM ims_washing_order WHERE status_delivery=1")      
#MySQLdb.connect   
#cursor = conn.cursor()
#n = cursor.execute("SELECT  bagsn FROM ims_washing_order WHERE bagsn IS NOT NULL AND bagsn<>''") 
#print cursor.fetchall()
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
#for row in cursor.fetchall():
    #print row
    
    
n = cursor.execute("SELECT MAX(id) FROM ims_washing_order") 
for row in cursor.fetchall():
    for r in row:      
        print "===maxidrow is ",r  
print "maxrowdid+1 is ",str(r+1)
strmax=str(r+1)
print strmax


nup=cursor.execute("UPDATE ims_washing_order SET fanxidan_id = %s WHERE ordersn = %s",(strmax, "15062510429996"))
print nup
conn.commit()
#n = cursor.execute(cursor.execute("UPDATE ims_washing_order SET fanxidan_id = %s WHERE Id = %s",ax,"15062510429996"))      
#print n  
               
if 'E0000125599' in listbagsn:
   print "it is exsit on mysql order table."
else:
   print "it is not exsit on mysql order table"
                                    
'''                                  
for row in cursor.fetchall():
     
    for r in row:      
        print r,     
print ""  
'''
cursor.close()
conn.close()
print random.randint(0,999)+random.randint(0,999)
'''
cursor.execute("SELECT id, name FROM `table`")
for i in xrange(cursor.rowcount):
    id, name = cursor.fetchone()
    print id, name


cursor.execute("SELECT id, name FROM `table`")
result = cursor.fetchmany()
while result:
    for id, name in result:
        print id, name
    result = cursor.fetchmany()


cursor.execute("SELECT id, name FROM `table`")
for id, name in cursor.fetchall():
    print id, name
    
'''
theTuple = ('a','b','c')
if 'a' in theTuple:
    print 'a in the Tuple'
    
    
theList = ['a','b','c']
if 'a' in theList:
    print 'a in the list'

if 'd' not in theList:
    print 'd is not in the list'