from . import views
from django.urls import path


urlpatterns = [
    path('register',views.register,name='register'),
    path('login',views.login,name='login'),
    path('CollegeForm', views.CollegeForm, name='CollegeForm'),
    path('formstudent', views.formstudent, name='formstudent'),
    path('logout',views.logout,name='logout'),

]