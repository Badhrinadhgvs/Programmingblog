from django.shortcuts import render
from django import *
from Timeapp.models import *
# Create your views 
# 
# here.



def index(request):
#   posts = Post.objects.all()
  post = Post.objects.all()
  context={
        'post':post
    }
  return render(request,'index.html',context)



# blog/views.py

# ...

def blog_category(request, category):
    posts = Post.objects.filter(
        categories_name_contain=category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "category.html", context)


# blog/views.py

# ...

def blog_detail(request, pk):
    post = Post.objects.get(pk=pk)
    context = {
        "post": post    }

    return render(request, "detail.html", context)



