from django.shortcuts import get_object_or_404
from django.utils import timezone
from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import PurchaseOrderModel
from . serializers import PurchaseOrderSerializer


# Create your views here.
# views to create PO
class CreatePurchaseOrderViews(generics.CreateAPIView):
    queryset=PurchaseOrderModel
    serializer_class=PurchaseOrderSerializer

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({"message": "Purchase Order created successfully"}, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views to list PO
class PurchaseOrderListAPIView(generics.ListAPIView):
    serializer_class = PurchaseOrderSerializer

    def get_queryset(self):
        queryset = PurchaseOrderModel.objects.all()
        vendor_id = self.request.query_params.get('vendor_id', None)
        if vendor_id:
            queryset = queryset.filter(vendor_id=vendor_id)
        return queryset
    

# views to retrieve details of a particular PO
class RetrievePurchaseOrderViews(generics.RetrieveAPIView):
    serializer_class=PurchaseOrderSerializer
    queryset=PurchaseOrderModel
    lookup_field='pk'
 

# Views to update PO
class UpdatePurchaseOrderViews(generics.UpdateAPIView):
    serializer_class=PurchaseOrderSerializer
    queryset=PurchaseOrderModel
    lookup_field='pk'

    def get_object(self):
        queryset = self.get_queryset()
        obj = generics.get_object_or_404(queryset, pk=self.kwargs.get('pk'))
        return obj


# Delete views to delete certain PO
class DeletePurchaseOrderViews(generics.DestroyAPIView):
    serializer_class=PurchaseOrderSerializer
    queryset=PurchaseOrderModel
    lookup_field='pk'


# views to update acknowledgement
class AcknowledgePurchaseOrder(APIView):
    def post(self, request, po_id):
        purchase_order = get_object_or_404(PurchaseOrderModel, pk=po_id)

        # Check if the purchase order is already acknowledged
        if purchase_order.acknowledgement_date:
            return Response({"error": "Purchase order is already acknowledged"}, status=status.HTTP_400_BAD_REQUEST)

        # Update acknowledgment date
        purchase_order.acknowledgement_date = timezone.now()
        purchase_order.save()

        # Trigger recalculation of average_response_time
        vendor = purchase_order.vendor
        vendor.calculate_average_response_time()

        return Response({"message": "Purchase order acknowledged successfully"}, status=status.HTTP_200_OK)