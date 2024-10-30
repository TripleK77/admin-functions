from django.urls import path
from .views import *
urlpatterns = [
    path('courses', showCourses,name="courses"),
    path('course',displayCourse,name="course"),
    path('insert',insertCourse,name="insert"),
    path('',homePage,name='home'),
    path('contact',contactPage,name='contact'),
    path('about',aboutPage,name='about'),
    path('user',userCourses,name='userView'),
    path('register',register,name='register'),
]
