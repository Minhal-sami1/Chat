from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('register/', views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path('', views.index, name="index"),
    path('getid/', views.get_unique_id, name="getid"),
    path('connect/', views.connect, name="connect"),
    path("message/<str:user_id>", views.messages, name="message"),
    path("newmessages/<str:userf>/<str:usert>", views.get_messages, name="message"),
    path("contacted/", views.Already_contacted, name="contacted")
]
