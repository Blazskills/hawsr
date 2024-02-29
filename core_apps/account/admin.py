from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy as _

from .forms import CustomUserCreationForm

# from .forms import UserChangeForm, UserCreationForm
from .models import User


class UserAdmin(BaseUserAdmin):

    list_display = (
        "pkid",
        "id",
        "email",
        "phone",
        "role",
        "first_name",
        "last_name",
        "is_staff",
        "is_active",
        "created",
    )

    list_display_links = [
        "pkid",
        "id",
        "email",
        "phone",
    ]

    list_filter = ["is_staff", "is_active"]

    fieldsets = (
        (_("Login Credentials"), {"fields": ("email", "password")}),
        (
            _("Personal Info"),
            {
                "fields": (
                    "first_name",
                    "last_name",
                    "phone",
                    "role",
                )
            },
        ),
        (
            _("Permissions and Groups"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                )
            },
        ),
        (_("Important Dates"), {"fields": ("last_login",)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'phone'),
        }),
    )
    search_fields = ["email", "first_name", "last_name", "id"]
    ordering = ("-created",)
    model = User


admin.site.register(User, UserAdmin)
