__author__ = 'chenqingsen'



import configparser
def test():
    config =configparser.ConfigParser()
    config.read("config.ini")
    sections=config.sections()
    print("配置块：",sections)

    o=config.options("WebConfig")
    print("配置项：",o)

    v=config.items("WebConfig")
    print("内容：",v)

    #根据配置型块和配置项返回内容
    url=config.get("WebConfig","url")
    print("url:",url)
    delaycd=config.get("WebConfig","delaycd")
    print("delaycd:",delaycd)