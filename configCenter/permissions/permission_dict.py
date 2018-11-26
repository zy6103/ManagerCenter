#!/opt/python3/bin/python3
# Author: zhaoyong
# 权限对比原始字典
# url_type = 0  表示当前URL标记为相对路径，也就是匿名，视图中name定义的名称
# url_type = 1  表示当前URL标记为绝对路径。

perm_dict = {
    'menuLv1_index_get': {
        'url_type': 0,
        'url': 'menuLv1_index',
        'method': ['GET'],
        'args': []
    },
    'menuLv2_index_get': {
        'url_type': 0,
        'url': 'menuLv2_index',
        'method': ['GET'],
        'args': []
    },
    'role_index_get': {
        'url_type': 0,
        'url': 'role_index',
        'method': ['GET'],
        'args': []
    },
    'account_index_get': {
        'url_type': 0,
        'url': 'account_index',
        'method': ['GET'],
        'args': []
    },

    'menuLv1_add_all': {
        'url_type': 0,
        'url': 'menuLv1_add',
        'method': ['GET', 'POST'],
        'args': []
    },
    'menuLv1_change_all': {
        'url_type': 0,
        'url': 'menuLv1_change',
        'method': ['GET', 'POST'],
        'args': []
    },
    'menuLv2_add_all': {
        'url_type': 0,
        'url': 'menuLv2_add',
        'method': ['GET', 'POST'],
        'args': []
    },
    'menuLv2_change_all': {
        'url_type': 0,
        'url': 'menuLv2_change',
        'method': ['GET', 'POST'],
        'args': []
    },
    'role_add_all': {
        'url_type': 0,
        'url': 'role_add',
        'method': ['GET', 'POST'],
        'args': []
    },
    'role_change_all': {
        'url_type': 0,
        'url': 'role_change',
        'method': ['GET', 'POST'],
        'args': []
    },
    'account_add_all': {
        'url_type': 0,
        'url': 'account_add',
        'method': ['GET', 'POST'],
        'args': []
    },
    'account_change_all': {
        'url_type': 0,
        'url': 'account_change',
        'method': ['GET', 'POST'],
        'args': []
    },
    'delete_obj_post': {
        'url_type': 0,
        'url': 'delete_obj',
        'method': ['POST'],
        'args': []
    },
    'reset_password_post': {
        'url_type': 0,
        'url': 'reset_password',
        'method': ['POST'],
        'args': []
    },
}
