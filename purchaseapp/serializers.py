from . models import PurchaseOrderModel
from rest_framework import serializers
# Serializers for PO

class PurchaseOrderSerializer(serializers.ModelSerializer):

    class Meta:
        model=PurchaseOrderModel
        fields='__all__'