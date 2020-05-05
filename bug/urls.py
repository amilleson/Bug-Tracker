from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.index),
    path('new_ticket', views.new_ticket),
    path('create', views.create),
    path('edit/<id>', views.edit_ticket),
    path('edit/<id>/1', views.edit),
    path('dashboard', views.dashboard),
    path('login', views.login),
    path('register', views.register),
    path('logout', views.logout),
    path('admin', views.admin),
    path('delete/<id>', views.delete_trip),
    path('edit/<id>/2', views.edit2),
    path('edit/<id>/3', views.edit3),
    path('vote/<id>', views.vote),
]