from django.db import models
from vendorapp.models import VendorModel
# Create your models here.

# models for PO
class PurchaseOrderModel(models.Model):
    STATUS_CHOICES=(
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled')
    )
    po_number = models.CharField(max_length=100, unique = True, verbose_name = "Purchase Order Number")
    vendor = models.ForeignKey(VendorModel, on_delete = models.CASCADE, verbose_name="Vendor", related_name="purchase_orders")
    order_date = models.DateTimeField()
    delivery_date = models.DateTimeField()
    items = models.JSONField()
    quantity = models.IntegerField()
    status = models.CharField(max_length = 100, choices=STATUS_CHOICES, default='pending')
    quality_rating = models.FloatField(null=True, blank=True )
    issue_date=models.DateTimeField(null=True, blank=True)
    acknowledgement_date = models.DateTimeField(null = True, blank=True)

    def __str__(self):
        return self.vendor.name +" "+ self.po_number
