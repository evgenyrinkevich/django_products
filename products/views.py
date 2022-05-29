from django.views.generic import ListView
from django.views.generic.base import ContextMixin

from products.models import Product, Category


class PageContextMixin(ContextMixin):
    title = ''
    categories = Category.objects.all()

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
    queryset = Product.objects.prefetch_related('category').all()


class ProductCategoryListView(PageContextMixin, ListView):
    model = Product
    title = 'products'
    template_name = 'products_category.html'
    ordering = ['-receipt_date']

    def get_queryset(self):
        category_pk = self.kwargs.get('pk')
        self.title = Category.objects.filter(id=category_pk).first().name
        if category_pk:
            return Product.objects.filter(category__in=[category_pk])
        else:
            return Product.objects.all()

