from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
from .models import produk,status,kategori
from django.contrib import messages
from .serializers import produkSerializer,kategoriSerializer,statusSerializer

from rest_framework.renderers import JSONRenderer
from .forms import PostForm,StatusForm,KategoriForm
from rest_framework import generics, viewsets, filters
from .filters import ProdukFilter
from django_filters.rest_framework import DjangoFilterBackend
def indexkategori(request):
    kategoris= kategori.objects.all().order_by('pk')
    
    
    
    context ={
        'title':' Apikasi Rekayasa Data Produk Dengan Django & PostgreSQL',
        'Heading' : 'Aplikasi di my website',
        'Kategoris':kategoris,
       
    }
    return render(request, 'blog/indexkategori.html',context)

def updatekategori(request,update_id):
    
    akun_update = kategori.objects.get(id_kategori=update_id)
   
    data = {
        'nama_kategori' : akun_update.nama_kategori,
      
        
    }
    akun_form = KategoriForm(request.POST or None, initial=data,instance=akun_update)
    if request.method =='POST':
        if akun_form.is_valid():
         
            akun_form.save()
        return redirect("indexkategori")
    context = {
        'title':'Update Data Status',
        'kategori_form':akun_form
    }

    return render(request, 'blog/createkategori.html',context)

def deletekategori(request,delete_id):
   kategori.objects.filter(id_kategori=delete_id).delete()
   messages.success(request, 'Item has been successfully deleted.')
   return redirect("indexkategori")

def indexstatus(request):
    
    statuss= status.objects.all().order_by('pk')
 
    context ={
        'title':' Apikasi Rekayasa Data Produk Dengan Django & PostgreSQL',
        'Heading' : 'Aplikasi di my website',

        'Statuss':statuss,
    
    }
    return render(request, 'blog/indexstatus.html',context)

def createKategori(request):
    kategori_form = KategoriForm(request.POST or None)
    if request.method =='POST':
        if kategori_form.is_valid():
    
            kategori_form.save()
        return redirect("indexkategori")
    context = {
        'title':'Tambahkan Kategori',
        'kategori_form':kategori_form
    }
    return render(request, 'blog/createkategori.html',context)

def createStatus(request):
    status_form = StatusForm(request.POST or None)
    if request.method =='POST':
        if status_form.is_valid():
    
            status_form.save()
        return redirect("indexstatus")
    context = {
        'title':'Tambahkan Status',
        'status_form':status_form
    }
    return render(request, 'blog/createstatus.html',context)

def updateStatus(request,update_id):
    
    akun_update = status.objects.get(id_status=update_id)
   
    data = {
        'nama_status' : akun_update.nama_status,
      
        
    }
    akun_form = StatusForm(request.POST or None, initial=data,instance=akun_update)
    if request.method =='POST':
        if akun_form.is_valid():
         
            akun_form.save()
        return redirect("indexstatus")
    context = {
        'title':'Update Data Status',
        'status_form':akun_form
    }

    return render(request, 'blog/createstatus.html',context)

def deletestatus(request,delete_id):
   status.objects.filter(id_status=delete_id).delete()
   messages.success(request, 'Item has been successfully deleted.')
   return redirect("indexstatus")

def index(request):
    # produks= produk.objects.all().order_by('pk')
    
    produks = produk.objects.filter(status_id__nama_status="bisa dijual").order_by('pk')
    # print(books_with_authors)
    
    
    context ={
        'title':' Apikasi Rekayasa Data Produk Dengan Django & PostgreSQL',
        'Heading' : 'Aplikasi di my website',
        'Produks':produks,
        # 'Foreign':books_with_authors
    }
    return render(request, 'blog/index.html',context)

def produk_detail(request):
    prd = produk.objects.get(id_produk=6)
    serializer = produkSerializer(prd)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')

def create(request):
    post_form = PostForm(request.POST or None)
    if request.method =='POST':
        if post_form.is_valid():
    
            post_form.save()
        return redirect("index")
    context = {
        'title':'Tambahkan Produk',
        'post_form':post_form
    }
    return render(request, 'blog/create.html',context)

def delete(request,delete_id):
   produk.objects.filter(no=delete_id).delete()
   messages.success(request, 'Item has been successfully deleted.')
   return redirect("index")


def update(request,update_id):
    akun_update = produk.objects.get(no=update_id)
   
    data = {
        'nama_produk' : akun_update.nama_produk,
        'kategori_id' : akun_update.kategori_id,
        'harga' : akun_update.harga,
        'status_id_id' : akun_update.status_id_id,
        
    }
    akun_form = PostForm(request.POST or None, initial=data,instance=akun_update)
    if request.method =='POST':
        if akun_form.is_valid():
         
            akun_form.save()
        return redirect("index")
    context = {
        'title':'Update Data',
        'post_form':akun_form
    }

    return render(request, 'blog/create.html',context)

class produkListCreateView(generics.ListCreateAPIView):
    queryset = produk.objects.all()
    serializer_class = produkSerializer
        

class ProdukListView(generics.ListAPIView):
    queryset = produk.objects.all()
    serializer_class = produkSerializer
    filterset_class = ProdukFilter
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['id_produk']

class kategoriListCreateView(generics.ListCreateAPIView):
    queryset = kategori.objects.all()
    serializer_class = kategoriSerializer
class kategoriDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = kategori.objects.all()
    serializer_class = kategoriSerializer
# class statusListCreateView(generics.ListCreateAPIView):
#     queryset = status.objects.all()
#     serializer_class = statusSerializer
# class statusDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = status.objects.all()
#     serializer_class = statusSerializer



          
