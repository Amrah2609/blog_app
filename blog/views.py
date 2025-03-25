from django.shortcuts import render

# Create your views here.

def home_page(request):
    return render(request, template_name= 'home/index.html', context= {})

def about_view(request):
    return render(request, template_name='about.html', context= {})


