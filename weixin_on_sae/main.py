from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import logging
logger = logging.getLogger(__name__)

def checkSignature(request):
    '''
    signature=9c5f1d86525dcb9300ce55f03040a8932e48d4f7&echostr=5667388023579343993&timestamp=1438566449&nonce=209415066 500 0.413 0.413 53112
    :param request:
    :return:
    '''
    signature = request.GET.get('signature', None)
    timestamp = request.GET.get('timestamp', None)
    nonce = request.GET.get('nonce', None)
    echostr = request.GET.get('echostr', None)

    token = '015433'

    l = [token, timestamp, nonce]
    l.sort()
    s = ''.join(l)
    import hashlib
    ret = hashlib.sha1(s.encode('utf-8')).hexdigest()
    if ret == signature:
        return echostr
    else:
        raise Exception('WRONG Sig#' + signature)

@csrf_exempt
def index(requset):
    if requset.method == 'GET':
        return HttpResponse(checkSignature(requset))

    from xml.etree import ElementTree
    from django.utils.encoding import smart_str, smart_unicode
    xmlstr = smart_str(requset.body)
    logger.info(xmlstr)
    xml = ElementTree.fromstring(xmlstr)
    ToUserName = xml.find('ToUserName').text
    FromUserName = xml.find('FromUserName').text
    CreateTime = xml.find('CreateTime').text
    MsgType = xml.find('MsgType').text
    Content = xml.find('Content').text
    MsgId = xml.find('MsgId').text
    reply_xml = """<xml>
        <ToUserName><![CDATA[%s]]></ToUserName>
       <FromUserName><![CDATA[%s]]></FromUserName>
       <CreateTime>%s</CreateTime>
       <MsgType><![CDATA[text]]></MsgType>
       <Content><![CDATA[%s]]></Content>
    </xml>""" % (FromUserName, ToUserName, CreateTime, Content + "  Hello world, this is test message")
    return HttpResponse(reply_xml)


from django.conf.urls import url, include, patterns

urlpatterns = patterns('',
                       url(r'^$', index),
                       )

# import sae
# application = sae.create_wsgi_application(get_wsgi_application())
import sys

if __name__ == '__main__':
    from django.conf import settings

    settings.configure(
        DEBUG=True,
        SECRET_KEY='thisisthesecret',
        ROOT_URLCONF='main',
    )
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
