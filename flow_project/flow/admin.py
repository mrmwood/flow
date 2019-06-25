from django.contrib import admin
#from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser, Role, Teacher, Student, Product

#All imports are registered at the bottom of this files
#Don't forget to register any new imports






class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email',)
    list_filter = ('email',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Role)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(Product)
