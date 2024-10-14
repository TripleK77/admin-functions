from django.urls import path
from .views import *
urlpatterns = [
    path('courses', showCourses,name="courses"),
    path('course',displayCourse,name="course"),
    path('insert',insertCourse,name="insert"),
    path('',homePage,name='home')
]
