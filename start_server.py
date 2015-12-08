#!/usr/bin/python
#coding = utf-8

__author__ = 'wangnan'
#from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from src.api.ConfigAuth.ConfigAuthHandler import ConfigAuthHandler
from src.api.HelloWorld.HelloWorldHandler import HelloWorldHandler
from src.api.WXMessageHandler.WXMessageHandler import WXMessageHandler
import web

urls = (
    '/configAuth', 'ConfigAuthHandler',
    '/interface', 'WXMessageHandler',
    '/helloWorld', 'HelloWorldHandler'
)

if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()