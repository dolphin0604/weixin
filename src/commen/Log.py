## -*-coding:utf-8-*-
__author__ = 'wangnan'
import logging
import os
import time

# LOG_FILE=os.path.abspath(os.path.dirname("../../resource/test.log"))+"\\test.log"
#LOG_FILE="../../resource/test.log"


class Log():
    def __init__(self, **arg):
        self.con = arg.get("console", "log")
        self.levelStr = arg.get("levelStr", "debug")
        self.logFormatStr = arg.get("logFormatStr", '''%(asctime)s\t%(levelname)s\t%(message)s''')
        ''' set  log level '''
        self.levelEnum = {"debug": logging.DEBUG,
                          "info": logging.INFO,
                          "warn": logging.WARN,
                          "error": logging.ERROR}

        self.logLevel = self.levelEnum.get(self.levelStr)

        ''' get system time to create log '''
        systemTime = time.strftime('%Y%m%d', time.localtime(time.time()))
        LOG_FILE = os.path.abspath("../../resource/" + str(systemTime) + ".log")
        ''' create a Logging '''
        if self.con == "console":
            self.console = logging.StreamHandler()
            self.console.setLevel(self.logLevel)
            self.formatter = logging.Formatter(self.logFormatStr)
            self.console.setFormatter(self.formatter)
            logging.getLogger('').addHandler(self.console)
        logging.basicConfig(filename=LOG_FILE, level=self.logLevel, format=self.logFormatStr,
                            datefmt='%Y-%m-%d %H:%M:%S')


    def logging_debug(self, debugStr):
        logging.debug(debugStr)

    def logging_info(self, infoStr):
        logging.info(infoStr)

    def logging_warning(self, warningStr):
        logging.warning(warningStr)

    def logging_error(self, errorStr):
        logging.error(errorStr)

#     def logging_consol(self,consolStr):



if __name__ == '__main__':
#     log=Log()
# #     print LOG_FILE
#     log.logging_info("test info")
#     log.logging_debug("test debug")
    log1 = Log(console="log")
    log1.logging_debug("test debug")
    log1.logging_warning("test warning")
    log1.logging_error("test error")