from django.urls import path
from . import views
from django.urls import include, path

app_name = 'app'

urlpatterns = [
    path('', views.home, name="home"),
    path("profile/", views.profile, name='profile'),
    path("eye/", views.eye, name='eye'),
    path("about/", views.about, name='about'),
    path("faq/", views.faq, name='faq'),
    path("lips/", views.lips, name='lips')
]