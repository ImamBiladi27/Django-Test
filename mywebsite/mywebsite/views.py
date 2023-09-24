from django.shortcuts import render

def index(request):
    context={
        'page':'Home'
    }
    return render(request, 'index.html',context)