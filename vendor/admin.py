from django.contrib import admin
from .models import Vendor

# Register your models here.z
class VendorAdmin(admin.ModelAdmin):
    list_display = ('user', 'vendor_name', 'is_approved', 'created_at')
    list_display_links = ('user', 'vendor_name') 

admin.site.register(Vendor, VendorAdmin)