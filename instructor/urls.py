from django.urls import path
from instructor.views import instructor, search_function

urlpatterns = [
    path('instructors/', instructor, name='instructors'),
    path('search1/', search_function, name='search1')
]
