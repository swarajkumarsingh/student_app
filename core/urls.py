from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('health', views.health, name='health'),
    path('student/create/', views.student_form, name='student_form'),
    path("student/create/raw", views.create, name='create'),
    path("student/<str:sid>", views.get, name='get'),  # Change this line
    path("students", views.get_all, name='get_all'),
]
