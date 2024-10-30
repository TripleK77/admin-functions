from django.shortcuts import render

def showCourses(request):
    return render(request,"course/courses.html")

def displayCourse(request):
    return render(request,"course/course.html")

def insertCourse(request):
    return render(request,"course/course_insert.html")

def homePage(request):
     return render(request,"course/home_page.html")

def aboutPage(request):
    return  render(request,"course/about.html")

def contactPage(request):
    return render(request,"course/contact.html")

def userCourses(request):
    return render(request,"course/user_courses.html")

def register(request):
    print("Method id",request.method)
    return render(request,"course/register.html")