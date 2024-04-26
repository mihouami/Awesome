from django.shortcuts import render, redirect
from .models import *
from .forms import *

def home_view(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'a_posts/home.html', context)


def post_create_view(request):
    form = PostCreateForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'a_posts/post_create.html', {'form':form})
