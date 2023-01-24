from django.urls import path

from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name='index'),
    path('', views.index, name='home'),

    path('login/', auth_views.LoginView.as_view(template_name='quora/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='quora/logout.html'), name='logout'),

    path("register/", views.user_register, name="register"),

    path("create_question",views.create_question,name='create_question')
]
