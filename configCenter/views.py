import json
from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from configCenter import custom_admin
from configCenter import forms
from configCenter import models
from configCenter.permissions import permission
from ManagerCenter.views import log, response_result
from utils import utils

@permission.check_permission
def menuLv1(request):
    '''索引， 进行了过滤，搜索，排序，分页功能的封装，字典形式返回，'''
    app_name, tab_name = request.path.strip('/').split('/')
    obj = utils.table_obj_show(request, app_name, tab_name)
    return render(request, 'configcenter/config_index.html', {'admin_class': obj['admin_class'],
                                                              "query_sets": obj['query_sets'],
                                                              'filter_conditions': obj['filter_conditions'],
                                                              'orderby_key': obj['orderby_key'],
                                                              'privious_orderby': request.GET.get('o', ''),
                                                              'search_text': request.GET.get('_q', '')})


@permission.check_permission
def menuLv2(request):
    app_name, tab_name = request.path.strip('/').split('/')
    obj = utils.table_obj_show(request, app_name, tab_name)
    return render(request, 'configcenter/config_index.html', {'admin_class': obj['admin_class'],
                                                              "query_sets": obj['query_sets'],
                                                              'filter_conditions': obj['filter_conditions'],
                                                              'orderby_key': obj['orderby_key'],
                                                              'privious_orderby': request.GET.get('o', ''),
                                                              'search_text': request.GET.get('_q', '')})


@permission.check_permission
def role_index(request):
    app_name, tab_name = request.path.strip('/').split('/')
    obj = utils.table_obj_show(request, app_name, tab_name)
    return render(request, 'configcenter/config_index.html', {'admin_class': obj['admin_class'],
                                                              "query_sets": obj['query_sets'],
                                                              'filter_conditions': obj['filter_conditions'],
                                                              'orderby_key': obj['orderby_key'],
                                                              'privious_orderby': request.GET.get('o', ''),
                                                              'search_text': request.GET.get('_q', '')})


@permission.check_permission
def account_index(request):
    app_name, tab_name = request.path.strip('/').split('/')
    obj = utils.table_obj_show(request, app_name, tab_name)
    return render(request, 'configcenter/config_index.html', {'admin_class': obj['admin_class'],
                                                              "query_sets": obj['query_sets'],
                                                              'filter_conditions': obj['filter_conditions'],
                                                              'orderby_key': obj['orderby_key'],
                                                              'privious_orderby': request.GET.get('o', ''),
                                                              'search_text': request.GET.get('_q', '')})


