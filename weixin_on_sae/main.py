# encoding: utf-8
from django.conf import settings
import logging
import os

logger = logging.getLogger(__name__)
BASE_DIR = os.path.dirname(__name__)

if not settings.configured:  # prevent when starting from wsgi
    settings.configure(
        DEBUG=True,
        SECRET_KEY='thisisthesecret',
        ROOT_URLCONF='main',
        TEMPLATE_DIRS=(os.path.join(BASE_DIR, 'templates'),),
        LOGGING={
            'version': 1,
            'disable_existing_loggers': False,
            'handlers': {
                'console': {
                    'class': 'logging.StreamHandler',
                },
            },
            'loggers': {
                'django': {
                    'handlers': ['console'],
                    'level': 'DEBUG',
                },
            },
        }
    )


def checkSignature(request):
    '''
    signature=9c5f1d86525dcb9300ce55f03040a8932e48d4f7&echostr=5667388023579343993&timestamp=1438566449&nonce=209415066 500 0.413 0.413 53112
    :param request:
    :return:
    '''
    signature = request.GET.get('signature', '')
    timestamp = request.GET.get('timestamp', '')
    nonce = request.GET.get('nonce', '')
    echostr = request.GET.get('echostr', '')

    token = 'your token'

    l = [token, timestamp, nonce]
    l.sort()
    s = ''.join(l)
    import hashlib
    ret = hashlib.sha1(s.encode('utf-8')).hexdigest()
    if ret == signature:
        return echostr
    else:
        logger.exception('WRONG Sig#' + signature)
        raise Exception('WRONG Sig#' + signature)


from django.views.decorators.csrf import csrf_exempt

from django.http import HttpResponse
from django.shortcuts import render_to_response, render

@csrf_exempt
def index(request):
    print(request.body)

    if request.method == 'GET':
        return HttpResponse(checkSignature(request))

    from xml.etree import ElementTree
    from django.utils.encoding import smart_str
    xmlstr = smart_str(request.body)
    logger.error(xmlstr)
    xml = ElementTree.fromstring(xmlstr)
    ToUserName = xml.find('ToUserName').text
    FromUserName = xml.find('FromUserName').text
    CreateTime = xml.find('CreateTime').text
    MsgType = xml.find('MsgType').text
    Content = xml.find('Content').text
    # MsgId = xml.find('MsgId').text

    if MsgType == 'event':
        event = xml.find('Event').text
        if event == 'Subscribe':
            return ''
    reply_xml = ''
    Content = Content.lower()
    if Content == 'text':
        # msg = '<h3>Hello, this is a simple message. </h3>\nVisit  <a href="http://www.baidu.com">Baidu</a> here.'
        msg = 'hello world, :)'
        # reply_xml = """<xml>
        #     <ToUserName><![CDATA[%s]]></ToUserName>
        #    <FromUserName><![CDATA[%s]]></FromUserName>
        #    <CreateTime>%s</CreateTime>
        #    <MsgType><![CDATA[text]]></MsgType>
        #    <Content><![CDATA[%s]]></Content>
        # </xml>""" % (FromUserName, ToUserName, CreateTime, msg)
        # print('====================')
        # return HttpResponse(reply_xml, content_type="application/xml") # worked for weixin

        # from, to <=> to, from , SURE
        return render_to_response('tpl_text.xml', {'fromUserName': ToUserName,
                                                'toUserName': FromUserName,
                                                'createTime': CreateTime,
                                                'content': msg}, content_type="application/xml")
    elif Content == 'image':
        return render_to_response( 'tpl_image.xml', {'fromUserName': ToUserName,
                                                 'toUserName': FromUserName,
                                                 'createTime': CreateTime,
                                                 'mediaId': 1})
    elif Content == 'voice':
        return render_to_response('tpl_voice.xml', {'fromUserName': ToUserName,
                                                 'toUserName': FromUserName,
                                                 'createTime': CreateTime,
                                                 'mediaId': 1})
    elif Content == 'video':
        return render_to_response('tpl_video.xml', {'fromUserName': ToUserName,
                                                 'toUserName': FromUserName,
                                                 'createTime': CreateTime,
                                                 'mediaId': 1,
                                                 'title': 'Sample VIDEO',
                                                 'description': 'This is a sample video'})
    elif Content == 'music':
        return render_to_response('tpl_music.xml', {'fromUserName': ToUserName,
                                                 'toUserName': FromUserName,
                                                 'createTime': CreateTime,
                                                 'title': 'Sample Music',
                                                 'description': 'This is a sample music.',
                                                 'musicUrl': 'http://mp3.baidu.com/brench.mp3',
                                                 'hqMusicUrl': 'http://mp3.baidu.com/brench.ace',
                                                 'thumbMediaId': 2})
    elif Content == 'news':
        return render_to_response('tpl_news.xml', {'fromUserName': ToUserName,
                                                'toUserName': FromUserName,
                                                'createTime': CreateTime,
                                                'articles': [
                                                    {'title': 'Baidu', 'description':'Baidu.com',
                                                     'picUrl':'http://m.baidu.com/static/index/plus/plus_logo.png', 'url': 'http://www.baidu.com'},
                                                ]})
    return HttpResponse('')


from django.conf.urls import url, include, patterns

urlpatterns = patterns('',
                       url(r'^$', index),
                       )

# import sae
# application = sae.create_wsgi_application(get_wsgi_application())
import sys

if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
