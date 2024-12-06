from django.urls import path
from course.views import index, courses, every_single_course, search_function

urlpatterns = [
    path('', index, name='index'),
    path('courses/', courses, name='url_course'),
    path('single_course/<int:pk>/', every_single_course, name='single_course'),
    path('search/', search_function, name='search'),
]