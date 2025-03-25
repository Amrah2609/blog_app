from django.urls import path
from blog.views import home_page, about_view

urlpatterns = [
    path("", home_page, name="home-page"),
    path("about/", about_view, name="about-page"),
]
