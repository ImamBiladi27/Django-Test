# from django.urls import path
# from . import views
# from .views import produk_detail

# urlpatterns = [
#     path('', views.index),
#     path('serializer/', views.produk_detail, name='produk')
# ]
from django.contrib import admin
from django.urls import path,include

from . import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name='index'),

    path('produk/', views.produkListCreateView.as_view(), name='produk-list-create'),
     path('produk/<int:pk>/', views.produkDetailView.as_view(), name='produk-detail'),
    path('create/',views.create,name='create'),
    path('delete/<delete_id>', views.delete, name='delete'),
    path('update/<update_id>', views.update, name='update'),
    
]
