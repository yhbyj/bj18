#Django练习  
参考：  
1、[传智播客 python 高级编程 (day11Django框架~day14 天天生鲜Django项目）](https://www.bilibili.com/video/BV1CJ411G79F?from=search&seid=13747040854823667147)  
2、[django 1.8.2 中文文档](https://yiyibooks.cn/xx/django_182/index.html)    
## 第一天
## 练习环境准备：
1、Windows 10 教育版  
2、PyCharm Community Edition 2019.3.4 x64  + 插件：Gitee(码云)  
push https://github.com/yhbyj/bj18.git  
push https://gitee.com/zjdyez/bj18.git  
3、python 3.6.8 + django 1.8.2  + ipython
pip install django==1.8.2 -i https://mirrors.aliyun.com/pypi/simple  
pip install ipython -i https://mirrors.aliyun.com/pypi/simple   
4、phpstudy_pro： mysql, redis等工具  
5、linux + mysql  
## 主要内容
1、创建工程、应用、后台管理员（amdin/admin）等  
django-admin startproject test1  
python manage.py startapp booktest  
2、创建数据库 ，迁移数据库等。  
mysql> create database bj18 default charset=utf8;  
grant all on bj18.* to 'test1'@'%' identified by '123456';  
flush privileges;  
python manage.py makemigrations  
python manage.py migrate  
3、测试 
例子：查询1980年发表的图书。  
python manage.py shell    
from booktest.models import BookInfo  
BookInfo.objects.filter(bpub_date__year=1980)    
注意：连上linux的mysql服务器，开启日志功能，可以查看到查询是如何在数据库上发生的！  
$ vi my.conf  
generate_log_file  = /var/log/mysql/mysql.log   
log_error =  /var/log/mysql/error.log       
$ tail -f /var/log/mysql/mysql.log   
## 第二天  
### ajax 登录案例  
jquery-1.12.4.min.js  
### cookie
由服务器产生，保存在客户端（如浏览器）！  
response = HttpResponse('设置cookie')   
response.set_cookie('num', 1)   

request.COOKIES['num']  
### session
由服务器产生，保存在服务器端！  
你去办健身卡，你的信息都保存在电脑中，给你卡号（cookie seesionid）  
request.session['username'] = 'smart'  
request.session['age'] = 18   
表 django_session 中以 base64编码格式保存   
### 登录装饰器
@login_required  
### csrf
中间件：'django.middleware.csrf.CsrfViewMiddleware'  
### 验证码
pip install Pillow -i https://mirrors.aliyun.com/pypi/simple   
from PIL import Image, ImageDraw, ImageFont   
### 反向解析
from django.core.urlresolvers import reverse  
### 静态文件
STATIC_URL = '/static/'   #设置访问静态文件对应的url  
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]   #设置静态文件所在的物理目录  
## 第三天
### 中间件
预留函数  
----init----  
----process_request----  
----process_view----   
----process_response----   
### 后台管理
模型管理类、列表页、编辑页  
重写模板： Lib\site-packages\django\contrib\admin\templates\admin\base_site.html   
上传图片： MEDIA_ROOT  
### 省市县案例
ajax 

  





       