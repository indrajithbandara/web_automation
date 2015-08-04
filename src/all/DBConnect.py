# coding=utf-8
import MySQLdb
 
#查询数量
def Count(cur):
   count=cur.execute('select * from Student')
   print 'there has %s rows record' % count
    
#插入
def Insert(cur):
   sql = "insert into Student(ID,Name,Age,Sex)values(%s,%s,%s,%s)"
   param = (2,'xiaoming',24,'boy')
   cur.execute(sql,param)
 
#查询 
def  Select(cur):  
   n = cur.execute("select * from Student")    
   print "------"
   for row in cur.fetchall():    
      for r in row:    
         print r
      print "------"   
#更新
def Update(cur):
   sql = "update Student set Name = %s where ID = 2"  
   param = ("xiaoxue")    
   count = cur.execute(sql,param)
 
#删除
def Delete(cur):    
   sql = "delete from Student where Name = %s"  
   param =("xiaoxue")    
   n = cur.execute(sql,param)   
  
try:
   conn=MySQLdb.connect(host='localhost',user='root',passwd='123456',db='python',port=3306)
   cur=conn.cursor()
   #数量
   Count(cur)
   #查询
   Select(cur)
   #插入
   Insert(cur)
   print "插入之后"
   #查询
   Select(cur)
   #更新
   Update(cur)
   print "更新之后"
   #查询
   Select(cur)
   #删除
   Delete(cur)
   print "删除之后"
   #查询
   Select(cur)
    
   cur.close()
   conn.close()
    
except MySQLdb.Error,e:
   print "Mysql Error %d: %s" % (e.args[0], e.args[1])