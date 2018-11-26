#!/opt/python3/bin/python3
#Author: zhaoyong

from django import forms
from configCenter import models
from django.forms import ValidationError
from django.utils.translation import ugettext as _  # 国际化
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from configCenter import custom_admin
from django.urls import reverse  # 将匿名URL转换为URL绝对路径


class MenuLevel1Form(forms.ModelForm):
    def __new__(cls, *args, **kwargs):
        for field_name,field_obj in cls.base_fields.items():
            if not custom_admin.MenuLevel1Admin.is_add_form:  # 表示修改
                if field_name in custom_admin.MenuLevel1Admin.readonly_field:
                    field_obj.widget.attrs['disabled'] = 'disabled'
            else:  # 表示添加
                if field_obj.widget.__dict__['attrs'].get('disabled'):
                    del field_obj.widget.__dict__['attrs']['disabled']
            field_obj.widget.attrs['class'] = 'form-control'
            field_obj.widget.attrs['maxlength'] = getattr(field_obj, 'max_length') if hasattr(field_obj, 'max_length') else ""
        return forms.ModelForm.__new__(cls)

    class Meta:
        model = models.MenuLevel1
        fields = '__all__'

    def clean_url_name(self):
        url_name = self.cleaned_data['url_name']
        if self.cleaned_data['url_type'] == 0:
            try:
                reverse(url_name)
            except Exception as e:
                raise ValidationError(
                    _('添加的url name未在urls文件中配置，错误：%s' % e),
                    code='invalid',
                )
        return url_name


class MenuLevel2Form(forms.ModelForm):
    def __new__(cls, *args, **kwargs):
        for field_name,field_obj in cls.base_fields.items():
            if not custom_admin.MenuLevel2Admin.is_add_form:
                if field_name in custom_admin.MenuLevel2Admin.readonly_field:
                    field_obj.widget.attrs['disabled'] = 'disabled'
            else:
                if field_obj.widget.__dict__['attrs'].get('disabled'):
                    del field_obj.widget.__dict__['attrs']['disabled']
            field_obj.widget.attrs['class'] = 'form-control'
            field_obj.widget.attrs['maxlength'] = getattr(field_obj, 'max_length') if hasattr(field_obj, 'max_length') else ""
        return forms.ModelForm.__new__(cls)

    class Meta:
        model = models.MenuLevel2
        fields = '__all__'

    def clean_url_name(self):
        url_name = self.cleaned_data['url_name']
        try:
            reverse(url_name)
        except Exception as e:
            raise ValidationError(
                _('添加的url name未在urls文件中配置，错误：%s' % e),
                code='invalid',
            )
        return url_name


class RoleForm(forms.ModelForm):
    def __new__(cls, *args, **kwargs):
        for field_name,field_obj in cls.base_fields.items():
            if not custom_admin.RoleAdmin.is_add_form:
                if field_name in custom_admin.RoleAdmin.readonly_field:
                    field_obj.widget.attrs['disabled'] = 'disabled'
            else:
                if field_obj.widget.__dict__['attrs'].get('disabled'):
                    del field_obj.widget.__dict__['attrs']['disabled']
            field_obj.widget.attrs['class'] = 'form-control'
            field_obj.widget.attrs['maxlength'] = getattr(field_obj, 'max_length') if hasattr(field_obj, 'max_length') else ""
        return forms.ModelForm.__new__(cls)

    class Meta:
        model = models.Role
        fields = '__all__'


class AccountForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    def __new__(cls, *args, **kwargs):
        for field_name,field_obj in cls.base_fields.items():
            # 为字段添加属性
            field_obj.widget.attrs['class'] = 'form-control'
            field_obj.widget.attrs['maxlength'] = getattr(field_obj, 'max_length') if hasattr(field_obj, 'max_length') else ""
        return forms.ModelForm.__new__(cls)

    class Meta:
        model = models.Account
        fields = ['email','name','roles','user_permissions']

    def clean_password2(self):
        # Check that the two password entries match
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        # Save the provided password in hashed format
        user = super(AccountForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    """ 后台管理页面修改账号信息"""
    password = ReadOnlyPasswordHashField()

    def __new__(cls, *args, **kwargs):
        for field_name,field_obj in cls.base_fields.items():
            # 为字段添加属性
            if hasattr(custom_admin.AccountAdmin,'is_add_form'):
                if not custom_admin.AccountAdmin.is_add_form:
                    if field_name in custom_admin.AccountAdmin.readonly_field:
                        field_obj.widget.attrs['disabled'] = 'disabled'
                else:
                    if field_obj.widget.__dict__['attrs'].get('disabled'):
                        del field_obj.widget.__dict__['attrs']['disabled']
        return forms.ModelForm.__new__(cls)

    class Meta:
        model = models.Account
        fields = ('email','password','name','roles','user_permissions')

    def clean_password(self):
        # Regardless of what the user provides, return the initial value.
        # This is done here, rather than on the field, because the
        # field does not have access to the initial value
        return self.initial["password"]