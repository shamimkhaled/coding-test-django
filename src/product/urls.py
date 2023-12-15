from django.urls import path
from product.views.product import search


from product.views.product import CreateProductView, ListViewProductTable, ProductEditView
from product.views.variant import VariantView, VariantCreateView, VariantEditView

app_name = "product"
 
urlpatterns = [
    # Variants URLs
    path('variants/', VariantView.as_view(), name='variants'),
    path('variant/create', VariantCreateView.as_view(), name='create.variant'),
    path('variant/<int:id>/edit', VariantEditView.as_view(), name='update.variant'),

    # Products URLs
    path('create/', CreateProductView.as_view(), name='create.product'),
    path('<int:id>/edit', ProductEditView.as_view(), name='update.product'),

    path('list/', ListViewProductTable.as_view(), name='list.product'),
    
   # path('list/', TemplateView.as_view(template_name='products/list.html', extra_context={
    #    'product': True
   # }), name='list.product'),

   path('filter/', search, name='search'),
]
