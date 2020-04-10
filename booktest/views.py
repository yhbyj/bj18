from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from booktest.models import  BookInfo, HeroInfo
from datetime import date

def my_render(request, template_path, context_dict={}):
    '''使用模板文件'''
    # 使用模板文件
    # 1.加载模板文件
    temp = loader.get_template(template_path)
    # 2.定义模板上下文，给模板文件传递数据
    context = RequestContext(request, context_dict)
    # 3. 模板渲染，产生标准的HTML内容
    rest_html = temp.render(context)
    # 4. 返回给浏览器
    return HttpResponse(rest_html)

# Create your views here.
# 1. 定义视图函数，HttpRequest
# 2. 进行url配置处理，建立url地址和视图的对应关系
# http://127.0.0.1:8000/index
def index(request):
    '''显示图书信息'''
    # 1. 查询出所有图书的信息
    books = BookInfo.objects.all()
    # 2.使用模板
    return render(request, 'booktest/index.html', {'books':books})

    # 进行处理，与M和T进行交互
    # return HttpResponse('老铁，没毛病')
    # return my_render(request, 'booktest/index.html')
    # context = {'content':'hello world', 'list':list(range(1,10))}
    # return render(request, 'booktest/index.html', context)

def create(request):
    '''新增一本图书'''
    # 1. 创建BOOKINFO对象
    b = BookInfo()
    b.btitle = '流星蝴蝶剑'
    b.bpub_date = date(1990,1,1)
    # 2.保存进数据库
    b.save()
    # 3.返回应答，让浏览器再访问/index，重定向
    # return HttpResponse('ok')
    return HttpResponseRedirect(redirect_to='/index')

def delete(request, bid):
    '''删除点击的图书'''
    # 1.通过BID获取图书对象
    b = BookInfo.objects.get(id=bid)
    # 2.删除
    b.delete()
    # 3.重定向，让浏览器再访问/index
    # return HttpResponseRedirect(redirect_to='/index')
    return redirect('/index')

def show_books(request):
    '''显示图书的信息'''
    # 1. 通过M查找图书表中的数据
    books = BookInfo.objects.all()
    # 2. 使用模板
    return render(request, 'booktest/show_books.html', {'books':books})

def detail(request, bid):
    '''查询图书关联的英雄信息'''
    # 1.根据BID查询图书信息
    book = BookInfo.objects.get(id=bid)
    # 2. 查询图书关联的英雄信息
    heros = book.heroinfo_set.all()
    return render(request, 'booktest/detail.html', {'book':book, 'heros':heros})

def books(request):
    '''返回图书列表'''
    books = BookInfo.objects.all()
    context = {'books':books}
    return render(request, 'booktest/books.html', context)

def BookDetails(request, book_id):
    '''返回图书列表'''
    book = BookInfo.objects.get(id=book_id)
    heroes = book.heroinfo_set
    context = {'book':book, 'heroes': heroes}
    return render(request, 'booktest/book_details.html', context)

