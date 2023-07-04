from django.urls import path
from .views import ItemsList, ItemsDetail,PostList,PostDetail

urlpatterns = [
    path('', ItemsList.as_view(), name='items_list'),
    path('<int:pk>/', ItemsDetail.as_view(), name='item_detail'),
    path('post/', PostList.as_view(), name='post_list'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
]