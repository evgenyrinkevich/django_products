from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.base import ContextMixin

from products.models import Product


class TitlePageMixin(ContextMixin):
    title = ''

    def get_context_data(self, **kwargs):
        context = super(TitlePageMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        return context


class ProductListView(TitlePageMixin, ListView):
    model = Product
    title = 'products'
    template_name = 'goods_list.html'
    queryset = Product.objects.all()
