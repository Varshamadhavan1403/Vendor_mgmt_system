from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import PurchaseOrderModel

# Signals to trigger the status and based on this calculates performance metrics
@receiver(post_save, sender=PurchaseOrderModel)
def update_vendor_metrics(sender, instance, created, **kwargs):
    if not created:
        vendor = instance.vendor
        vendor.calculate_on_time_delivery_rate()
        vendor.calculate_quality_rating_avg()
        vendor.calculate_average_response_time()
        vendor.calculate_fulfillment_rate()
