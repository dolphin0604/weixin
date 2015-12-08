__author__ = 'wangnan'
# coding: UTF-8
import hashlib

from src.commen.Config import Config
from src.commen.Log import Log
import web
import simplejson as json
import ast

class Login():

    def __init__(self):
        self.config = Config()
        self.log = Log()

    def login(self):
        self.TOKEN = ""
        self.TOKEN = self.config.get_key_value("weixin", "token")
        print self.TOKEN
        data = web.input()
        signature = data.signature
        timestamp = data.timestamp
        nonce = data.nonce
        echostr = data.echostr
        list = [self.TOKEN, timestamp,nonce]
        list.sort()
        sha1 = hashlib.sha1()
        map(sha1.update, list)
        hashcode = sha1.hexdigest()
        #sha1加密算法

        #如果是来自微信的请求，则回复echostr
        if hashcode == signature:
            return echostr


if __name__ == '__main__':
    Login().login()
    print "abc"