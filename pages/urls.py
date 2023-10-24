from django.urls import path
from pages import HomePageviews, AboutPageView

urlpatterns = [
    path("", HompePageView.as_view(), name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
