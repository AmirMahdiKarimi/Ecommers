from django.shortcuts import get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Category, Product, Image

class ProductListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = "index.html"

    def get_queryset(self):
        products = Product.objects.all().order_by('-created_at')
        for product in products:
            product.main_image = Image.objects.filter(product=product).first()

        return products

class CategoryListView(ListView):
    model = Category
    context_object_name = 'categories'
    queryset = Category.objects.all()
    template_name = 'pages/collection.html'

class SelectedCategoryListView(ListView):
    model = Product
    context_object_name = 'products'
    template_name = "index.html"

    def get_queryset(self):
        products = Product.objects.all().order_by('-created_at')
        if self.kwargs['slug']:
            products = products.filter(category__slug=self.kwargs['slug'])
        for product in products:
            product.main_image = Image.objects.filter(product=product).first()
        return products

class ProductDetailListView(ListView):
    model = Product
    context_object_name = 'product'
    template_name = "pages/product.html"

    def get_queryset(self):
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        # if self.kwargs['slug']:
        #     product = Product.objects.filter(product__slug=self.kwargs['slug'])
        product.main_image = Image.objects.filter(product=product).first()
        product.images = Image.objects.filter(product=product)[:4]
        return product
    
    def get_context_data(self, **kwargs):
        context = super(ProductDetailListView, self).get_context_data(**kwargs)
        product = get_object_or_404(Product, slug=self.kwargs['slug'])
        products = Product.objects.filter(category=product.category).exclude(id=product.id)[:4]
        for product in products:
            product.main_image = Image.objects.filter(product=product).first()
        context['similars'] = products
        return context
