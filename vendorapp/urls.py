from django.urls import path
from . views import (
    CreateVendorViews,
    VendorListViews,
    RetrieveVendorViews, 
    UpdateVendorViews, 
    DeleteVendorViews,
    VendorPerformanceView,
    )
urlpatterns = [

    path('', CreateVendorViews.as_view(),name='create_vendor'),
    path('list/', VendorListViews.as_view(), name='list_of_all_vendors'),
    path('<int:pk>/', RetrieveVendorViews.as_view(), name='retrieve_vendors'),
    path('<int:pk>/update/', UpdateVendorViews.as_view(), name='update_vendors'),
    path('<int:pk>/delete/', DeleteVendorViews.as_view(), name='delete_vendors'),
    path('<int:vendor_id>/performance/', VendorPerformanceView.as_view(), name='vendor_performance'),
]
