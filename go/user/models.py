from django.core.validators import RegexValidator
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self, phone_number, password=None, **extra_fields):
        if not phone_number:
            raise ValueError("Не указан номер телефона")
        user = self.model(phone_number=phone_number, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, phone_number, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("username", 'admin')
        return self.create_user(phone_number, password, **extra_fields)


class User(AbstractUser):
    phone_number = models.CharField(
        max_length=15,
        unique=True,
        validators=[RegexValidator(regex=r"^\+?1?\d{8,15}$")]
    )

    USERNAME_FIELD = "phone_number"
    REQUIRED_FIELDS = ['email']

    objects = CustomUserManager()

