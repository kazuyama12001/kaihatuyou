from django.urls import path
from . import views

urlpatterns = [
    path('', views.work_ck, name='work_ck'),
    path('workCk/<int:pk>/', views.work_detail, name='work_detail'),
]