from django.contrib import admin
from django import forms
from django.contrib.auth.admin import UserAdmin
from .models import User,User_type,AddressInfo,PersonalInfo

from  django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Register your models here.


		






admin.site.register(User)
admin.site.register(User_type)
admin.site.register(AddressInfo)
admin.site.register(PersonalInfo)

#admin.site.register(User_type,UserTypeAdmin)
#admin.site.register(Student,StudentAdmin)
