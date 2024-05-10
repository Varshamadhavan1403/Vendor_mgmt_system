from django.urls import path
from . views import (
    CreatePurchaseOrderViews, 
    # ListPurchaseOrderViews,
    PurchaseOrderListAPIView, 
    RetrievePurchaseOrderViews, 
    UpdatePurchaseOrderViews,
    DeletePurchaseOrderViews,
    AcknowledgePurchaseOrder)


urlpatterns = [
    path('', CreatePurchaseOrderViews.as_view(), name="purchase_orders"),
    path('list/', PurchaseOrderListAPIView.as_view(), name='purchase_order_list'),
    path('retrieve/<int:pk>/', RetrievePurchaseOrderViews.as_view(), name="retreive_purchase_orders"),
    path('put/<int:pk>/', UpdatePurchaseOrderViews.as_view(), name='update_purchase_order'),
    path('delete/<int:pk>/', DeletePurchaseOrderViews.as_view(), name='update_purchase_order'),
    path('<int:po_id>/acknowledge/', AcknowledgePurchaseOrder.as_view(), name='acknowledge_purchase_order'),

]