from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import MainUser, Account


class UserAdmin(UserAdmin):
    list_display = ('email',)
    search_fields = ('email',)
    ordering = ('-created',)
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )
    fieldsets = ()
    filter_horizontal = ()
    list_filter = ()


admin.site.register(MainUser, UserAdmin)
admin.site.register(Account, admin.ModelAdmin)
