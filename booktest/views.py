from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader, RequestContext
from booktest.models import  BookInfo, HeroInfo, PicTest, AreaInfo
from datetime import date
from django.conf import settings

EXCLUDE_IPS = ['192.168.31.141']
def blocked_ips(view_func):
    '''阻止某些IP地址访问的装饰器'''
    def wrapper(request, *view_args, **view_kwargs):
        # 获取浏览器的IP地址
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in EXCLUDE_IPS:
            return HttpResponse('<h1>Forbidden</h1>')
        else:
            return view_func(request, *view_args, **view_kwargs)
    return wrapper

def login_required(view_func):
    '''登录判断装饰器'''
    def wrapper(request, *view_args, **view_kwargs):
        # 判断用户是否登录
        if request.session.has_key('isLogin'):
            # 用户已登录，调用对应的视图
            return view_func(request, *view_args, **view_kwargs)
        else:
            # 用户未登录，跳转到登录页面
            return redirect('/login')
    return wrapper

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
    '''首页'''
    # print('----index----')
    # print(settings.FILE_UPLOAD_HANDLERS)
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

# /login
def login(request):
    '''显示登录页面'''
    # 判断用户是否已登录
    if request.session.has_key('isLogin'):
        # 用户已登录，跳转到首页
        # return redirect('/index')
        # 用户已登录，跳转到密码修改页面
        return redirect('/change_pwd')
    else:
        # 获取cookie username
        if 'username' in request.COOKIES:
            # 获取记住的用户名
            username = request.COOKIES['username']
        else:
            username = ''
        return render(request, 'booktest/login.html', {'username':username})

# /login_check
def login_check(request):
    '''登录校验视图'''
    # request.POST 保存的是post方式提交的参数 QueryDict
    # request.GET 保存的是get方式提交的参数
    # print(request.method)
    # 1.获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    remember = request.POST.get('remember')
    # print(remember)
    # 获取用户输入的验证码
    vcode = request.POST.get('vcode')
    # 获取session中保存的验证码
    verifycode = request.session.get('verifycode')
    # 进行验证码校验
    if vcode != verifycode:
        # 验证码错误
        return redirect('/login')
    # 2.进行登录的校验
    # 实际开发：根据用户名和密码查找数据库
    # 模拟：smart  123
    if username == 'smart' and password == '123' :
        # 用户名和密码正确，跳转到首页
        # response = redirect('/index')
        # 用户名和密码正确，跳转到密码修改页面
        response = redirect('/change_pwd')
        # 判断是否需要记住用户名
        if remember == 'on':
            # 设置Cookie username，过期时间1周
            response.set_cookie('username', username, max_age=7*24*3600)
        # 记住用户的登录状态
        # 只要session中有isLogin，就认为用户已经登录，不管它是什么值。
        request.session['isLogin'] = True
        # 记住登录的用户名
        request.session['username'] = username
        return  response
    else:
        # 用户名或密码错误，跳转到登录页面
        return redirect('/login')

# /login_ajax
def login_ajax(request):
    '''显示Ajax登录页面'''
    return render(request, 'booktest/login_ajax.html')

# /login_ajax_check
def login_ajax_check(request):
    '''Ajax登录校验'''
    # 1.获取用户名和密码
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 2.进行校验，放回json数据
    if username == 'smart' and password == '123' :
        # 用户名和密码正确
        return JsonResponse({'res':1})
    else:
        # 用户名或密码错误
        return JsonResponse({'res': 0})

# /set_session
def set_session(request):
    '''设置session信息'''
    request.session['username'] = 'smart'
    request.session['age'] = 18
    return HttpResponse('设置session')

# /get_session
def get_session(request):
    '''获取session的信息'''
    username = request.session['username']
    age = request.session['age']
    return HttpResponse(username + ':' + age)

# /set_cookie
def set_cookie(request):
    '''设置Cookie信息'''
    response = HttpResponse('设置cookie')
    # 设置一个Cookie信息
    response.set_cookie('num', 1)
    # 返回 response
    return response

# /get_cookie
def get_cookie(request):
    '''获取Cookie的信息'''
    # 取出Cookie num 的值
    num = request.COOKIES['num']
    return  HttpResponse(num)

# /change_pwd
@login_required
# login_required(change_pwd)(request, *view_args, *view_kwargs)
def change_pwd(request):
    '''修改密码页面'''
    return render(request, 'booktest/change_pwd.html')

# /change_pwd_action
@login_required
def change_pwd_action(request):
    '''模拟修改密码处理'''
    # 1.获取新密码
    pwd = request.POST.get('pwd')
    # 获取用户名
    username = request.session.get('username')
    # 2.实际开发的时候：修改对应数据库中的内容……
    # 3. 返回一个应答
    return HttpResponse('%s修改的密码为：%s'%(username,pwd))

