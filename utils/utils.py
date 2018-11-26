#!/opt/python3/bin/python3
# Author: zhaoyong
from django.db.models import Q
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from configCenter import custom_admin


class ResponseLog(object):
    '''前后端信息交互
       status: 后端执行状态，解释：1 -> 成功  0 -> 失败
       data : 后端执行后返回的数据，如果没有则为：None
       message: 后端执行成功后返回的消息内容
       error: 后端执行失败后返回的失败内容
    '''
    status = 1
    data = None
    message = None
    error = None


def table_obj_show(request, app_name, tab_name):
    '''
    功能封装
    :param request: 请求类型
    :param app_name: 应用名称
    :param tab_name: 表名
    :return:
    '''
    admin_class = custom_admin.enabled_admins[app_name][tab_name]
    object_list, filter_conditions = table_filter(request, admin_class)  # 过滤后的结果
    object_list = table_search(request, admin_class, object_list)  # 搜索
    object_list, orderby_key = table_sort(request, object_list)  # 排序
    paginator = Paginator(object_list, admin_class.list_per_page)  # 每页显示数据数量
    page = request.GET.get('page')
    try:
        query_sets = paginator.page(page)
    except PageNotAnInteger:
        query_sets = paginator.page(1)
    except EmptyPage:
        query_sets = paginator.page(paginator.num_pages)
    return {'admin_class': admin_class, 'query_sets': query_sets, 'filter_conditions': filter_conditions,
            'orderby_key': orderby_key}


def table_filter(request, admin_class):
    '''
    进行条件过滤并返回过滤后的数据，如：source=1&consultent=5&consult_course=1
    :param request:
    :param admin_class:
    :return:
    '''
    filter_conditions = {}
    keywords = ['page', 'o', '_q']
    for k, v in request.GET.items():
        if k in keywords:  # 保留分页关键字 and 排序关键字
            continue
        if v:
            filter_conditions[k] = v

    return admin_class.model.objects.filter(**filter_conditions).order_by(
        "-%s" % admin_class.ordering if admin_class.ordering else "-id"), filter_conditions


def table_sort(request, objs):
    '''
    排序
    :param request: 请求对象
    :param objs: 表对象
    :return:
    '''
    orderby_key = request.GET.get('o')
    if request.GET.get('o'):
        res = objs.order_by(orderby_key)
        if orderby_key.startswith('-'):
            orderby_key = orderby_key.strip('-')
        else:
            orderby_key = '-%s' % orderby_key
    else:
        res = objs
    return res, orderby_key


def table_search(request, admin_class, object_list):
    '''
    搜索
    :param request:
    :param admin_class: 管理类
    :param object_list: 对象列表
    :return:
    '''
    search_key = request.GET.get('_q', "")
    if search_key:
        q_obj = Q()
        q_obj.connector = 'OR'
        for column in admin_class.search_filters:
            q_obj.children.append(("%s__contains" % column, search_key))
        res = object_list.filter(q_obj)
    else:
        res = object_list
    return res