@permission.check_permission
def menuLv1_add(request):
    '''添加'''
    name_obj = request.path.strip('/').split('/')
    admin_class = custom_admin.enabled_admins[name_obj[0]][name_obj[1]]
    admin_class.is_add_form = True  # 这个在表单里标识为添加
    if request.method == 'POST':
        form_obj = forms.MenuLevel1Form(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            log.info('account:%s add level1 menu finish' % request.user)
            return redirect(request.path.replace('add/', ''))
    else:
        form_obj = forms.MenuLevel1Form()
    return render(request, 'configcenter/config_add_and_change.html',
                  {'form_obj': form_obj, 'admin_class': admin_class})


@permission.check_permission
def menuLv2_add(request):
    name_obj = request.path.strip('/').split('/')
    admin_class = custom_admin.enabled_admins[name_obj[0]][name_obj[1]]
    admin_class.is_add_form = True
    if request.method == 'POST':
        form_obj = forms.MenuLevel2Form(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            log.info('account:%s add level2 menu finish' % request.user)
            return redirect(request.path.replace('add/', ''))
    else:
        form_obj = forms.MenuLevel2Form()
    return render(request, 'configcenter/config_add_and_change.html',
                  {'form_obj': form_obj, 'admin_class': admin_class})


@permission.check_permission
def role_add(request):
    name_obj = request.path.strip('/').split('/')
    admin_class = custom_admin.enabled_admins[name_obj[0]][name_obj[1]]
    admin_class.is_add_form = True
    if request.method == 'POST':
        form_obj = forms.RoleForm(request.POST)
        if form_obj.is_valid():
            form_obj.save()
            log.info('account:%s add role finish' % request.user)
            return redirect(request.path.replace('add/', ''))
    else:
        form_obj = forms.RoleForm()
    return render(request, 'configcenter/config_add_and_change.html',
                  {'form_obj': form_obj, 'admin_class': admin_class})


@permission.check_permission
def account_add(request):
    name_obj = request.path.strip('/').split('/')
    admin_class = custom_admin.enabled_admins[name_obj[0]][name_obj[1]]
    admin_class.is_add_form = True
    if request.method == 'POST':
        form_obj = forms.AccountForm(request.POST)
        if form_obj.is_valid():
            data = form_obj.cleaned_data
            r_user = form_obj.save()
            log.info('account:%s add new user:%s finish' % (request.user,data['email']))
            # 对新注册的用于进行权限关联
            register_user = models.Account.objects.get(name=r_user.name)
            for perm in data['user_permissions']:
                register_user.user_permissions.add(perm.id)
            for r in data['roles']:
                register_user.roles.add(r.id)
            log.info('account:%s relevancy permission and role finish' % request.user)
            return redirect(request.path.replace('add/', ''))
    else:
        form_obj = forms.AccountForm()
    return render(request, 'configcenter/config_add_and_change.html',
                  {'form_obj': form_obj, 'admin_class': admin_class})


@permission.check_permission
def delete_obj(request, table_name):
    '''删除'''
    name_obj = request.path.strip('/').split('/')
    admin_class = custom_admin.enabled_admins[name_obj[0]][table_name]
    if request.method == 'POST':
        id_list = request.POST.getlist('delete_id')
        for id in id_list:
            obj = admin_class.model.objects.get(id=id)
            log.info('account:%s del obj:%s finish' % (request.user, obj))
            obj.delete()
        return HttpResponse(json.dumps('ok'))


@permission.check_permission
def menuLv1_change(request, obj_id):
    '''修改'''
    name_obj = request.path.strip('/').split('/')
    admin_class = custom_admin.enabled_admins[name_obj[0]][name_obj[1]]
    obj = admin_class.model.objects.get(id=obj_id)
    admin_class.is_add_form = False
    if request.method == 'POST':
        form_obj = forms.MenuLevel1Form(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            log.info('account:%s modify level1 menu finish, modify obj:%s' % (request.user, obj))
        return redirect('/%s/%s/' % (name_obj[0], name_obj[1]))

    else:
        form_obj = forms.MenuLevel1Form(instance=obj)
    return render(request, 'ConfigCenter/config_add_and_change.html',
                  {'form_obj': form_obj, 'admin_class': admin_class})


@permission.check_permission
def menuLv2_change(request, obj_id):
    name_obj = request.path.strip('/').split('/')
    admin_class = custom_admin.enabled_admins[name_obj[0]][name_obj[1]]
    obj = admin_class.model.objects.get(id=obj_id)
    admin_class.is_add_form = False
    if request.method == 'POST':
        form_obj = forms.MenuLevel2Form(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            log.info('account:%s modify level2 menu finish, modify obj:%s' % (request.user, obj))
        return redirect('/%s/%s/' % (name_obj[0], name_obj[1]))

    else:
        form_obj = forms.MenuLevel2Form(instance=obj)
    return render(request, 'ConfigCenter/config_add_and_change.html',
                  {'form_obj': form_obj, 'admin_class': admin_class})


@permission.check_permission
def role_change(request, obj_id):
    name_obj = request.path.strip('/').split('/')
    admin_class = custom_admin.enabled_admins[name_obj[0]][name_obj[1]]
    obj = admin_class.model.objects.get(id=obj_id)
    admin_class.is_add_form = False
    if request.method == 'POST':
        form_obj = forms.RoleForm(request.POST, instance=obj)
        if form_obj.is_valid():
            form_obj.save()
            log.info('account:%s modify role finish, modify obj:%s' % (request.user, obj))
        return redirect('/%s/%s/' % (name_obj[0], name_obj[1]))

    else:
        form_obj = forms.RoleForm(instance=obj)
    return render(request, 'ConfigCenter/config_add_and_change.html',
                  {'form_obj': form_obj, 'admin_class': admin_class})


@permission.check_permission
def account_change(request, obj_id):
    name_obj = request.path.strip('/').split('/')
    admin_class = custom_admin.enabled_admins[name_obj[0]][name_obj[1]]
    obj = admin_class.model.objects.get(id=obj_id)
    admin_class.is_add_form = False
    if request.method == 'POST':
        form_obj = forms.UserChangeForm(request.POST, instance=obj)
        if form_obj.is_valid():
            data = form_obj.cleaned_data
            form_obj.save()
            log.info('account:%s modify account finish, modify obj:%s' % (request.user, obj))
            # 对新注册的用于进行权限关联
            obj.user_permissions.clear()
            obj.roles.clear()
            for perm in data['user_permissions']:
                obj.user_permissions.add(perm.id)
            for del_role in obj.roles.all():
                obj.remove(del_role.id)
            for r in data['roles']:
                obj.roles.add(r.id)
        return redirect('/%s/%s/' % (name_obj[0], name_obj[1]))

    else:
        form_obj = forms.UserChangeForm(instance=obj)
    return render(request, 'ConfigCenter/config_add_and_change.html',
                  {'form_obj': form_obj, 'admin_class': admin_class})


@permission.check_permission
def reset_password(request, account_id):
    '''配置中心修改账号密码'''
    acct_obj = models.Account.objects.get(id=account_id)
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if len(password1) <= 6 or len(password2) <= 6:
            response_result.status = 0
            response_result.error = '密码长度不可以小于6位'
        elif password1 == password2:
            acct_obj.set_password(password1)
            acct_obj.save()
            log.info('account:%s reset user:%s password finish, modify obj:%s' % (request.user, acct_obj))
            response_result.status = 1
            response_result.message = '账号：%s 密码变更成功' % (acct_obj.email)
        else:
            response_result.status = 0
            response_result.error = '账号：%s 密码变更失败，2次密码不匹配' % (acct_obj.email)
        return JsonResponse(response_result.__dict__)


def not_found(request, tab_name, obj_id):
    '''未找到对应的页面'''
    log.error('page no found: %s' % request.path)
    return render(request, 'pages-nofound.html')
