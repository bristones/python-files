from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from .managers import CustomUserManager
from django.utils.translation import ugettext_lazy as _

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email Address'), unique= True)
    username = models.CharField(_('Username'), unique= True, max_length=50)
    first_name = models.CharField(_('First Name'), blank= True, max_length=50)
    last_name = models.EmailField(_('Last Name'), blank= True, max_length=50)
    mobile_number = models.CharField(_('Mobile Number'), blank= True, max_length=50)
    pin  = models.IntegerField(_('PIN Number'), default=0)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ('email',)
    
    objects = CustomUserManager()
    
    #helper functions
    # eg creating user functions/retrieving user & permissions
    
    def _str_(self):
        return self.email
    
    class Meta:
        verbose_name_plural = 'Users'