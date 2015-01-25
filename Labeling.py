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
import datetime
import cookielib
import string
import re
import time
import json

# set parameter
old = '100001'
itemType = 'clothes'
totalNumber = 20000
startNumber = 100001
#登录的主页面
targetURL = r"http://image.baidu.com/i?objurl=http%3A%2F%2Fholdonyb.github.io%2Fbigdatacontest%2Fclothes_image%2F"+itemType+r"_100001.jpg&rainbow=1&filename=&rt=0&rn=10&ftn=searchpcstu&ct=1&stt=0&tn=shituresultpc"

headers ={"User-agent":"Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36",
          "Host":"image.baidu.com",
          "Referer":"image.baidu.com"}
keyword = []
f=codecs.open('keyword'+str(totalNumber)+'.txt','w','utf-8');
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
# ans = json.loads(responsedata.decode('utf8'))
# captchaID = ans['retval']
#
# #####################################################
# #获取验证码，并将其存为一个图片
# requrl2= "http://www.gewara.com/captcha.xhtml?captchaId="+captchaID+ "&r=%d"  %rtime()
# print requrl2
# reqGetCaptcha= urllib2.Request(requrl2,headers=headers)
# response2 = urllib2.urlopen(reqGetCaptcha)
# imgdata = response2.read()
# captchaName ='v.png'
# imgfile = open(captchaName, "wb")
# imgfile.write(imgdata)
# imgfile.close()
# t = ThreadClass()
# t.start()
# captcha=raw_input('Captcha:')
# ############################################################
# #构造Post数据，是从抓的包里分析得出的。
# postData = {'TARGETURL' : '',
#             'RememberMe' : 'Y',  #特有数据，不同网站可能不同
#             'j_username' : username,#你的用户名
#             'j_password' : password, #你的密码，密码可能是明文传输也可能是密文，如果是密文需要调用相应的加密算法加密
#             'captchaId' : captchaID,   #特有数据，不同网站可能不同
#             'captcha':captcha
#             }
# postData = dict(postData)
# #需要给Post数据编码
# postData = urllib.urlencode(postData)
#
# ############################################
# #通过urllib2提供的request方法来向指定Url发送我们构造的数据，并完成登录过程
# request = urllib2.Request(postURL, postData, headers)
# # print request
# response = opener.open(request)
# trueurl = response.geturl()
# text = response.read()
