__author__ = 'chenqingsen'

from src.cn.holystudio.files import configfile
from src.cn.holystudio.files import webfile
from src.cn.holystudio.souyun import search_pingshuiyun as pingshuiyun


cfg = configfile.ConfigFile()
cfg.init_config("config.ini")
domain  = cfg.get_config("WebConfig","Domain")
yunListUrl = cfg.get_config("WebConfig","Url")


psyun = pingshuiyun.SearchPingShuiYun(yunListUrl)
psyun.start()

#yunlist = psyun.get_datalist("<a href='(QR.aspx\?ct=.*?)'>(.*?)</a>")







'''
web = webfile.WebFile()
web.load_data(yunListUrl)

yunList = web.get_data("<a href='(QR.aspx\?ct=.*?)'>(.*?)</a>")
print(len(yunList))
print(type(yunList))
index =1
for item in yunList:
    subYunListUrl = domain+"/"+item[0]
    web.load_data(subYunListUrl)

    print("key="+item[1])
    subYunList = web.get_data("<a href=\"(QR.aspx\?ct=.*?)\">(.*?)</a>")

    print(type(subYunList))
    #print(subYunList)
    #print(keyUrl)

    index=index+1
    if index>2:
        break
'''

