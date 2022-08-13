from unicodedata import name


from django.urls import path
from . import views

urlpatterns = [
    path("", views.home_page, name="home_page"),
    path("base/", views.base, name="base"),
    path("all_cats/", views.all_cats, name="all_cats"),
    path("products/<int:id>/", views.products, name="products"),
    path("home_cats/", views.home_cats, name="home_cats"),
]
