from django.db import models
from vendorapp.models import VendorModel
# Create your models here.

# Models to calculate performance of vendors
class HistoricalPerformanceModel(models.Model):
    vendor = models.ForeignKey(VendorModel, on_delete=models.CASCADE)
    date=models.DateTimeField()
    on_time_delivery_rate=models.FloatField()
    quality_rating_avg=models.FloatField()
    average_response_time=models.FloatField()
    fulfillment_rate=models.FloatField()

    def __str__(self):
        return f"{self.vendor.name} - {self.date}"
    

