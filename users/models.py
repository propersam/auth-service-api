from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class UserProfileManager(BaseUserManager):
    """ Helps django work with the custom user model below """
    def create_user(self, email, username, password=None, firstName, lastName):
        """ Creates a new User Profile object """
        
        # check that email was provided
        if not email:
            raise ValueError("Users must have an Email address")
        
        email = self.normalize_email(email)
        user = self.model(email=email, username=username,
         firstName=firstName, lastName=lastName)

        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, username, password, firstName, lastName):
        """ Create and saves a new superuser with the given details """

        user = self.create_user(email, username, password, firstName, lastName)

        user.is_superuser = True
        user.is_staff = True
        
        user.save(using=self._db)

        return user



class UserProfile(AbstractBaseUser, PermissionsMixin):
    """
      Add Additional fields for users here
    """
    firstName = models.CharField('User First Name', max_length=50)
    lastName = models.CharField('User Last Name', max_length=50)
    username = models.CharField("User's login username", max_length=50)
    email = models.EmailField("User Email", max_length=125, unique=True)
    # organisation = models.ForeignKey(Organisation, related_name='The User Organisation',on_delete=models.CASCADE)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def get_full_name(self):
        """
         Used to get a users full name. 
        """
        return self.firstName+' '+self.lastName

    def get_short_name(self):
        """ Used to GEt a user's username """

        return self.username

    def __str__(self):
        """ This is used to represent the object as a string """
        return self.email


class Organisation(models.Model):
    """
     Model containing User Organisation
    """
    name = models.CharField('name of organisation', max_length=255, unique=True)
    size = models.IntegerField('Organisation Size', max_length=6)
    address = models.TextField('Organisation Address Location')


# class Role(models.Model):
#     """ 
#       Model containing all different roles of any user
#     """
#     name = models.CharField('role name', max_length=50)
#     desc = models.TextField('Role Description')
#     created_at = models.DateTimeField(auto_now_add=True)

