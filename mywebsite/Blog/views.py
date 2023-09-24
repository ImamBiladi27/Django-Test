from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
from .models import produk,status,kategori
from django.contrib import messages
from .serializers import produkSerializer
from rest_framework.renderers import JSONRenderer
from .forms import PostForm,UpdateForm
from rest_framework import generics

def index(request):
    produks= produk.objects.filter(status_id=1).order_by('pk')
    statuss=status.objects.all()
    kategoris=kategori.objects.all()
    
    # print(produks)
    context ={
        'title':' Apikasi Rekayasa Data Produk Dengan Django & PostgreSQL',
        'Heading' : 'Aplikasi di my website',
        'Produks':produks,
        'Statuss':statuss,
        'Kategoris':kategoris
    }
    return render(request, 'blog/index.html',context)

def produk_detail(request):
    prd = produk.objects.get(id_produk=6)
    serializer = produkSerializer(prd)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


# def recent(request):
#     return HttpResponse('<h1> ini adalah recent post </h1>')

def create(request):
    post_form = PostForm(request.POST or None)
    if request.method =='POST':
        if post_form.is_valid():
            # produk.objects.create(
            #     id_produk = post_form.cleaned_data.get['id_produk'],
            #     nama_produk = post_form.cleaned_data.get['nama_produk'],
            #     kategori_id = post_form.cleaned_data.get['kategori'],
            #     harga = post_form.cleaned_data.get['harga'],
            #     status_id_id = post_form.cleaned_data.get['status'],
            # )
            post_form.save()
        return redirect("index")
    context = {
        'title':'Tambahkan Produk',
        'post_form':post_form
    }
    return render(request, 'blog/create.html',context)
def delete(request,delete_id):
   produk.objects.filter(id=delete_id).delete()
   messages.success(request, 'Item has been successfully deleted.')
   return redirect("index")
def update(request,update_id):
    akun_update = produk.objects.get(id=update_id)
   
    data = {
        'nama_produk' : akun_update.nama_produk,
        'kategori_id' : akun_update.kategori_id,
        'harga' : akun_update.harga,
        'status_id_id' : akun_update.status_id_id,
        
    }
    akun_form = PostForm(request.POST or None, initial=data,instance=akun_update)
    if request.method =='POST':
        if akun_form.is_valid():
            # produk.objects.create(
            #     id_produk = post_form.cleaned_data.get['id_produk'],
            #     nama_produk = post_form.cleaned_data.get['nama_produk'],
            #     kategori_id = post_form.cleaned_data.get['kategori'],
            #     harga = post_form.cleaned_data.get['harga'],
            #     status_id_id = post_form.cleaned_data.get['status'],
            # )
            akun_form.save()
        return redirect("index")
    context = {
        'title':'Update Data',
        'post_form':akun_form
    }
    # print(akun_update)
    return render(request, 'blog/create.html',context)
class produkListCreateView(generics.ListCreateAPIView):
    queryset = produk.objects.all()
    serializer_class = produkSerializer

class produkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = produk.objects.all()
    serializer_class = produkSerializer
# class produkList(generics.ListCreateAPIView):
#     serializer_class=produkSerializer
#     queryset = produk.objects.all()
   
