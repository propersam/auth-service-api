from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create your models here.

class Organisation(models.Model):
	"""
	 Model containing User Organisation
	"""
	SIZE_CHOICES=(
		(1, '1 to 10'),
		(2, '11 to 50'),
		(3, '50 and Above')
	)
	name = models.CharField('Name of Organisation', max_length=255, unique=True)
	size = models.IntegerField('Organisation Size', choices=SIZE_CHOICES)
	address = models.TextField('Organisation Address Location', null=True, blank=True)
	logo = models.ImageField('Upload Organisation Logo', upload_to='logos', null=True, blank=True)
	email = models.EmailField('Company email Address', blank=True, unique=True)
	website = models.CharField('website of the Company',max_length=50, blank=True, null=True)
	about_company = models.TextField('Short Description About Company', blank=True, null=True)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class Role(models.Model):
	""" 
	  Model containing all different roles of any user
	"""
	name = models.CharField('Role name', max_length=50, unique=True)
	desc = models.TextField('Role Description')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


class UserProfileManager(BaseUserManager):

	use_in_migrations = True 

	""" Helps django work with the custom user model below """
	def create_user(self, email, username, password=None):
		""" Creates a new User Profile object """
		
		# check that email was provided
		if not email:
			raise ValueError("Users must have an Email address")
		
		email = self.normalize_email(email)
		user = self.model(email=email, username=username)

		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, email, username, password):
		""" Create and saves a new superuser with the given details """

		user = self.create_user(email, username, password)

		user.is_superuser = True
		user.is_staff = True

		user.save(using=self._db)

		return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
	"""
	  Add Additional fields for users here
	"""
	# sys_id = models.AutoField(primary_key=True, blank=True)
	firstName = models.CharField('User First Name', max_length=50)
	lastName = models.CharField('User Last Name', max_length=50)
	username = models.CharField("User's login username", max_length=50)
	email = models.EmailField("User Email", max_length=125, unique=True, blank=False, null=False)
	organisation = models.ForeignKey(Organisation, related_name='user_organisation', on_delete=models.CASCADE, blank=True, null=True)
	roles = models.ManyToManyField(Role, related_name='user')
	contact_num = models.CharField("User's phone number", max_length=17, null=True, blank=True)
	profile_pics = models.ImageField("Upload User's Profile Picture", upload_to='profile_pics/%Y/%m/%d', null=True, blank=True)

	is_active = models.BooleanField(default=True)
	is_staff = models.BooleanField(default=False)

	objects = UserProfileManager()

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username']

	class Meta:
		app_label = "users"
		db_table = "users"

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

	def has_perm(self, perm, obj=None):
		return self.is_staff

	def has_module_perms(self, app_label):
		return self.is_staff



