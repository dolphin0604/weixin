from Login import Login

__author__ = 'wangnan'
#!/usr/bin/python
#coding=utf-8

class ConfigAuthHandler():
    def GET(self):
        checkSignResult = Login().login()
        return checkSignResult