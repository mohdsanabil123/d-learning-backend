from django.contrib import admin
from django.contrib.auth import get_user_model

User = get_user_model()

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name','email','phone_number', 'address')
    list_display_links = ('first_name','email')

admin.site.register(User, UserAdmin)