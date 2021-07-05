from os import name
from django.urls import path
from django.views.generic import TemplateView
from app import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/',TemplateView.as_view(template_name='about.html'), name='about'),
    path('terms/',TemplateView.as_view(template_name='tnc.html'),name='tnc'),
    path('article/add',views.article_add, name="article_add"),
    path('contact/',views.contact,name='contact'),
]