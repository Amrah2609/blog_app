from django.shortcuts import render
from blog.models import Header, Blog, About


# Create your views here.

def home_page(request):
    context = {}
    context["header"] = Header.objects.last()
    context["blogs"] = Blog.objects.filter(status="publish")
    return render(request, template_name= 'home/index.html', context=context)

def about_view(request):
    return render(request, template_name='about.html', context= {
        'about': About.objects.last(),
    })


