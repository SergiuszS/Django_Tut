from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainView.as_view()),
    path('redirect', views.redirect),
    path('second_page', views.second_page),
]