import urllib
import urllib2
##
##http://open13.edaixi.cn:81/client/v1/order_delivery_status_list


url = "http://open13.edaixi.cn:81/client/v1/order_delivery_status_list"

req = urllib2.Request(url)
print req

res_data = urllib2.urlopen(req)
res = res_data.read()
print res