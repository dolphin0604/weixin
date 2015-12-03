from src.commen.Log import Log

__author__ = 'wangnan'
## -*-coding:utf-8-*-
import ConfigParser

filePath = "../../etc/config"

class Config():
    def __init__(self):
        self.cf = ConfigParser.ConfigParser()
        self.log = Log()
        # print filePath
        try:
            self.cf.read(filePath)
            self.log.logging_info("find file")
        except Exception, e:
            self.log.logging_error(e)

    def get_key_value(self, session, key, **arg):
        self.item = ""
        arg = arg.get("item", self.item)
        try:
            if arg == "int":
                value = self.cf.getint(session, key)
            elif arg == "float":
                value = self.cf.getfloat(session, key)
            elif arg == "boolean":
                value = self.cf.getboolean(session, key)
            else:
                value = self.cf.get(session, key)

            self.log.logging_info("find session and key")
            return value
        except Exception, e:
            self.log.logging_error(e)
            print e

if __name__=='__main__':

    configFile=Config()

    print configFile.get_key_value("vv","port")