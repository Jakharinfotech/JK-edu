from django.db import models
from django.contrib.auth.models import AbstractUser
#from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

# Create your models here.
class User_type(models.Model):
    user_type = models.CharField(max_length=50)

    def __str__(self):
        return self.user_type


class User(AbstractUser):
    email    = models.EmailField(verbose_name='email',max_length=60,unique=True)
    username = models.CharField(max_length=30, unique=True)
    mobile = models.CharField(max_length=30, unique=True)
    user_type = models.ForeignKey(User_type,on_delete=models.CASCADE,null=True,blank=True)
    date_joined = models.DateTimeField(verbose_name='date joined', default= timezone.now)
    last_login  = models.DateTimeField(verbose_name='last login',default= timezone.now)
    
    



    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email


class PersonalInfo(models.Model):
    user = user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to ='myapp/img',null=True,blank=True)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=10,null=True,blank=True)

    



class AddressInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=150, blank=True,null=True)
    city = models.CharField(max_length=30,null=True,blank=True)
    state = models.CharField(max_length=30,null=True,blank=True)
    country = models.CharField(max_length=30,null=True,blank=True)
    zipcode = models.CharField(max_length=30,null=True,blank=True)

    










"""class User(AbstractUser):
	
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)
    is_company = models.BooleanField(default=False)
    is_institute = models.BooleanField(default=False) 
    is_exam_manager = models.BooleanField(default=False)
    is_company_manager = models.BooleanField(default=False)
    is_institute_manager = models.BooleanField(default=False)


class Student(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
	city = models.TextField(max_length=50, blank=True) 
class AutoDateTimeField(models.DateTimeField):
    def pre_save(self, model_instance, add):
        return timezone.now()

class MyAccountManager(BaseUserManager):
	def create_user(self,email,username,password=None):
		if not email:
			raise ValueError("User must have an email")
		if not username:
			raise ValueError("User must have username")

		user = self.model(
			   email = self.normalize_email(email),
			   username=username,
			)


		user.set_password(password)

		user.save(using=self._db)
		return user


	def create_superuser(self,email,username,password):
		if not email:
			raise ValueError("User must have an email")
		if not username :
			raise ValueError("User must have a username")
		if not password:
			raise ValueError("User must have a password")

		user = self.model(
				email = self.normalize_email(email),
				username=username,
				password=password
			)
		user.set_password(password)
		user.is_admin = True
		user.is_staff = True
		user.is_superuser = True
		user.save(using=self._db)
		return user


class User(AbstractBaseUser):
	email 				= models.EmailField(verbose_name='email',max_length=60,unique=True)
	username 			= models.CharField(max_length=30, unique=True)
	date_joined 		= models.DateTimeField(verbose_name='date joined', default= timezone.now)
	last_login  		= models.DateTimeField(verbose_name='last login',default= timezone.now)
	is_admin    		= models.BooleanField(default=False)
	is_active   		= models.BooleanField(default=False)
	is_staff    		= models.BooleanField(default=False)
	is_superuser		= models.BooleanField(default=False)
	is_student 			= models.BooleanField(default=False)
	is_teacher 			= models.BooleanField(default=False)
	is_company 			= models.BooleanField(default=False)
	is_institute 		= models.BooleanField(default=False)
	is_exam_manager 	= models.BooleanField(default=False)
	is_company_manager 	= models.BooleanField(default=False)
	is_institute_manager = models.BooleanField(default=False)



	USERNAME_FIELD = 'email'
	REQUIRED_FIELD = ['username','email']	

	objects = MyAccountManager()

	def __str__(self):
		return self.email

	def has_perm(self, perm,obj=None):
		return self.is_admin	

	def has_module_perms(self, app_label):
		return True"""


"""class User_type(models.Model):
	user_type = models.CharField(max_length=30, unique=True,null=True,blank=True)

	def __str__(self):
		return self.user_type

class User(User):
	username = models.CharField(max_length=30,unique=True)
	email = models.EmailField(max_length=60,unique=True)
	user_type = models.ForeignKey('myapp.User_type',on_delete=models.CASCADE,null=True,blank=True)
	#mobile = models.CharField(max_length=30,null=True, blank=True)

	USERNAME_FIELD = 'email'
	REQUIRED_FIELDS = ['username',]

	def __str__(self):
		return self.email"""




		


