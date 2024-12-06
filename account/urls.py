from django.urls import path
from account.views import register_function, main_function, login_function, logout_function

urlpatterns = [
    path('register/', register_function, name='register'),
    path('main/', main_function, name='main'),
    path('login/', login_function, name='login'),
    path('logout/', logout_function, name='logout')
]