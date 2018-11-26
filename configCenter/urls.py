"""ManagerCenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from configCenter import views


urlpatterns = [
    url(r'^menulevel1/$', views.menuLv1, name='menuLv1_index'),
    url(r'^menulevel1/add/$', views.menuLv1_add, name='menuLv1_add'),
    url(r'^menulevel1/(\d+)/change/$', views.menuLv1_change, name='menuLv1_change'),
    url(r'^menulevel2/$', views.menuLv2, name='menuLv2_index'),
    url(r'^menulevel2/add/$', views.menuLv2_add, name='menuLv2_add'),
    url(r'^menulevel2/(\d+)/change/$', views.menuLv2_change, name='menuLv2_change'),
    url(r'^role/$', views.role_index, name='role_index'),
    url(r'^role/add/$', views.role_add, name='role_add'),
    url(r'^role/(\d+)/change/$', views.role_change, name='role_change'),
    url(r'^account/$', views.account_index, name='account_index'),
    url(r'^account/add/$', views.account_add, name='account_add'),
    url(r'^account/(\d+)/change/$', views.account_change, name='account_change'),
    url(r'^(\w+)/delete/$', views.delete_obj, name='delete_obj'),
    url(r'^account/(\d+)/reset_password/$', views.reset_password, name='reset_password'),
    url(r'^(\w+)/(\d+)/$', views.not_found),
]