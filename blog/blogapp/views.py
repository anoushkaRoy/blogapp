from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Blog, SubBlog


@login_required
def blog_list(request):
    blogs = Blog.objects.filter(author=request.user)
    return render(request, 'blog_list.html', {'blogs': blogs})

@login_required
def blog_detail(request, pk):
    blog = get_object_or_404(Blog, pk=pk, author=request.user)
    return render(request, 'blog_detail.html', {'blog': blog})

@login_required
def blog_create(request):
    if request.method == 'POST':
        blog = Blog.objects.create(
            title=request.POST['title'],
            content=request.POST['content'],
            author=request.user
        )
        return redirect('blog_detail', pk=blog.pk)
    return render(request, 'blog_create.html')

@login_required
def blog_update(request, pk):
    blog = get_object_or_404(Blog, pk=pk, author=request.user)
    if request.method == 'POST':
        blog.title = request.POST['title']
        blog.content = request.POST['content']
        blog.save()
        return redirect('blog_detail', pk=blog.pk)
    return render(request, 'blog_update.html', {'blog': blog})

@login_required
def blog_delete(request, pk):
    blog = get_object_or_404(Blog, pk=pk, author=request.user)
    if request.method == 'POST':
        blog.delete()
        return redirect('blog_list')
    return render(request, 'blog_delete.html', {'blog': blog})

@login_required
def subblog_create(request, blog_pk):
    blog = get_object_or_404(Blog, pk=blog_pk, author=request.user)
    if request.method == 'POST':
        SubBlog.objects.create(
            blog=blog,
            title=request.POST['title'],
            content=request.POST['content']
        )
        return redirect('blog_detail', pk=blog.pk)
    return render(request, 'subblog_create.html', {'blog': blog})

@login_required
def user_profile(request):
    user = request.user
    return render(request, 'user_profile.html', {'user': user})