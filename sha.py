# -*- coding:utf-8 -*-

import httplib

httplib.HTTPConnection.debuglevel = 1
'''
200正常状态码不会有跳转 也就不会有location
conn = httplib.HTTPConnection("tu.duowan.com") #这里是host
conn.request('GET', '/m/meinv/index.html')#上面是分支 注意是GET
'''
# 访问跳转的302页面就可以在headers中找到location
conn = httplib.HTTPConnection("dl.acm.org")  # 这里是host
conn.request('GET', '/authorize.cfm?key=N12211')  # 上面是分支 注意是GET
for item in conn.getresponse().getheaders():
    if item[0] == 'location':
        print item[1]
conn.close()