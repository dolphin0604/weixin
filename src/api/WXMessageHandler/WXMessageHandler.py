#!/usr/bin/python
#coding=utf-8
__author__ = 'wangnan'
import web
import time
import re
import random
from xml.etree import ElementTree
from src.commen.Config import Config
filePath = "/home/web/templates"

class WXMessageHandler():
    def __init__(self):
        self.render = web.template.render(filePath)

    def POST(self):
        str_xml = web.data()
        xmlElement = ElementTree.fromstring(str_xml)
        contentPre = xmlElement.find("Content").text #获得用户所输入的内容
        print contentPre
        if contentPre == u'主持人':
            comperelist = re.split(',', Config().get_key_value("sharing", "compereList"))
            comperecount = len(comperelist)
            num = random.randint(0, comperecount-1)
            content = comperelist[num]
            print content
        else:
            content = contentPre
        msgType = xmlElement.find("MsgType").text
        fromUser = xmlElement.find("FromUserName").text
        toUser = xmlElement.find("ToUserName").text
        return self.render.reply_text(fromUser, toUser, int(time.time()), msgType, content)

