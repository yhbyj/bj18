
from django.conf.urls import include, url
from booktest import views

urlpatterns = [
    url(r'^index$', views.index),   # 图书信息页面
    url(r'^create$', views.create),   # 新增一本图书
    url(r'^delete/(\d+)$', views.delete),   # 删除一本图书
    # url(r'^books$', views.books),
    url(r'^books$', views.show_books),
    # url(r'^books/(^P<book_id>\d+)$', views.BookDetails),
    # url(r'^books/(?P<bid>\d+)$', views.detail),
    url(r'^books/(\d+)$', views.detail),
]
