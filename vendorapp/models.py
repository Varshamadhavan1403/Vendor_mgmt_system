from django.db import models
from django.utils import timezone
from django.db.models import Avg

# Create your models here.
# Models to for vendor details
class VendorModel(models.Model):
    name = models.CharField(max_length = 255)
    contact_details = models.TextField()
    address = models.TextField()
    vendor_code = models.CharField(max_length=100, unique = True, verbose_name = "Vendor Code")
    on_time_delivery_rate = models.FloatField(default=0)
    quality_rating_avg = models.FloatField()
    average_response_time = models.FloatField()
    fulfillment_rate = models.FloatField()

#   Calculates on_time_delivery_date 
    def calculate_on_time_delivery_rate(self):
        completed_orders = self.purchase_orders.filter(status='completed')
        total_completed_orders = completed_orders.count()
        if total_completed_orders > 0:
            on_time_delivered_orders = completed_orders.filter(delivery_date__lte=timezone.now())
            on_time_delivery_rate = (on_time_delivered_orders.count() / total_completed_orders) * 100
            self.on_time_delivery_rate = on_time_delivery_rate
            self.save()

    #   Calculates quality_rating_avg 

    def calculate_quality_rating_avg(self):
        completed_orders = self.purchase_orders.filter(status='completed').exclude(quality_rating=None)
        if completed_orders.exists():
            avg_quality_rating = completed_orders.aggregate(avg_quality_rating=models.Avg('quality_rating'))['avg_quality_rating']
            self.quality_rating_avg = avg_quality_rating
        else:
            self.quality_rating_avg = 0
        self.save()
   
#    calculates average response time
    def calculate_average_response_time(self):
        completed_orders = self.purchase_orders.filter(status='completed', acknowledgement_date__isnull=False)
        if completed_orders.exists():
            total_response_time_seconds = sum((order.acknowledgement_date - order.issue_date).total_seconds() for order in completed_orders)
            avg_response_time = total_response_time_seconds / completed_orders.count()
            self.average_response_time = avg_response_time
        else:
            self.average_response_time = 0
        self.save()

# calculates fulfillment rate of PO
    def calculate_fulfillment_rate(self):
        total_orders = self.purchase_orders.count()
        if total_orders > 0:
            fulfilled_orders = self.purchase_orders.filter(status='completed')
            fulfillment_rate = (fulfilled_orders.count() / total_orders) * 100
            self.fulfillment_rate = fulfillment_rate
        else:
            self.fulfillment_rate = 0
        self.save()

    def __str__(self):
        return self.name


