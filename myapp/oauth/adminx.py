# _*_ coding: utf-8 _*_
import xadmin
from django.contrib import admin
# Register your models here.
from .models import OAuthUser


class OAuthUserAdmin:
    list_display = ('id', 'author', 'nikename', 'type', 'picture', 'email',)
    list_display_links = ('id', 'nikename')
    list_filter = ('author', 'type',)

xadmin.site.register(OAuthUser, OAuthUserAdmin)