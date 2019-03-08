from django import forms
from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField

from . import models

# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.Role)
admin.site.register(models.Organisation)