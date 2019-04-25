from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager



class CustomAuthenticationBackend:

    def authenticate(self, request, email_or_phone=None, password=None):
        try:
             user = User.objects.get(
                 Q(email=email_or_phone) | Q(phone=email_or_phone)
             )
             pwd_valid = user.check_password(password)
             if pwd_valid:            
                 return user
             return None
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None


class CustomUserManager(UserManager):
    pass

class CustomUser(AbstractUser):
    objects = CustomUserManager()
# from django.contrib.auth.models import PermissionsMixin
# from django.contrib.auth.base_user import AbstractBaseUser
# from django.contrib.auth.models import AbstractUser
# from django.utils.translation import ugettext_lazy as _

# class UserDetails(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(_('email'), max_length=30,unique=True,blank=False)
#     phoneNo = models.CharField(_('phoneNo'), max_length=10, blank=False, unique=True)
#     password = models.CharField(_('password'), max_length=5,blank=False)

#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ["password"]

#     # class Meta:
#     #     verbose_name = _('user')
#     #     verbose_name_plural = _('users')