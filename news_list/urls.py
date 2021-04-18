from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "news_list"

urlpatterns = [
    path('', views.home, name="homepage"),

]