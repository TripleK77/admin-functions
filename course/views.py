from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import messages

def showCourses(request):
    courses=[
        ["#java","Java Courses"],
        ["#python","Python courses"],
        ["#php","PHP courses"],
        ["#flutter","Flutter courses",],
        ["#matlab","MatLab Courses",],
    ]
    java_courses=[
    {
    "title":"Java Dart Concepts",
    "duration" : "2 months",
    "start_date" : "01-11-2024",
    "time" : "09 AM - 11 AM",
    },
    {
    "title":"Java Advance",
    "duration" : "2 months",
    "start_date" : "01-11-2024",
    "time" : "09 AM - 11 AM",
    },
    {
    "title":"Java Web Concepts",
    "duration" : "2 months",
    "start_date" : "01-11-2024",
    "time" : "09 AM - 11 AM",
    },
    ]
    return render(request,"course/courses.html",{"courses":courses,"java_courses":java_courses,"title":"Show Courses"})


def displayCourse(request):
    return render(request,"course/course.html",{"title":"Display Course"})

def insertCourse(request):
    return render(request,"course/course_insert.html",{"title":"Insert Course"})

def homePage(request):
     course_categories=[
         {
             "title":"Web Dev",
             "desc":"""Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sunt, nulla, maxime quae deserunt asperiores itaque voluptatem, assumenda magni quas nesciunt
                         incidunt? Veniam, repellat officia! Ipsa quasi voluptatum modi nisi repellat""",
         },
         {
             "title":"Mobile Dev",
             "desc":"""Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sunt, nulla, maxime quae deserunt asperiores itaque voluptatem, assumenda magni quas nesciunt
                         incidunt? Veniam, repellat officia! Ipsa quasi voluptatum modi nisi repellat""",
         },
         {
             "title":"API Dev",
             "desc":"""Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sunt, nulla, maxime quae deserunt asperiores itaque voluptatem, assumenda magni quas nesciunt
                         incidunt? Veniam, repellat officia! Ipsa quasi voluptatum modi nisi repellat""",
         }
     ]
     return render(request,"course/home_page.html",{"course_categories":course_categories})

def aboutPage(request):
    return  render(request,"course/about.html",{"title":"About Page"})

def contactPage(request):
    return render(request,"course/contact.html",{"title":"Contact Page"})

def userCourses(request): 
    flutter_courses=[
        {
        "title":"Dart Concepts",
        "duration" : "2 months",
        "start_date" : "01-11-2024",
        "time" : "09 AM - 11 AM",
        },
        {
        "title":"Dart Advance",
        "duration" : "2 months",
        "start_date" : "01-11-2024",
        "time" : "09 AM - 11 AM",
        },
        {
        "title":"Flutter Concepts",
        "duration" : "2 months",
        "start_date" : "01-11-2024",
        "time" : "09 AM - 11 AM",
        },
    ]
    java_courses=[
        {
        "title":"Java Dart Concepts",
        "duration" : "2 months",
        "start_date" : "01-11-2024",
        "time" : "09 AM - 11 AM",
        },
        {
        "title":"Java Advance",
        "duration" : "2 months",
        "start_date" : "01-11-2024",
        "time" : "09 AM - 11 AM",
        },
        {
        "title":"Java Web Concepts",
        "duration" : "2 months",
        "start_date" : "01-11-2024",
        "time" : "09 AM - 11 AM",
        },
    ]
    python_courses=[
        {
        "title":"Python Dart Concepts",
        "duration" : "2 months",
        "start_date" : "01-11-2024",
        "time" : "09 AM - 11 AM",
        },
        {
        "title":"Python Advance",
        "duration" : "2 months",
        "start_date" : "01-11-2024",
        "time" : "09 AM - 11 AM",
        },
        {
        "title":"Python Web Concepts",
        "duration" : "2 months",
        "start_date" : "01-11-2024",
        "time" : "09 AM - 11 AM",
        },
    ]
    return render(request,"course/user_courses.html",{"flutter_courses":flutter_courses,"java_courses":java_courses,"python_courses":python_courses,"title":"User Courses"})

def register(request):
    print("Method id",request.method)
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        address=request.POST["address"]
        course=request.POST["courses"]
        print(name,email,phone,address,course,sep=" , ")
    return render(request,"course/register.html",{"title":"Register"})

def login(request):
    if request.method=="POST":
        name=request.POST["name"]
        phone=request.POST["phone"]
        if name=="abc" and phone=="0987":
            user=authenticate(name=name)
            print("login success")
            messages.add_message(request,messages.SUCCESS,'Login Success')
            return render(request,"course/home_page.html")
        else:
            return render(request,"course/login.html")
    return render(request,"course/login.html",{"title":"Login"})