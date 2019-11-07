from django.urls import path
from . import views

urlpatterns = [
    path('index', views.show),
    path('register', views.register),
    path('', views.index),
    path('edit/<int:id>',views.edit),
    path('update/<int:id>',views.update),
    path('delete/<int:id>',views.destroy),
    path('addData',views.addData),
]