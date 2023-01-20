from django.contrib import admin
from Main import views
from django.urls import path, re_path

urlpatterns = [
    re_path(r"^login/$", views.user_login, name="login"),
    re_path(r"^logout/$", views.user_logout, name="logout"),
    re_path(r"^$", views.Question_list, name="home"),
    re_path(r"^views$", views.Question_list_views, name="home_views"),
    re_path(r"^create/$", views.Question_create, name="create"),
    re_path(r"^question/(?P<id>\d+)/$", views.Question_detail, name="detail"),
    re_path(r"^update/(?P<id>\d+)/$", views.Question_update, name="update"),
    re_path(r"^delete/(?P<id>\d+)/$", views.Question_delete, name="delete"),
    re_path(r"^ansupdate/(?P<id>\d+)/$", views.Answer_update, name="ans_update"),
    re_path(r"^ansdelete/(?P<id>\d+)/$", views.Answer_delete, name="ans_delete"),
    re_path(r"^ansaccept/(?P<id>\d+)/$", views.Answer_accept, name="accept"),
    re_path(r"^ansunaccept/(?P<id>\d+)/$", views.Answer_unaccept, name="unaccept"),
    re_path(r"^upvote/(?P<id>\d+)/$", views.vote_up, name="up"),
    re_path(r"^downvote/(?P<id>\d+)/$", views.vote_down, name="down"),
    re_path(r"^profile/(?P<id>\d+)/$", views.profile, name="profile"),
    re_path(r"^profileupdate/(?P<id>\d+)/$", views.Update_pro, name="profile_update"),
    re_path(r"^users$", views.User_list, name="user"),
]
