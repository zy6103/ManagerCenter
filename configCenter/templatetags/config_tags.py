#!/opt/python3/bin/python3
# Author: zhaoyong
from django import template
from django.utils.safestring import mark_safe
from django.utils.timezone import datetime, timedelta
from django.core.exceptions import FieldDoesNotExist
import json

register = template.Library()


@register.simple_tag
def get_model_name(admin_class):
    return admin_class.model._meta.verbose_name_plural


@register.simple_tag
def render_filter_ele(filter_field, admin_class, filter_conditions):
    '''
    过滤
    :param filter_field: admin_class.list_filters 中定义的字段名称，用于过滤
    :param admin_class: 管理类
    :param filter_conditions: 查询的字段名和字段值
    :return:
    '''
    select_ele = "<select class='form-control' name='{filter_field}'><option value=''>-----</option>"
    field_obj = admin_class.model._meta.get_field(filter_field)  # 获取到字段对象

    if field_obj.choices:  # choices字段类型
        selected = ''
        for choice_item in field_obj.choices:
            if filter_conditions.get(filter_field) == str(choice_item[0]):
                selected = "selected"
            select_ele += '''<option value='%s' %s> %s</option>''' % (choice_item[0], selected, choice_item[1])
            selected = ''
    if type(field_obj).__name__ == 'ForeignKey':  # 外键类型
        selected = ''
        for choice_item in field_obj.get_choices()[1:]:
            if filter_conditions.get(filter_field) == str(choice_item[0]):
                selected = "selected"
            select_ele += '''<option value='%s' %s> %s</option>''' % (choice_item[0], selected, choice_item[1])
            selected = ''

    if type(field_obj).__name__ in ['DateTimeField', 'DateField']:  # 日期类型
        date_ele = []
        today_ele = datetime.now().date()
        date_ele.append(['今天', datetime.now().date()])
        date_ele.append(['昨天', today_ele - timedelta(days=1)])
        date_ele.append(['近7天', today_ele - timedelta(days=7)])
        date_ele.append(['近30天', today_ele - timedelta(days=30)])
        date_ele.append(['近90天', today_ele - timedelta(days=90)])
        date_ele.append(['近180天', today_ele - timedelta(days=180)])
        date_ele.append(['近一年', today_ele - timedelta(days=365)])
        date_ele.append(['本月', today_ele.replace(day=1)])
        date_ele.append(['本年', today_ele.replace(month=1, day=1)])
        selected = ''
        for item in date_ele:
            select_ele += '''<option value='%s' %s> %s</option>''' % (item[1], selected, item[0])

        filter_field_name = "%s__gte" % filter_field
    if type(field_obj).__name__ in ['EmailField', 'CharField']:  # 邮箱和charfield 类型
        filter_field_name = filter_field
        for f_obj in admin_class.model.objects.all():
            v = getattr(f_obj, filter_field)
            selected = ''
            if filter_conditions.get(filter_field) == v:
                selected = "selected"
            # select_ele += '''<option value='%s' %s> %s</option>''' % (choice_item[0], selected, choice_item[1])
            # selected = ''
            select_ele += '''<option value='%s' %s> %s</option>''' % (v, selected, v)

    else:
        filter_field_name = filter_field

    select_ele = select_ele.format(filter_field=filter_field_name)
    select_ele += "</select>"
    return mark_safe(select_ele)


@register.simple_tag
def build_table_header_column(column, orderby_key, filter_conditions, admin_class):
    '''

    :param column:  admin_class.list_display 的字段名
    :param orderby_key:  进行排序的字段
    :param filter_conditions: 查询的字段名和字段值
    :param admin_class: 管理类
    :return:
    '''
    filters = ''
    for k, v in filter_conditions.items():  # 增加搜索的url
        filters += "&%s=%s" % (k, v)

    ele = '<th><a href="?o={orderby_key}{filters}">{column}</a> \
          {sort_icon}</th>'

    if orderby_key:  # 正序和倒序
        if orderby_key.startswith('-'):
            sort_icon = '<span class="glyphicon glyphicon-chevron-up" aria-hidden="true"></span>'
        else:
            sort_icon = '<span class="glyphicon glyphicon-chevron-down" aria-hidden="true"></span>'

        if orderby_key.strip('-') == column:
            orderby_key = orderby_key
        else:
            orderby_key = column
            sort_icon = ''
    else:
        orderby_key = column
        sort_icon = ''
    try:
        column_verbose_name = admin_class.model._meta.get_field(column).verbose_name  # 表字段名称
    except FieldDoesNotExist as e:
        column_verbose_name = getattr(admin_class, column).display_name  # 自定义字段名称
        ele = '<th><a href="javascript:void(0)">{column}</a></th>'.format(column=column_verbose_name)
    ele = ele.format(orderby_key=orderby_key, column=column_verbose_name, sort_icon=sort_icon, filters=filters)
    return mark_safe(ele)


