from django.urls import path

from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("<h1> ini adalah home </h1>")
def about(request):
    return HttpResponse("<h1> ini adalah about</h1>")

def index(request):
    return render(request,'create.html')

# urlpatterns = [
#     path('', views.create_blog, name='create-blog'),
#     path('search/', views.retrieve_blog, name='retrieve-blog'),
#     path('update/<int:pk>', views.update_blog, name='update-blog'),
#     path('delete/<int:pk>', views.delete_blog, name='delete-blog'),
# ]