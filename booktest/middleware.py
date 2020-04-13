from django.http import HttpResponse

class BlockedIPSMiddleware(object):
    '''中间件类'''
    EXCLUDE_IPS = ['192.168.31.141']
    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''视图函数调用之前会被调用'''
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in BlockedIPSMiddleware.EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')

class TestMiddleware(object):
    '''中间件'''
    def __init__(self):
        '''服务器重启后，接收第一个请求时调用'''
        print('----init----')

    def process_request(self, request):
        '''产生request对象之后，URL匹配之前调用'''
        print('----process_request----')

    def process_view(self, request, view_func, *view_args, **view_kwargs):
        '''URL匹配之后，视图函数调用之前调用'''
        print('----process_view----')

    def process_response(self, request, response):
        '''视图函数调用之后，内容返回浏览器之前调用'''
        print('----process_response----')
        return response