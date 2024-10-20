from django.urls import path
from .views import ItemList, ItemDetails

urlpatterns = [
    path("items/", ItemList.as_view(), name='item-list'),
    path("items/<int:pk>/", ItemDetails.as_view(), name='item-details')
]