@register.simple_tag
def build_table_row(request, obj, admin_class):
    '''
    :param request: 请求对象
    :param obj: 数据对象
    :param admin_class:  管理类
    :return:
    '''
    row_ele = ""
    for index, column in enumerate(admin_class.list_display):
        try:
            field_obj = obj._meta.get_field(column)  # 这里get不到字段就报错了
            if field_obj.choices:  # 判断是否为choices字段类型,当存在数据表示为choices字段
                column_data = getattr(obj, "get_%s_display" % column)()  # 提取choices字段类型数据
            elif type(field_obj).__name__ == 'datetime':
                column_data = column_data.strftime("%Y-%m-%d %H:%M:%S")
            elif type(field_obj).__name__ == 'ManyToManyField':
                data = getattr(obj, column).all()
                column_data = [column.name for column in data]
                column_data = ','.join(column_data)
            elif type(field_obj).__name__ == 'ForeignKey':
                column_data = getattr(obj, column)
            else:
                column_data = getattr(obj, column)
            if index == 0:  # add a tag,  可以跳转到修改页
                column_data = "<a href={request_path}{obj_id}/change>{data}</a>".format(request_path=request.path,
                                                                                        obj_id=obj.id, data=column_data)
        except FieldDoesNotExist as e:  # 数据库里找不到指定的字段，就到这里查找
            if hasattr(admin_class, column):  # 自定义字段
                column_func = getattr(admin_class, column)
                admin_class.instance = obj
                admin_class.request = request
                column_data = column_func()
        row_ele += "<td>%s</td>" % column_data
    return mark_safe(row_ele)


@register.simple_tag
def build_paginatora(query_sets, filter_conditions, privious_orderby, search_text):
    '''
    :param query_sets: 每页的数据对象
    :param filter_conditions: 查询的字段名和字段值
    :param privious_orderby: 排序字段
    :param search_text: 搜索字段文本
    :return:
    '''
    pages_btns = ''
    filters = ''
    for k, v in filter_conditions.items():  # 增加搜索的url
        filters += "&%s=%s" % (k, v)

    if query_sets.has_previous():
        pages_btns += '<li><a href="?page=%s%s&o=%s&_q=%s">上一页</a></li>' % (
            query_sets.previous_page_number(), filters, privious_orderby, search_text)
    added_dot_ele = False
    for page_num in query_sets.paginator.page_range:
        if page_num < 3 or page_num > query_sets.paginator.num_pages - 2 or abs(
                        query_sets.number - page_num) <= 2:  # 代表最前2页或者最后2页
            ele_class = ""
            if query_sets.number == page_num:
                added_dot_ele = False
                ele_class = "active"
            pages_btns += '<li class="%s"><a href="?page=%s%s&o=%s&_q=%s">%s</a></li>' % (
                ele_class, page_num, filters, privious_orderby, search_text, page_num)
        else:
            if added_dot_ele == False:
                pages_btns += '<li class="%s"><a href="#">...</a></li>' % ele_class
                added_dot_ele = True
    if query_sets.has_next():
        pages_btns += '<li><a href="?page=%s%s&o=%s&_q=%s">下一页</a></li>' % (
            query_sets.next_page_number(), filters, privious_orderby, search_text)
    return mark_safe(pages_btns)


