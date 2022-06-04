from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from products.views import ProductListView, ProductCategoryListView

app_name = 'products'

urlpatterns = [
    path('', ProductListView.as_view(), name='index'),
    path('category/<int:pk>/', ProductCategoryListView.as_view(), name='category'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

