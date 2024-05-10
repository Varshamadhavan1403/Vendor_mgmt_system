from rest_framework import generics
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . models import VendorModel
from . serializers import VendorModelSerializers, VendorPerformanceSerializer
# Create your views here.

# Views to create vendor
class CreateVendorViews(generics.CreateAPIView):
    queryset = VendorModel.objects.all()
    serializer_class = VendorModelSerializers

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({"message": "Vendor created successfully"}, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# views to list vendors
class VendorListViews(generics.ListAPIView):
    queryset=VendorModel.objects.all()
    serializer_class = VendorModelSerializers

    def list(self, request, *args, **kwargs):
        queryset=self.get_queryset()
        if not queryset.exists():
            return Response({"message" : "Vendors Does not exists"}, status=status.HTTP_404_NOT_FOUND)
        serializer=self.get_serializer(queryset, many=True)
        return Response(serializer.data)


# Views to retrieve specific vendors
class RetrieveVendorViews(generics.RetrieveAPIView):
    serializer_class = VendorModelSerializers
    queryset = VendorModel.objects.all()
    lookup_field = 'pk'

    def retrieve(self, request, *args, **kwargs):
        try:
            instance = VendorModel.objects.get(pk=self.kwargs['pk'])
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        except VendorModel.DoesNotExist:
            return Response({"message": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
   
       
# Views to update vendor details
class UpdateVendorViews(generics.UpdateAPIView):
    queryset=VendorModel.objects.all()
    serializer_class=VendorModelSerializers
    lookup_url_kwarg= 'pk'

    def get(self, request, pk):
        try:
            # Retrieve vendor object from database
            vendor = VendorModel.objects.get(pk=pk)
        except VendorModel.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the existing vendor data
        serializer = VendorModelSerializers(vendor)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        try:
            # Retrieve vendor object from database
            vendor = VendorModel.objects.get(pk=pk)
        except VendorModel.DoesNotExist:
            return Response({'error': 'Vendor not found'}, status=status.HTTP_404_NOT_FOUND)
        
        # Serialize the existing vendor data and pre-fill fields
        serializer = VendorModelSerializers(vendor, data=request.data)
        
        if serializer.is_valid():
            # Update and save the vendor object
            serializer.save()
            return Response({'success': 'Vendor details updated successfully'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Delete vendors
class DeleteVendorViews(generics.DestroyAPIView):
    queryset=VendorModel.objects.all()
    serializer_class=VendorModelSerializers
    lookup_url_kwarg='pk'

    def perform_destroy(self, instance):
        instance.delete()

    def destroy(self, request, *args,**kwargs):
        try:
            instance = VendorModel.objects.get(pk=self.kwargs['pk'])
            serializer = self.get_serializer(instance)
            self.perform_destroy(instance)

            return Response({"message":"Vendor details deleted successfully"}, status=status.HTTP_200_OK)
        except VendorModel.DoesNotExist:
            return Response({"message": "Vendor not found"}, status=status.HTTP_404_NOT_FOUND)
   
# Calculate Vendor performance
class VendorPerformanceView(APIView):
    def get(self, request, vendor_id):
        try:
            vendor = VendorModel.objects.get(id=vendor_id)
            serializer = VendorPerformanceSerializer(vendor)
            return Response(serializer.data)
        except VendorModel.DoesNotExist:
            return Response({"message": "Vendor not found."}, status=status.HTTP_404_NOT_FOUND)
        
