from django.urls import path
from .views import *
urlpatterns = [
    path('', showCourses,name="courses"),
    path('course',displayCourse,name="course"),
    path('insert',insertCourse,name="insert"),
]
