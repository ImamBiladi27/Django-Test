
import django_filters
from .models import produk
class ProdukFilter(django_filters.FilterSet):
    id_produk = django_filters.CharFilter(lookup_expr='icontains')  # Ubah 'nama_kolom' sesuai dengan nama kolom yang diinginkan

    class Meta:
        model = produk
        fields = ['id_produk','nama_produk']