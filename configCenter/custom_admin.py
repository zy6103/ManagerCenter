#!/opt/python3/bin/python3
# Author: zhaoyong

from configCenter import models

# 效果： {'appName': {'table_name':'admin_class'}}
enabled_admins = {}


class BaseAdmin(object):
    list_display = []  # 显示字段
    list_filters = []  # 过滤字段
    search_filters = []  # 查找字段
    list_per_page = 10  # 每页显示数据量
    ordering = None  # 默认排序字段
    readonly_field = []  # 字段只读


class RoleAdmin(BaseAdmin):
    list_display = ('name', 'menu_level1')
    list_filters = ('name', 'menu_level1')
    search_filters = ('name',)
    readonly_field = ()


class MenuLevel1Admin(BaseAdmin):
    list_display = ('name', 'url_type', 'url_name')
    list_filters = ('name', 'url_type', 'url_name')
    search_filters = ('name', 'url_type', 'url_name')
    readonly_field = ()


class MenuLevel2Admin(BaseAdmin):
    list_display = ('name', 'url_name', 'level2_to_level1')
    list_filters = ('name', 'url_name', 'level2_to_level1')
    search_filters = ('name', 'url_name')
    readonly_field = ()


class AccountAdmin(BaseAdmin):
    list_display = ('id', 'email', 'name', 'is_active', 'is_admin', 'set_password')
    list_filters = ('email', 'name')
    search_filters = ('email', 'name')
    readonly_field = ('email',)

    def set_password(self):
        '''自定义字段'''
        return '''<a onclick='SetPassword(%s,"%s")' style='color:blue;'>修改密码</a>''' % (
        self.instance.id, self.instance.email)

    set_password.display_name = 'reset password '


def register(model_class, admin_class=None):
    if model_class._meta.app_label not in enabled_admins:
        enabled_admins[model_class._meta.app_label] = {}  # 添加app名称

    admin_class.model = model_class  # 绑定model 对象和admin类
    enabled_admins[model_class._meta.app_label][model_class._meta.model_name] = admin_class
    # 以上这行相当于：enabled_admin['crm']['customerfollowup'] = CustomerFollowUpAdmin
    # 这里CustomerFollowUpAdmin包含所有的静态字段，还包含当前操作的表对象，用.model调用
    # print('---enabled_admins:', enabled_admins)

register(models.Role, RoleAdmin)
register(models.MenuLevel1, MenuLevel1Admin)
register(models.MenuLevel2, MenuLevel2Admin)
register(models.Account, AccountAdmin)
