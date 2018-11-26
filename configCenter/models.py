from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, PermissionsMixin, AbstractBaseUser
)


# Create your models here.

class AccountManager(BaseUserManager):
    def create_user(self, email, name, password=None):
        """
        创建普通账号
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
            name=name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, name, password):
        """
        建管理员账号
        """
        user = self.create_user(
            email,
            password=password,
            name=name,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    name = models.CharField(max_length=32)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    roles = models.ManyToManyField('Role', blank=True)

    objects = AccountManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        #     "Does the user have a specific permissions?"
        #     # Simplest possible answer: Yes, always
        if self.is_admin:
            # print('我是管理员')
            return True
        else:
            # 不是管理员
            app_name = self._meta.app_label
            for db_perm in self.get_all_permissions():
                if '%s.%s' % (app_name, perm) == db_perm:
                    return True
            return False

    #
    def has_module_perms(self, app_label):
        if self.is_admin:
            # print('我是管理员')
            return True
        else:
            return False

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_active

    class Meta:
        verbose_name = '账号表'
        verbose_name_plural = verbose_name
        permissions = (
            ('menuLv1_index_get', '配置中心一级索引页面'),
            ('menuLv2_index_get', '配置中心二级索引页面'),
            ('role_index_get', '配置中心角色索引页面'),
            ('account_index_get', '配置中心账号索引页面'),
            ('menuLv1_add_all', '配置中心一级菜单添加页面'),
            ('menuLv1_change_all', '配置中心一级菜单修改页面'),
            ('menuLv2_add_all', '配置中心二级菜单添加页面'),
            ('menuLv2_change_all', '配置中心二级菜单修改页面'),
            ('role_add_all', '配置中心角色添加页面'),
            ('role_change_all', '配置中心角色修改页面'),
            ('account_add_all', '配置中心账号添加页面'),
            ('account_change_all', '配置中心账号修改页面'),
            ('delete_obj_post', '配置中心删除提交页面'),
            ('reset_password_post', '配置中心账号密码修改提交页面'),
        )


class Role(models.Model):
    ''' 角色表 '''
    name = models.CharField(max_length=32, unique=True)
    menu_level1 = models.ManyToManyField('MenuLevel1', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '角色表'
        verbose_name_plural = '角色表'


class MenuLevel1(models.Model):
    '''一级菜单'''
    name = models.CharField(max_length=32, unique=True)
    url_type_choices = ((0, 'alias'), (1, 'absolute_url'))
    url_type = models.SmallIntegerField(choices=url_type_choices, default=0,
                                        help_text='注意：当一级菜单内包含二级菜单时，添加一级菜单要用absolute_url，url_name使用：#')
    url_name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '一级菜单表'
        verbose_name_plural = verbose_name


class MenuLevel2(models.Model):
    '''二级菜单'''
    name = models.CharField(max_length=32, unique=True)
    url_name = models.CharField(max_length=64, unique=True)
    level2_to_level1 = models.ForeignKey('MenuLevel1')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '二级菜单表'
        verbose_name_plural = verbose_name
