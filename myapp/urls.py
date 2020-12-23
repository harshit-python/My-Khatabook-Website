from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("addnewtrans", views.addnewtrans, name="addnewtrans"),
    path("transactions", views.transactions, name="transactions"),
    path("logout", views.logout, name="logout"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register")

]
