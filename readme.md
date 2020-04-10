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

