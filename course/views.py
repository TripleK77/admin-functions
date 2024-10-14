from django.shortcuts import render

def showCourses(request):
    return render(request,"course/courses.html")

def displayCourse(request):
    return render(request,"course/course.html")

def insertCourse(request):
    return render(request,"course/course_insert.html")

def homePage(request):
     return render(request,"course/home_page.html")