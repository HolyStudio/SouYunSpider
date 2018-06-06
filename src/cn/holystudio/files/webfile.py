__author__ = 'chenqingsen'

import urllib.request
import urllib.error
import re


class WebFile():

    def load_data(self,url,encode='UTF-8'):
        """
        加载html内容
        :param url: 地址
        :return:
        """
        if url==None or url=="":
            return

        self.__url      = url
        self.__encode   = encode
        self.__content  = None
        try:
            dataReader = urllib.request.urlopen(url)
            data =dataReader.read()
            self.__content = data
        except urllib.error.HTTPError as e:
            print("HTTPError:",e.code)

        except urllib.error.URLError as e:
            print("URLError:",e.reason)

        #finally:
        #    print("ok:")



    def get_data_html(self):
        """
        获取html内容
        :param encode:
        :return:
        """
        if not self.__content:
            return None

        if not self.__encode or self.__encode==None or self.__encode=="" :
            return self.__content
        else:
            return self.__content.decode(self.__encode)

    def get_data_no_html(self):
        """
        :param regstr:
        :param encode:
        :return:
        """
        content = self.get_data_html();
        #TODO
        return content

    def get_data(self,pattern):
        """
        通过正则表达式获取指定内容[findall]
        :param pattern:
        :return:
        """
        try:
            content = self.get_data_html()
            #re.(pattern,content,re.I)
            content = re.findall(pattern,content,re.I)
        except re.error as e:
            content =""
            print(pattern,e.msg)

        return content








