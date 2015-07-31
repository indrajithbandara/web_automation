import urllib
import urllib2

test_data = {'ServiceCode':'aaaa','b':'bbbbb'}
test_data_urlencode = urllib.urlencode(test_data)

requrl = "http://192.168.81.16/cgi-bin/python_test/test.py"

req = urllib2.Request(url = requrl,data =test_data_urlencode)
print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print res