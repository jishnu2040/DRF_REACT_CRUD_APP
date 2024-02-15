from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin


# CustomUser Manager

class UserAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, email, password=None ):
        if not email:
            raise ValueError("Users must have an email address")
        
        email = self.normalize_email(email)
        email = email.lower()

        user = self.model(
            email=email,
            first_name = first_name,
            last_name = last_name
        )

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, first_name, last_name, email, password=None):
       
        user = self.create_user(
            first_name,
            last_name,
            email,
            password=password,
        
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

# Custom UserModel
    
class UserAccount(AbstractBaseUser, PermissionsMixin):# permisssonmixin are using to defind user is superuser or not
    first_name = models.CharField(max_length = 225)
    last_name = models.CharField(max_length = 225)
    email = models.EmailField(unique= True,max_length = 225)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserAccountManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['first_name', 'last_name']


    def __str__(self):
        return self.email   
