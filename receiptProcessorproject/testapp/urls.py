from django.urls import path
from .views import submitReceipt,getReceiptPoints

urlpatterns=[
     path('receipts/process',submitReceipt,name='submitReceipt'), 
     path('receipts/<str:id>/points', getReceiptPoints, name='getReceiptPoints'),
    
]