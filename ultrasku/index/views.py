from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index/index.html',context={
        "index":0
    })

def contact(request):
    return  render(request, 'index/contact.html',context={
        "index":1
    })

def why_me(request):
    return  render(request, 'index/index.html',context={
        "index":2
    })