@register.simple_tag
def get_m2m_obj_list(admin_class, field, form_obj):
    '''
    返回M2M的所有待选数据
    :param admin_class: 管理类
    :param field: 字段对象
    :param form_obj: 表单对象
    :return:
    '''
    field_obj = getattr(admin_class.model, field.name)
    all_obj_list = field_obj.rel.to.objects.all()  # 所有待选的数据

    # 单条数据的对象中的某个字段
    if form_obj.instance.id:
        obj_instance_field = getattr(form_obj.instance, field.name)
        selectd_obj_list = obj_instance_field.all()
    else:  # 代表这是在 创建新的一条记录
        return all_obj_list
    # 进行对已使用的数据过滤
    standby_obj_list = []
    for obj in all_obj_list:
        if obj not in selectd_obj_list:
            standby_obj_list.append(obj)
    return standby_obj_list


@register.simple_tag
def get_m2m_selectd_obj_list(form_obj, field):
    '''
    返回已经选中的M2M数据
    :param form_obj: 表单对象
    :param field: 字段对象
    :return:
    '''
    if form_obj.instance.id:  # 这里用于修改数据的复选框显示，添加数据没有M2M数据，所以不返回
        field_obj = getattr(form_obj.instance, field.name)
        return field_obj.all()


@register.simple_tag
def get_m2m_perm_list(admin_class, field, form_obj):
    '''
    返回M2M的所有待选数据
    :param admin_class:  管理类
    :param field:  字段对象
    :param form_obj:  表单对象
    :return:
    '''
    all_permissions = admin_class.model._meta.permissions
    field_obj = getattr(admin_class.model, field.name)
    all_obj_list = []
    for perm in all_permissions:  # 过滤掉django默认自带的权限，只提取Account表下自定义的权限
        obj = field_obj.rel.to.objects.get(codename=perm[0])
        all_obj_list.append(obj)

    # 单条数据的对象中的某个字段
    if form_obj.instance.id:
        obj_instance_field = getattr(form_obj.instance, field.name)
        selectd_obj_list = obj_instance_field.all()
    else:  # 代表这是在 创建新的一条记录
        return all_obj_list
    # 进行对已使用的数据过滤
    standby_obj_list = []
    for obj in all_obj_list:
        if obj not in selectd_obj_list:
            standby_obj_list.append(obj)
    return standby_obj_list


@register.simple_tag
def get_m2m_selectd_perm_list(form_obj, field):
    '''返回已经选中的M2M数据'''
    if form_obj.instance.id:  # 这里用于修改数据的复选框显示，添加数据没有M2M数据，所以不返回
        field_obj = getattr(form_obj.instance, field.name)
        return field_obj.all()


@register.simple_tag
def url_link(url_path):
    ''' 返回链接字串，如：aa > bb > cc'''
    li = '<ol class="breadcrumb">'
    url_str = ''
    url_list = url_path.strip('/').split('/')
    for url_name in url_list:
        if len(url_str) == 0:
            url_str = '/' + url_name
            li += '<li><a href="{link_url}">{link_name}</a></li>'.format(link_name=url_name, link_url='#')
        elif url_name == url_list[-1]:
            url_str += '/' + url_name
            li += '<li><a href="{link_url}" class="active">{link_name}</a></li>'.format(link_name=url_name,
                                                                                        link_url=url_str)
        else:
            url_str += '/' + url_name
            li += '<li><a href="{link_url}">{link_name}</a></li>'.format(link_name=url_name, link_url=url_str)
    li += '</ol>'
    return mark_safe(li)


@register.simple_tag
def err_info(field):
    '''
    动态返回表单每个字段的错误提示
    :param field: 字段对象
    :return:
    '''
    if field.errors:
        err_msg = json.loads(field.errors.as_json())
        return err_msg[0]['message']
    else:
        return ''


@register.simple_tag
def account_detail(field):
    '''
    获取当前登录账号的详细信息
    :param field: 字段对象
    :return:
    '''
    if type(field.field).__name__ in ['EmailField', 'ReadOnlyPasswordHashField', 'CharField']:
        return field.value()
    if type(field.field).__name__ == 'ModelMultipleChoiceField':
        ul_ele = "<ul class='list-unstyled list-group'>"
        for f in field.field.queryset:
            if f.id in field.value():
                ul_ele += '<li>%s</li>' % f.name
        ul_ele += "</ul>"
        return mark_safe(ul_ele)
