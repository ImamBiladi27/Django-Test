from django import forms
from .models import status,produk
# STATUS_CHOICES = (
#     ('available1', 'L QUEENLY'),
#     ('discontinued', 'L MTH AKSESORIS (IM)'),
#     ('ava', 'L MTH TABUNG (LK)'),
#     ('ava2', 'CI MTH TINTA LAIN (IM)'),
#     ('ava3', 'L MTH AKSESORIS (LK)'),
#     ('ava4', 'S MTH STEMPEL (IM)'),
#     ('ava5', 'SP MTH SPAREPART (LK)'),


# )
# class PostForm(forms.Form):
class PostForm(forms.ModelForm):
    class Meta:
        model = produk
        fields=[
            'id_produk',
            'nama_produk',
            'harga',
            'status_id',
            'kategori_id'
        
        ]
        widgets = {
            'id_produk': forms.NumberInput(attrs={'class':'form-control','min': '1', 'max': '10000000'}),
            'nama_produk': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Masukkan Nama Produk'
                }
            ), 
            'harga': forms.NumberInput(attrs={ 'class':'form-control','min': '10', 'max': '10000000'}),  
                  'status_id': forms.Select(attrs={'class':'form-control'}),
         'kategori_id': forms.Select(attrs={'class':'form-control'}),
        }
class UpdateForm(forms.ModelForm):
    class Meta:
        model = produk
        fields=[
         
            'nama_produk',
            'harga',
            'status_id',
            'kategori_id'
        
        ]
        widgets = {
            
            'nama_produk': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Masukkan Nama Produk'
                }
            ), 
            'harga': forms.NumberInput(attrs={ 'class':'form-control','min': '10', 'max': '10000000'}),  
                  'status_id': forms.Select(attrs={'class':'form-control'}),
         'kategori_id': forms.Select(attrs={'class':'form-control'}),
        }   
    # id_produk = forms.IntegerField()
    # nama_produk = forms.CharField(max_length=255)
    # kategori = forms.ChoiceField(
    #     widget=forms.Select,
    #     choices=produk.STATUS_CHOICES,
        
    # )
    # harga = forms.IntegerField()
    # status = forms.ModelChoiceField(queryset=status.objects.all())
    