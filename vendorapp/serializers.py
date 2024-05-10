from rest_framework import serializers
from . models import VendorModel

# serializer for Vendor model details
class VendorModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = VendorModel
        fields='__all__'

# Serializer to calculate performance metrics of PO
class VendorPerformanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = VendorModel
        fields = ['on_time_delivery_rate','quality_rating_avg','average_response_time','fulfillment_rate']