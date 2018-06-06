__author__ = 'chenqingsen'
import configparser

class ConfigFile():
    #configFilePath="/config.ini"

    #def __init__(self,filepath):
    #   self.configFilePath =filepath

    #初始配置文件
    def init_config(self,filepath):
        self.__cfgPath =filepath

        config = configparser.ConfigParser()
        config.read(self.__cfgPath)
        self.__config = config

    def get_config(self,section,option):
        if not self.__config:
            print("Error:the config was not inited")
            return None

        if not self.__config.has_section(section):
            print("Error:the section ["+section+"] not exist")
            return None

        if not self.__config.has_option(section,option):
            print("Error:the section ["+section+"],option ["+option+"] not exist")
            return None

        return self.__config.get(section,option)