from django.contrib import admin

from core_apps.hawsr.models import Building, Company, Office, UserOffice, Worker

# Register your models here.


@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    list_display = ("id", "user", "worker_type", "is_busy", "created")
    list_per_page = 500


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "phone", "created")
    list_per_page = 500


@admin.register(Building)
class BuildingAdmin(admin.ModelAdmin):
    list_display = ("id", "company", "name", "floor_count", "created")
    list_per_page = 500


@admin.register(Office)
class OfficeAdmin(admin.ModelAdmin):
    list_display = ("id", "building", "floor", "number", "created")
    list_per_page = 500


@admin.register(UserOffice)
class UserOfficeAdmin(admin.ModelAdmin):
    list_display = ("id", "office", "user", "created")
    list_per_page = 500
