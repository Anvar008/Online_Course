from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from blog.models import Blog
from course.models import Category


@login_required(login_url='login')
def blog(request):
    category = Category.objects.all()
    every_blog = Blog.objects.all()
    category_title = request.GET.get('category')
    category_blog = Paginator(Blog.objects.filter(category=category_title), 4)
    page = request.GET.get('page')
    all_blog = category_blog.get_page(page)
    if not page:
        page = 1
    context = {
        'page': page,
        'all_blog': all_blog,
        'every_blog': every_blog,
        'every_category': category,
        'category_blog': category_blog,
        'category_title': category_title,
    }
    return render(request, 'blog.html', context)


@login_required(login_url='login')
def single_blog(request, pk):
    all_blogs = get_object_or_404(Blog, id=pk)
    category = all_blogs.category
    category_blog = Blog.objects.filter(category=category)[:2]

    context = {
        'all_blogs': all_blogs,
        'category_blog': category_blog,
    }
    return render(request, 'blog-details.html', context)
