
from django.contrib import admin
from django.urls import path,include
# from django.http import HttpResponse


# from . import views
# def index(request):
#     return HttpResponse("halo dunia")
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('',include('Blog.urls')),
    # path('', Blogurls.index),
    # path('blog', blogViews.index),
    # # path('about/', Blogurls.about),
    path('',include('Blog.urls'),name='Blog'),
    # path('Blog2/',include('Blog.urls'),)

    
]