from PIL import Image, ImageDraw, ImageFont
from django.utils.six import BytesIO

# /verify_code
def verify_code(request):
    # 引入随机函数模块
    import  random
    # 定义变量，用于函数的背景色、宽、高
    bgcolor = (random.randrange(20, 100), random.randrange(20, 100), 255)
    width = 100
    height = 25
    # 创建画面对象
    im = Image.new('RGB', (width, height), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, height))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWZYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0,4):
        rand_str += str1[random.randrange(0, len(str1))]
    # 构造字体对象，ubuntu的字体路径为'/usr/share/fonts/truetype/freefont'
    # font = ImageFont.truetype('FreeMono.ttf', 23)
    font = ImageFont.truetype('C:\Windows\Fonts\simsunb.ttf', 23)
    # 构造字体颜色
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制四个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # 存入session，用于做进一步的验证
    request.session['verifycode'] = rand_str
    # 内存文件操作
    buf = BytesIO()
    # 将图片保存在内存，文件类型为png
    im.save(buf, 'png')
    return  HttpResponse(buf.getvalue(), 'image/png')

# /url_reverse
def url_reverse(request):
    '''url反向解析页面'''
    return render(request, 'booktest/url_reverse.html')

# /show_args/(\d+)/(\d+)
def show_args(request, a, b):
    return  HttpResponse(a + ':' + b)

# /show_kwargs/(?P<c>\d+)/(?P<d>\d+)
def show_kwargs(request, c, d):
    return  HttpResponse(c + ':' + d)

from django.core.urlresolvers import reverse
# /test_redirect
def test_redirect(request):
    # return redirect('/index')
    # 重定向到/index
    # url = reverse('booktest:index')
    # 重定向到/show_args/1/2
    # url = reverse('booktest:show_args', args=(1,2))
    # 重定向到/show_kwargs/3/4
    url = reverse('booktest:show_kwargs', kwargs={'c':3, 'd':4})
    return redirect(url)

# /test_static
def test_static(request):
    '''静态文件测试页码'''
    return render(request, 'booktest/test_static.html')

# /show_upload
def show_upload(request):
    '''显示上传图片页面'''
    return render(request, 'booktest/upload_pic.html')

def upload_handle(request):
    '''上传图片处理'''
    # 1.获取上传的图片
    # 上传文件不大于2.5M时， 文件放在内存中
    pic = request.FILES['pic']
    # print(type(pic))
    # print(pic.name)
    # pic.chunks()
    # 2.创建一个文件
    save_path = '%s/booktest/%s'%(settings.MEDIA_ROOT, pic.name)
    with open(save_path, 'wb') as f:
        # 3.获取上传文件的内容，并写入创建的文件中
        for content in pic.chunks():
            f.write(content)
    # 4.在数据库中保存上传记录
    PicTest.objects.create(goods_pic='booktest/%s'%pic.name)
    # 5.返回
    return HttpResponse('ok')

# /show_area页码
# 前端访问时，需要传递页码
from django.core.paginator import Paginator
def show_area(request, pindex):
    '''分页'''
    # 1.查询出所有省级地区的信息
    areas = AreaInfo.objects.filter(aparent__isnull=True)
    # 2.分页，每页显示10条
    pageinator = Paginator(areas, 10)
    # print(pageinator.num_pages)
    # print(pageinator.page_range)
    # 3.获取pindex的内容
    if pindex == '':
        # 默认取第一页的内容
        pindex = 1
    else:
        pindex = int(pindex)
    # page 是的Page类的实例对象
    page = pageinator.page(pindex)
    # print(page.number)
    # 4. 使用数模板
    return render(request, 'booktest/show_area.html', {'page':page})

# /areas
def areas(request):
    '''显示省市县信息'''
    return render(request, 'booktest/areas.html')

# /prov
def prov(request):
    '''获取所有省级地区的信息'''
    # 1.查询出所有省级地区的信息
    areas = AreaInfo.objects.filter(aparent__isnull=True)
    # 2.变量areas拼接出json数据：atitle id
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.atitle))
    # 3.返回数据
    return JsonResponse({'data': areas_list})

# /city
def city(request, pid):
    '''获取pid的下级地区的信息'''
    # 1.获取pid对应地区的下级地区
    # area = AreaInfo.objects.get(id=pid)
    # areas = area.areainfo_set.all()
    areas = AreaInfo.objects.filter(aparent__id=pid)
    # 2.变量areas拼接出json数据：atitle id
    areas_list = []
    for area in areas:
        areas_list.append((area.id, area.atitle))
    # 3.返回数据
    return JsonResponse({'data': areas_list})
