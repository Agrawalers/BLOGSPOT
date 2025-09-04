from django.shortcuts import render,redirect
from .models import Post
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def index(request):
  posts = Post.objects.all()
  return render(request, 'index.html',{'posts':posts})


def post(request,pk):
  posts = Post.objects.get(id=pk)
  return render(request,'post.html',{'posts': posts})

def register(request):
  if request.method == 'POST':
    title = request.POST['blogTitle']
    body = request.POST['blogContent']
    if title and body:
        Post.objects.create(title=title, body=body)
    
        return redirect('/')
  
  else:
    return render(request,'create.html')