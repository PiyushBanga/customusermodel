from django.urls import path
from . import views

app_name = 'Main'

urlpatterns = [
    path('', views.home, name='home'),
    path('studentregister', views.student_registration, name='studentregister'),
    path('teacherregister', views.teacher_registration, name='teacherregister'),
    path('login', views.login_view, name='login'),
    path('studentdashboard', views.student_dashboard, name='studentdashboard'),
    path('teacherdashboard', views.teacher_dashboard, name='teacherdashboard'),

]
