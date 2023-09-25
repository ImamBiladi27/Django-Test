from django import forms
from .models import status,produk,kategori

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
class StatusForm(forms.ModelForm):
    class Meta:
        model = status
        fields=[
          
            'nama_status'
        ]
        widgets = {
               'id_status': forms.NumberInput(attrs={'class':'form-control','min': '1', 'max': '10000000'}),
               'nama_status': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Masukkan Nama Status'
                }
            ), 
        }
class KategoriForm(forms.ModelForm):
    class Meta:
        model = kategori
        fields=[
            'nama_kategori',
        ]
        widgets = {
             'id_kategori': forms.NumberInput(attrs={'class':'form-control','min': '1', 'max': '10000000'}),
               'nama_kategori': forms.TextInput(
                attrs={
                    'class':'form-control',
                    'placeholder':'Masukkan Nama Kategori'
                }
            ), 
        }

class UpdateStatusForm(forms.ModelForm):
    class Meta:
        model = status
        fields=[
            
            'nama_status',
        ]
        widgets= {
                'id_status': forms.NumberInput(attrs={'class':'form-control','min': '1', 'max': '10000000'}),
               'nama_status': forms.Select(attrs={'class':'form-control'}),
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
    
    # class ProductSearchForm(forms.Form):
    #     search_query = forms.CharField(
    #         max_length=100,
    #         required=False,
    #         label='Search',
    #         widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search Products'})
    #     )