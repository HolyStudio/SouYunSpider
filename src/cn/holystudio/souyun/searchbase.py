__author__ = 'chenqingsen'

from src.cn.holystudio.files import configfile
from src.cn.holystudio.files import webfile

class SearchBase():

    def __init__(self,dataurl):
        self.web = webfile.WebFile()
        self.dataurl = dataurl
        #self.web.load_data(dataurl)
        pass

    def start(self):
        self.web.load_data(self.dataurl)

        pass

    def get_datalist(self,pattern):
        '''
        获取通过正则表达式匹配到的数据集
        :return:
        '''
        datalist = self.web.get_data(pattern)
        return datalist
