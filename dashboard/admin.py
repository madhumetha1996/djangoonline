from django.contrib import admin
from .models import Dashboard


class DashboardAdmin(admin.ModelAdmin):
    
    list_display = ['title', 'description']


admin.site.register(Dashboard, DashboardAdmin)
