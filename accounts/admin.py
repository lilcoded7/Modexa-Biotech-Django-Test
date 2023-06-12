from django.contrib import admin
from accounts.models import CustomUser


# Register your models here.
admin.site.site_header = 'Biomedical Admin'
admin.site.site_title = 'Biomedical Admin'



class CustomUserAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'phone']


admin.site.register(CustomUser, CustomUserAdmin)