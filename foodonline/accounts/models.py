from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin

# Create your models here.


class UserManager(BaseUserManager):
    def create_user(self,email,username,firstname,lastname,password=None):
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            firstname = firstname,
            lastname = lastname,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,username,firstname,lastname,password=None):
        pass



   