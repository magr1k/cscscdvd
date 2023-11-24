from Vladimir import views
from django.urls import path

urlpatterns = [
path('', views.index, kwargs={'name':'Владимир', 'surname': 'Магрик', 'age': '19', 'hobby': 'Настольным теннисом'}),
path('about/', views.about, name='about', kwargs={'place': 'Россия', 'grades': '4.2', 'like': 'да, люблю'}),
path('contacts/', views.contacts, name='about', kwargs={'tel': '+79884029420'}),
]
