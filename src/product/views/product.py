from django.views import generic
from django.shortcuts import render
from product.models import Variant, ProductVariant, Product, ProductVariantPrice
from django.shortcuts import get_object_or_404

from django.template import loader
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q

from django.views.generic import ListView, CreateView, UpdateView

from product.forms import ProductForm





    
# Create Product View
class CreateProductView(generic.TemplateView):
    template_name = 'products/create.html'
    model = Product
    def get_context_data(self, **kwargs):
        context = super(CreateProductView, self).get_context_data(**kwargs)
        variants = Variant.objects.filter(active=True).values('id', 'title')
        
        context['product'] = True 
        context['variants'] = list(variants.all())
        return context
    
    
    







class ListViewProductTable(generic.TemplateView):  
     template_name = 'products/list.html'
     
     def get_context_data(self, **kwargs):
        context = super(ListViewProductTable, self).get_context_data(**kwargs)
        variants = ProductVariant.objects.filter().values('variant_id', 'variant_title')
        #context['products'] = True
        context['variants'] = list(variants.all())
        products = Product.objects.all().filter().values('id', 'title', 'description', 'created_at')
        context['products'] = list(products.all())
        product_count = products.count()
        context['product_count'] = product_count
        prod_var_price = ProductVariantPrice.objects.all()
        context['prod_var_price'] = list(prod_var_price.all())
        

        paginator = Paginator(products, 2)  
        page = self.request.GET.get('page')

        try:
            products_page = paginator.page(page)
        except PageNotAnInteger:
            products_page = paginator.page(1)
        except EmptyPage:
            products_page = paginator.page(paginator.num_pages)

        context['products'] = products_page

        context['paginator'] = paginator
        context['page_obj'] = products_page
        return context
        
 
  
    
class ProductEditView(UpdateView):
    form_class = ProductForm
    model = ProductVariantPrice
    template_name = 'products/create.html'
    success_url = '/product/list'
    pk_url_kwarg = 'id'
   


def search(request):
    products = []  
    product_count = 0  
    title = request.GET.get('title')
    variants = request.GET.get('variants')
    price_from = request.GET.get('price_from')
    price_to = request.GET.get('price_to')
    date = request.GET.get('date')

    if title:
        products = Product.objects.order_by('-created_at').filter(
                Q(description__icontains=title) | Q(title__icontains=title)
            )
        product_count = len(products)  

    if variants:
        variants = Product.objects.filter(
                 Q(productvariant__variant_title__icontains =variants)
            ).order_by('-created_at')
    
    
    
    if price_from and price_to:
        price_from = Product.objects.filter(
                 Q(productvariantprice__price__range= (price_from, price_to)) 
            ).order_by('-created_at')
       
       
        
    if date:
        date = Product.objects.filter(
                 Q(created_at=date)).order_by('-created_at')
            

    context = {
        'products': products,
        'product_count': product_count,
        'variants': variants,
        'price_from': price_from,
        'date': date,
    }
    print(f"Products: {products}")  
    print(f"Variant Filter Products: {variants}") 
    print(f"Price Filter Products: {price_from}")  

    return render(request, 'products/list.html', context)

