from django.urls import path
from drfApp.api import views

urlpatterns = [
    path("show_list/", views.ShowListAV.as_view()),
    path("show/<int:pk>", views.ShowAV.as_view()),
    path("platform_list/", views.PlatformListAV.as_view()),
    path("platform/<int:pk>", views.PlatformAV.as_view()),
]