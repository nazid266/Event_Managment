from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from event_users.models import CustomUser

# Register your models here.

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    model=CustomUser
    fieldsets=(
        (None,{'fields':('username','password')}),
        ('Personal Info',{'fields' :('first_name','last_name','email','bio','profile_image')}),
        ('Permission',{'fields' :('is_active','is_staff','is_superuser','groups','user_permissions')}),
        ('Importants Dates',{'fields' :('last_login','date_joined')})
    )
    
    add_fieldsets=(
        (None,{
            'classes':('wide',),
            'fields':('username','password1','password2','email','bio','profile_image')
        }),
    )
    
    list_display=('username','first_name','last_name','is_staff')
    search_fields=('username','email','first_name','last_name')
    ordering=('-username',)