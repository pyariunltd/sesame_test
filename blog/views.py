from django.shortcuts import render, redirect
from blog.forms import BlogForm
from blog.models import Blog, Category
from django.http import HttpResponse


def blog(request):
    blogs=Blog.objects.order_by('-created_date')
    categories = Category.objects.all()
    data={
    'blogs' : blogs,
    'categories':categories
    }
    return render(request, 'blog/blog.html', data)


def new_post(request):
    if request.method == 'POST':
        form = BlogForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.save()
            return redirect('/blog')
    else:
        form = BlogForm()
    return render(request, 'blog/new-post.html', {'form': form})