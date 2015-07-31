# -*- coding:gb2312 -*-
import urllib2,urllib
from urllib import urlencode


def GetUserInfo(uname,method):
    if method == 'GET':
        url = 'http://ip:port/all/GetUserInfo.php?uname='+urlencode(uname)
        result = urllib2.urlopen(url).read()
        return result
   
    if method == 'POST':
        url = 'http://ip:port/all/GetUserInfo.php'
        values = {'uname' : uname}
        data = urllib.urlencode(values)
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)
        result = response.read()
        return result
