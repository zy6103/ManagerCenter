#!/opt/python3/bin/python3
# Author: zhaoyong
# 装饰器，实现权限控制
from configCenter.permissions import permission_dict
from django.shortcuts import redirect, render
from django.core.urlresolvers import resolve


def perm_check(*args, **kwargs):
    '''认证检测'''
    request = args[0]
    if request.user.is_authenticated():
        if request.user.is_admin:  # 管理员跳过权限验证
            return True
        for permission_name, v in permission_dict.perm_dict.items():
            url_matched = False
            if v['url_type'] == 1:  # absolute 绝对URL
                if v['url'] == request.path:  # 绝对URL匹配完成
                    url_matched = True
            else:
                # 把绝对的URL请求转成相对的URL name
                resolve_url_name = resolve(request.path)
                if resolve_url_name.url_name == v['url']:  # 相对的url 别名匹配上
                    url_matched = True

            if url_matched:
                if request.method in v['method']:  # 请求方法匹配上
                    arg_matched = True
                    for request_arg in v['args']:
                        request_method_func = getattr(request, v['method'])
                        if not request_method_func.get(request_arg):
                            arg_matched = False
                    if arg_matched:  # 走到这里，只代表这个请求和这条权限的定义规则匹配上了
                        if request.user.has_perm(permission_name):  # 有权限
                            return True
                        else:
                            return False
    else:
        return redirect("/accounts/login/")


def check_permission(func):
    def inner(*args, **kwargs):
        if perm_check(*args, **kwargs) is True:
            return func(*args, **kwargs)
        else:
            return render(args[0], 'pages-404.html')

    return inner
