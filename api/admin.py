from django.contrib import admin
from django_admin_listfilter_dropdown.filters import DropdownFilter
# Register your models here.
from .models import Company, Employee


class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'location', 'type')
    search_fields = ('name',)
    list_filter = (('location',DropdownFilter),)

admin.site.register(Company, CompanyAdmin)
admin.site.register(Employee)
