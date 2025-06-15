from django.urls import path
from .views import *

app_name = 'posts'

urlpatterns = [
    path('', post_list, name="list"),
    path('<slug:slug>', post_page, name="page")
]
