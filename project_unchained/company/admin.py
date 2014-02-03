from django.contrib import admin
from company.models import Company

class CompanyAdmin(admin.ModelAdmin):
    fields = ['name', 'www', 'admin', 'public']

admin.site.register(Company, CompanyAdmin)
