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
from .filters import ProdukFilter
urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.index,name='index'),
  path('indexstatus', views.indexstatus,name='indexstatus'),
  path('indexkategori', views.indexkategori,name='indexkategori'),
  path('produk/', views.produkListCreateView.as_view(), name='produk-list-create'),
  path('kategori/', views.kategoriListCreateView.as_view(), name='kategori-list-create'),
  # path('status/', views.statusSerializer.as_view(), name='status-list-create'),
  path('produk', views.ProdukListView.as_view(), name='produk-list'),
        #  path('produk/', views.produkDetailView.as_view({'get': 'list'}), name='produk-list'),
  # path('status/<int:pk>/', views.statusDetailView.as_view(), name='status-detail'),
  path('kategori/<int:pk>/', views.kategoriDetailView.as_view(), name='kategori-detail'),
  
  path('create/',views.create,name='create'),
  path('delete/<delete_id>', views.delete, name='delete'),
  path('update/<update_id>', views.update, name='update'),
  path('createstatus/',views.createStatus,name='createstatus'),
  path('deletestatus/<delete_id>',views.deletestatus,name='deletestatus'),
  path('updatestatus/<update_id>', views.updateStatus, name='updatestatus'),
   path('createkategori/',views.createKategori,name='createkategori'),
  path('updatekategori/<update_id>', views.updatekategori, name='updatekategori'),
    path('deletekategori/<delete_id>',views.deletekategori,name='deletekategori'),
    
]
