import time
 
print time.time()
import urllib2
 
response = urllib2.urlopen('http://www.cnseay.com/') 
 
print response.getcode() 
a=response.read() 
response.close()
 
 
print time.time()
import httplib   
conn = httplib.HTTPConnection("www.cnseay.com")   
conn.request('get', '/')
 
res = conn.getresponse()   
 
print res.status   
b=res.read()
conn.close()   
print time.time()