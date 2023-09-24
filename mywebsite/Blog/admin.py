from django.contrib import admin

# Register your models here.
from .models import kategori,produk,status

admin.site.register([kategori,produk,status])
