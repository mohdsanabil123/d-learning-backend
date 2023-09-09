from django.contrib import admin
from .models import News, UserAccount

from django.contrib.auth import get_user_model

User = get_user_model()

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display       = ('id', 'first_name','email','phone_number', 'address')
    list_display_links = ('id', 'first_name','email')

admin.site.register(User, UserAdmin)

admin.site.register(News)
admin.site.register(UserAccount)