from django.urls import path
from .views import set_cookie, show_template

urlpatterns = [
    path('set-cookie/', set_cookie, name='set-cookie'),
    path('show-template/', show_template, name='show-template'),
]
