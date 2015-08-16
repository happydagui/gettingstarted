from unittest import TestCase
from urllib.request import urlopen
from urllib.request import Request
from urllib.parse import urlencode
import logging
logging.basicConfig(level=logging.DEBUG)

# SERVICE_URL = 'http://min4weixinapp.sinaapp.com'
SERVICE_URL = 'http://localhost:8000'

class AppTest(TestCase):

    def testCheckSignature(self):
        url = SERVICE_URL + '/?signature=9c5f1d86525dcb9300ce55f03040a8932e48d4f7&echostr=5667388023579343993&timestamp=1438566449&nonce=209415066'
        with urlopen(url) as resp:
            response = resp.read()
            logging.debug(response)
            assert response == b'5667388023579343993'

    def testTextMsg(self):
        msg = '''<xml>
            <ToUserName><![CDATA[to]]></ToUserName>
           <FromUserName><![CDATA[from]]></FromUserName>
           <CreateTime>2011</CreateTime>
           <MsgType><![CDATA[text]]></MsgType>
           <Content><![CDATA[text]]></Content>
        </xml>
        '''
        url = SERVICE_URL
        req = Request(url, data=msg.encode('utf-8'), headers={'Content-Type':'text/xml'})

        with urlopen(req) as response:
            logging.debug(response.read())

    def testNewsMsg(self):
        msg = '''<xml>
            <ToUserName><![CDATA[to]]></ToUserName>
           <FromUserName><![CDATA[from]]></FromUserName>
           <CreateTime>2011</CreateTime>
           <MsgType><![CDATA[text]]></MsgType>
           <Content><![CDATA[news]]></Content>
        </xml>
        '''
        url = SERVICE_URL
        req = Request(url, data=msg.encode('utf-8'), headers={'Content-Type':'text/xml'})

        with urlopen(req) as response:
            logging.debug(response.read())
