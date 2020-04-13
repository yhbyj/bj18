from django.contrib import admin
from booktest.models import BookInfo, HeroInfo, AreaInfo, PicTest

# 后台管理相关文件
# Register your models here.
# 自定义模型管理类
class BookInfoAdmin(admin.ModelAdmin):
    '''图书模型管理类'''
    list_display = ['id', 'btitle', 'bpub_date']

class HeroInfoAdmin(admin.ModelAdmin):
    '''映像人物模型管理类'''
    list_display = ['id', 'hname', 'hcomment']


class AreaStackedInline(admin.StackedInline):
    # 写多类的名字
    model = AreaInfo
    extra = 2

class AreaTabularInline(admin.TabularInline):
    # 写多类的名字
    model = AreaInfo
    extra = 2

class AreaInfoAdmin(admin.ModelAdmin):
    '''地区模型管理类'''
    list_per_page = 10   # 指定每一页显示10条数据
    list_display = ['id', 'atitle', 'parent']   # 既可以指定模型的属性名，也可以指定模型的方法名
    actions_on_bottom = True
    actions_on_top = False
    list_filter = ['atitle']  # 列表页右侧过滤栏
    search_fields = ['atitle']  # 列表页上方的搜索框
    # fields = ['aparent', 'atitle']  # 编辑页面的字段显示顺序
    # 编辑页显示分组（与fields二选一）
    fieldsets = (
        ('基本', {'fields': ['atitle']}),
        ('高级', {'fields': ['aparent']}),
    )
    # inlines = [AreaStackedInline]  # 编辑页面以块的方式嵌入可编辑的多端对象
    inlines = [AreaTabularInline]  # 编辑页面以表格的方式嵌入可编辑的多端对象

# 注册模型类
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
admin.site.register(AreaInfo, AreaInfoAdmin)
admin.site.register(PicTest)