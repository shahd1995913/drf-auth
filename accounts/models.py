from django.contrib.auth.models import AbstractUser

from django.db import models

class Account_Info(AbstractUser):  #Person



    address = models.CharField(max_length=100, blank=True, null=True)


    city = models.CharField(max_length=100, blank=True, null=True)

    email_account = models.EmailField(unique=True, max_length=100,verbose_name="Email Address Accunt")



    age = models.IntegerField(blank=True, null=True)


    USERNAME_FIELD = 'email_account'

    REQUIRED_FIELDS = ['full_name', 'username']

    class Meta:

        verbose_name = "Account_Info"

        verbose_name_plural = "accounts"

    def __str__(self) -> str:

        return self.email_account
