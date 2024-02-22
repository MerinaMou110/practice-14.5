from django.urls import path,include
from . import views

urlpatterns = [
   
     path('', views.DjangoForm,name="django_form"),
     path('django/',views.DjangoModel,name="django_Model"),
     path('delete/<int:roll>', views.delete_student, name="delete_student"),
     path('add/', views.add_student, name="add_student"),
]