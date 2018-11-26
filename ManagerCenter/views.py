from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, redirect
from configCenter import models, forms
from utils import logger
from utils.utils import ResponseLog

# Create your views here.
log = logger.Logger()
response_result = ResponseLog()


@login_required()
def index(request):
    log.info('account %s login finish' % request.user)
    return render(request, 'index.html')


@login_required()
def change_password(request):
    if request.method == 'POST':
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if len(password1) <= 6 or len(password2) <= 6:
            response_result.status = 0
            response_result.error = '密码长度不可以小于6位'
        elif password1 == password2:
            request.user.set_password(password1)
            log.info('account %s change password finish' % request.user)
            response_result.status = 1
            response_result.message = '账号：%s 密码变更成功' % (request.user.email)
        else:
            response_result.status = 0
            response_result.error = '账号：%s 密码变更失败，2次密码不匹配' % (request.user.email)
        return JsonResponse(response_result.__dict__)


def account_detail(request):
    obj = models.Account.objects.get(id=request.user.id)
    form_obj = forms.UserChangeForm(instance=obj)
    return render(request, 'account_detail.html', {'form_obj': form_obj})


def acc_login(request):
    errors = {}
    if request.method == 'POST':
        _email = request.POST.get('logname')
        _pwd = request.POST.get('passwd')
        account = authenticate(username=_email, password=_pwd)
        if account:
            login(request, account)
            log.info('account %s logging' % request.user)
            next_url = request.GET.get('next', '/')
            return redirect(next_url)
        else:
            errors['error'] = '用户名或密码错误!'
            log.error('account %s login Faild' % _email)
    return render(request, 'login.html', {'errors': errors})


def acc_logout(request):
    log.info('account %s logout' % request.user)
    logout(request)
    return redirect('/accounts/login')
