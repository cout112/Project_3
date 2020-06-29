from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("orders", views.login_authenticate, name="orders"),
    path("logout", views.logout_view, name="logout"),
    path("signup", views.signup, name="signup"),
    path("add_address", views.add_address, name="address"),
    path("order", views.order, name="order"),
]
