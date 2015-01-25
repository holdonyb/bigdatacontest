#!/usr/bin/python
# -*- coding: utf-8 -*-
__author__ = 'holdo_000'

# import HTMLParser
# import urlparse
# import httplib
# import httplib2
import urllib
import urllib2
import codecs
#import datetime
#import cookielib
# string
#import re
import time
#import json

# set parameter
old = 'whatever'
itemType = 'clothes'
totalNumber = 10
startNumber = 100300
#登录的主页面
targetURL = r"http://image.baidu.com/i?objurl=http%3A%2F%2Fholdonyb.github.io%2Fbigdatacontest%2Fclothes_image%2F"+itemType+r"_"+old+r".jpg&rainbow=1&filename=&rt=0&rn=10&ftn=searchpcstu&ct=1&stt=0&tn=shituresultpc"

headers ={"User-agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
          "Host":"image.baidu.com",
          "Referer":"image.baidu.com"}
keyword = []
f=codecs.open('keyword_'+itemType+'_'+str(startNumber)+'_'+str(startNumber+totalNumber)+'.txt','w','utf-8');
start = time.clock()
for i in range(0,totalNumber):
    print i
    reqGetCaptchaID = urllib2.Request(targetURL.replace(old,str(i+startNumber)),headers=headers)
    response1= urllib2.urlopen(reqGetCaptchaID)
    try:
        keyword.append(urllib.unquote([x[8:] for x in response1.geturl().split('?',1)[1].split('&') if x.split('=')[0]=='keyword'][0]).decode('utf-8'))
    except:
        keyword.append(u'unknow')
    print keyword[i]
    f.write(unicode(i+startNumber)+u'\t'+keyword[i]+u'\n')
f.close()
end = time.clock()
print end - start
