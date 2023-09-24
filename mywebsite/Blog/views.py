from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import HttpResponseRedirect
# Create your views here.
from .models import produk,status,kategori
from django.contrib import messages
from .serializers import produkSerializer
from rest_framework.renderers import JSONRenderer
from .forms import PostForm,UpdateForm,StatusForm
from rest_framework import generics

def index(request):
    produks= produk.objects.filter(status_id=1).order_by('pk')
    statuss=status.objects.all()
    kategoris=kategori.objects.all()
    
    
    context ={
        'title':' Apikasi Rekayasa Data Produk Dengan Django & PostgreSQL',
        'Heading' : 'Aplikasi di my website',
        'Produks':produks,
        'Statuss':statuss,
        'Kategoris':kategoris
    }
    return render(request, 'blog/index.html',context)

def indexstatus(request):
    
    statuss= status.objects.all().order_by('pk')
 
    
    # print(produks)
    context ={
        'title':' Apikasi Rekayasa Data Produk Dengan Django & PostgreSQL',
        'Heading' : 'Aplikasi di my website',

        'Statuss':statuss,
    
    }
    return render(request, 'blog/indexstatus.html',context)
def produk_detail(request):
    prd = produk.objects.get(id_produk=6)
    serializer = produkSerializer(prd)
    json_data = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


# def recent(request):
#     return HttpResponse('<h1> ini adalah recent post </h1>')



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
    
    akun_update = status.objects.get(id=update_id)
   
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
   status.objects.filter(id=delete_id).delete()
   messages.success(request, 'Item has been successfully deleted.')
   return redirect("indexstatus")

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

class produkDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = produk.objects.all()
    serializer_class = produkSerializer
   
