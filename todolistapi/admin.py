from django.contrib import admin
from .models import DoTitle,DoList,DoComment
# Register your models here.

admin.site.register(DoTitle)
admin.site.register(DoList)
admin.site.register(DoComment)