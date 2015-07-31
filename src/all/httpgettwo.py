import httplib

url = "http://192.168.81.16/cgi-bin/python_test/test.py?ServiceCode=aaaa"

conn = httplib.HTTPConnection("192.168.81.16")
conn.request(method="GET",url=url) 

response = conn.getresponse()
res= response.read()
print res