from os import name
from resume.views import  blog_page, home, contact, about
from django.urls import path

urlpatterns = [
    path('', home, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('resume/<int:id>', blog_page, name='blog_page'),
]