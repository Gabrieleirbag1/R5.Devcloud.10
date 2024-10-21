from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('ajout/', views.ajout),
    path('update/<int:id>/',views.update),
    path('propterre/update/<int:id>/',views.update),
    path('delete/<int:id>/', views.delete),
    path('traitement/', views.traitement),
    path('affiche/<int:id>/',views.affiche),

]
