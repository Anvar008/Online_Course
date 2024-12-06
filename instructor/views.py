from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.contrib.auth.admin import User
from django.core.paginator import Paginator


@login_required(login_url='login')
def instructor(request):
    instructors = User.objects.filter(role=0)
    context = {
        'instructors':  instructors
    }
    return render(request, 'instructors.html', context)

@login_required(login_url='login')
def search_function(request):
    search1 = request.GET.get('search1')
    posts = Paginator(User.objects.filter(title__icontains=search1), 3 )
    page = request.GET.get('page')
    paginator = posts.get_page(page)
    if not page:
        page = 1

    context = {
        'posts': posts,
        'search1': search1,
        'page': page,
        'paginator': paginator,
    }
    return render(request, 'search.html', context)
