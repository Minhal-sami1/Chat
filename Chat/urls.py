from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('secretadminplace/minhalonly/', admin.site.urls),
    path('', include("app.urls"))
]
