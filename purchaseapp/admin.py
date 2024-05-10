from django.contrib import admin
from .models import PurchaseOrderModel
from vendor_performanceapp.models import HistoricalPerformanceModel
from vendorapp.models import VendorModel
# Register your models here.

admin.site.register(PurchaseOrderModel)
admin.site.register(VendorModel)
admin.site.register(HistoricalPerformanceModel)