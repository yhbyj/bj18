
from django.conf.urls import include, url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index, name='index'),   # 图书信息页面
    url(r'^create$', views.create),   # 新增一本图书
    url(r'^delete/(\d+)$', views.delete),   # 删除一本图书
    # url(r'^books$', views.books),
    url(r'^books$', views.show_books),
    # url(r'^books/(^P<book_id>\d+)$', views.BookDetails),
    # url(r'^books/(?P<bid>\d+)$', views.detail),
    url(r'^books/(\d+)$', views.detail),
    url(r'^login_ajax$', views.login_ajax),   #显示ajax登录页面
    url(r'^login_ajax_check$', views.login_ajax_check),   # ajax登录校验
    url(r'^set_cookie$', views.set_cookie),   # 设置 cookie
    url(r'^get_cookie$', views.get_cookie),  # 获取 cookie
    url(r'^login$', views.login),   # 显示登录页面
    url(r'^login_check$', views.login_check),  # 用户登录校验
    url(r'^set_session$', views.set_session),   #  设置 session
    url(r'^get_session$', views.get_session),   # 获取 session
    url(r'^change_pwd$', views.change_pwd),   # 修改用户密码页面
    url(r'^change_pwd_action$', views.change_pwd_action),   # 修改用户密码确认页面
    url(r'^verify_code$', views.verify_code),   # 获取验证码
    url(r'^url_reverse$', views.url_reverse),   # url反向解析页面
    url(r'^show_args/(\d+)/(\d+)$', views.show_args, name='show_args'),   # 捕获位置参数
    url(r'^show_kwargs/(?P<c>\d+)/(?P<d>\d+)$', views.show_kwargs, name='show_kwargs'),   # 捕获参关键字数
    url(r'^test_redirect$', views.test_redirect),   #
]
