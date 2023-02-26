# pages/urls.py
from django.urls import path
from .views import HomePageView
from .views import AboutPageView
from django.urls import path, include

urlpatterns = [
    #path("", homePageView, name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
    path("", HomePageView.as_view(), name="home"),
]