from rest_framework import serializers
from .models import produk,kategori,status
import django_filters
class produkSerializer(serializers.ModelSerializer):
    class Meta:
        model = produk
        fields = '__all__'
class kategoriSerializer(serializers.ModelSerializer):
    class Meta:
        model = kategori
        fields = '__all__'
class statusSerializer(serializers.ModelSerializer):
    class Meta:
        model = status
        fields = '__all__'
