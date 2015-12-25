from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class AccountManager(BaseUserManager):
    def create_user(self,email,password = None,**kwargs):
        if not email:
            raise ValueError('Users must have a valid email.')

        if not kwargs.get('username'):
			raise ValueError('Users must have a valid username.')

        account = self.model(email=self.normalize_email(email), username=kwargs.get('username'))

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self,email,password,**kwargs):
        account = self.create_user(email, password, **kwargs)

        account.is_admin = True
        account.save()

        return account





class Account(AbstractBaseUser):
    email = models.EmailField(unique = True)
    username = models.CharField(max_length = 100, unique = True)
    is_admin = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    objects = AccountManager()

    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = ['username']
    
    @property
    def is_superuser(self):
        return self.is_admin

    @property
    def is_staff(self):
        return self.is_admin


    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin



    def __unicode__(self):
        return self.username


    def get_full_name(self):
        return self.username

    def get_short_name(self):
        return self.username

