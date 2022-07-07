from django.urls import path
from . import views

urlpatterns = [
    path('<slug:foo>', views.MainView.as_view())
]