from django.urls import path
from . import views

urlpatterns = [
    path('', views.endpoint),
    path('advocates/', views.AdvocatesList),
    path('advocates/<str:username>', views.AdvocatesDetails),
]
