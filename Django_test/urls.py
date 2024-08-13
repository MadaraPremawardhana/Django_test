from django.urls import path
from app1 import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin

urlpatterns = [
    path("", views.home, name="home"),
    path("hello1/<name>", views.hello1, name="hello1"),
    path("hello2/<name>", views.hello2, name="hello2"),
    path("hello3/<firstname>/<lastname>", views.hello3, name="hello3"),
    path("count/<str:number>", views.count,name="count"),
    path("about/", views.home1, name="home"),
    path("home/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    ### 06/08/2024###
    path("", views.addMessage, name="log1"),
    path("log/", views.addMessage, name="log2"),
    path("show/", views.showMessages, name="show"),
    ####ADMIN URL####
    path('admin/',admin.site.urls),
    path("search/<q>", views.searchAjax, name="search"),
    #### REST- request####
    path("message/<i>", views.showMessageAsJson, name="showJson"),
    path("addMessage_json/", views.addMessage_json, name="addMessage"),
]   


urlpatterns += staticfiles_urlpatterns()
