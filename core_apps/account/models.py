import uuid

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, Permission
from core_apps.account.managers import CustomUserManager


class USER_TYPE(models.IntegerChoices):
    ADMIN = 1, 'Admin'
    USER = 2, 'User'
    WORKER = 3, 'Worker'


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True
        ordering = ['created']


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    pkid = models.BigAutoField(primary_key=True, editable=False)
    id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=25, unique=True, blank=True)
    first_name = models.CharField(max_length=255, blank=True)
    last_name = models.CharField(max_length=255, blank=True)
    role = models.IntegerField(choices=USER_TYPE.choices, default=USER_TYPE.USER, db_index=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["first_name", "last_name", "phone"]
    objects = CustomUserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")
        ordering = ("-created",)

    def _str_(self):
        full_name = f'{self.first_name} {self.last_name}'.strip()
        return full_name if full_name else self.phone if self.phone else self.email
