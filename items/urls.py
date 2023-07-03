from django.urls import path
from .views import ItemsList, ItemsDetail

urlpatterns = [
    path('', ItemsList.as_view(), name='items_list'),
    path('/<int:pk>/', ItemsDetail.as_view(), name='item_detail'),
]