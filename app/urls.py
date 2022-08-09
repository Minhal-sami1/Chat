from django.urls import path
from django.contrib.auth.decorators import login_required
from . import views


urlpatterns = [
    path('register/', views.RegisterView.as_view(), name="register"),
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", login_required(views.logout_view), name="logout"),
    path('', login_required(views.index), name="index"),
    path('getid/', login_required(views.get_unique_id), name="getid"),
    path('connect/', login_required(views.connect), name="connect"),
    path("message/<str:user_id>", login_required(views.messages), name="message"),
    path("newmessages/<str:userf>/<str:usert>", login_required(views.get_messages), name="message"),
    path("contacted/", login_required(views.Already_contacted), name="contacted")
]
