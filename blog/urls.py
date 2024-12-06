from django.urls import path
from blog.views import blog, single_blog

urlpatterns = [
    path('blog/', blog, name='blog'),
    path('blog/<int:pk>', single_blog, name='single_blog'),
]
