from django.contrib import admin
from .models import BusinessPlan


class BusinesPlanModelAdmin(admin.ModelAdmin):
    list_display = ['id','business_name','email']
    search_fields = ['id','business_name']


admin.site.register(BusinessPlan,BusinesPlanModelAdmin)

