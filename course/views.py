from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from course.models import Course, Event
from course.forms import RegisterForm
from blog.models import Blog
from django.core.paginator import Paginator


def index(request):
    form = RegisterForm()
    blog = Blog.objects.order_by('-id')[:2]
    events = Event.objects.all()
    if request.method == "POST":
        form = RegisterForm(data=request.POST)
        if form.is_valid():
            form.save()
            form = RegisterForm()
    course = Course.objects.all()
    context = {
        'events': events,
        'form': form,
        'courses': course,
        'blogs': blog,
    }
    return render(request, 'index.html', context)


@login_required(login_url='login')
def courses(request):
    all_course = Paginator(Course.objects.all(), 3)
    page = request.GET.get('page')
    all_post = all_course.get_page(page)
    if not page:
        page = 1
    context = {
        'page': page,
        'all_course': all_post,
    }
    return render(request, 'courses.html', context)


def every_single_course(request, pk):
    single_course = get_object_or_404(Course, id=pk)
    category = single_course.category
    category_course = Course.objects.filter(category=category)
    context = {
        'single_course': single_course,
        'every_category': category_course,
    }
    return render(request, 'single-course.html', context)


def search_function(request):
    search = request.GET.get('search')
    posts = Paginator(Course.objects.filter(title__icontains=search), 3 )
    page = request.GET.get('page')
    paginator = posts.get_page(page)
    if not page:
        page = 1

    context = {
        'posts': posts,
        'search': search,
        'page': page,
        'paginator': paginator,
    }
    return render(request, 'search.html', context)
