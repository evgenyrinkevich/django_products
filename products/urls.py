from django.urls import path

from products.views import ProductListView, ProductCategoryListView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('category/<int:pk>/', ProductCategoryListView.as_view(), name='category'),
]
