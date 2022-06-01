from django.contrib.sites.shortcuts import get_current_site
from django.views.generic import ListView
from django.views.generic.base import ContextMixin

from products.models import Product, Category


class PageContextMixin(ContextMixin):
    title = ''
    categories = Category.on_site.all()

    def get_context_data(self, **kwargs):
        context = super(PageContextMixin, self).get_context_data(**kwargs)
        context['title'] = self.title
        context['categories'] = self.categories
        return context


class ProductListView(PageContextMixin, ListView):
    model = Product
    title = 'products'
    template_name = 'goods_list.html'
    ordering = ['-receipt_date']
    queryset = Product.on_site.prefetch_related('category').all()


class ProductCategoryListView(PageContextMixin, ListView):
    model = Product
    title = 'products'
    template_name = 'products_category.html'
    ordering = ['-receipt_date']

    def get_queryset(self):
        category_pk = self.kwargs.get('pk')
        self.title = Category.on_site.filter(id=category_pk).first().name
        if category_pk:
            return Product.on_site.filter(category__in=[category_pk])
        else:
            return Product.on_site.all()

