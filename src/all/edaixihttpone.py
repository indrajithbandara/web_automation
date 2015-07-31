#!/usr/bin/env python
#coding=utf8
 
import httplib
 
httpClient = None
 
try:
    httpClient = httplib.HTTPConnection('open13.edaixi.cn', 81, timeout=30)
    httpClient.request('GET', '/client/v1/order_delivery_status_list')
 
    #response是HTTPResponse对象
    response = httpClient.getresponse()
    print response.status
    print response.reason
    print response.read()
except Exception, e:
    print e
finally:
    if httpClient:
        httpClient.close()