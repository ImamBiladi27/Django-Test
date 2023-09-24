from rest_framework import serializers
from .models import produk

class produkSerializer(serializers.ModelSerializer):
    class Meta:
        model = produk
        fields = '__all__'
