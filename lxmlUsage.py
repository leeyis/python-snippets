# -*- coding: utf-8 -*-

import urllib
import urllib2
from lxml import etree as ET
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
url='http://m.xiachufang.com/search/?keyword='
data=urllib.quote('酸菜鱼')
data=urllib2.urlopen(url+data)
resp=data.read()
html=ET.HTML(resp)
rst=html.xpath('''//header[@class="name ellipsis font19 bold"]/text()''')
for i in rst:
    print i



