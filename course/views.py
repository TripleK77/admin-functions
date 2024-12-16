from django.shortcuts import render
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from .models import *
from django.db import connection
from .forms import*
import psycopg2

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
    if request.method=="POST":
        title=request.POST["title"]
        description=request.POST["description"]
        start_date=request.POST["start_date"]
        end_date=request.POST["end_date"]
        price=request.POST["price"]
        image=request.POST["file"]
        print(title,start_date,end_date,price)
        c=Course1.object.create(title=title,start_date=start_date,end_date=end_date,price=price)
        c.save()
        return render(request,"course/home_page.html")

    else:
        return render(request,"course/course_insert.html")
    # return render(request,"course/course_insert.html",{"title":"insert course"})

def homePage(request):
     categories=CourseCategory.objects.all()
     return render(request,"course/home_page.html",{"categories":categories})
    # try:
    #     user=User.objects.get(username='KKK')
    #     print(user)
    # except Exception as e:
    #     print("user not found error")

    #     print("----------------")

    #     with connection.cursor() as cursor:
    #         cursor.excute("SELECT * FROM auth_user WHERE username=%s",['kkk'])
    #         row=cursor.fetchone()
    #         if row:
    #             columns=[col[0] for col in cursor.description]
    #             user_date=dict(zip(columns,row))
    #             print(user_date)

    # try:
    #     course=Course.objects.get(title="fwefs")
    #     print(course)
    # except Exception as e:
    #     print("course not found error")


    # conn = psycopg2.connect(
    #     "postgresql://django_project_h028_user:ZGwqiSSWgoVQldZEAMa9zNlNvc5ezNkz@dpg-csmcd6tds78s73edoln0-a.singapore-postgres.render.com/django_project_h028"
    # )
    # # Use the connection to interact with the database
    # cursor = conn.cursor()

    # try:
    #     # Query to drop all tables in the public schema
    #     cursor.execute("""
    #     DO $$ 
    #     DECLARE
    #         r RECORD;
    #     BEGIN
    #         FOR r IN (SELECT tablename FROM pg_tables WHERE schemaname = 'public') LOOP
    #             EXECUTE 'DROP TABLE IF EXISTS ' || quote_ident(r.tablename) || ' CASCADE';
    #         END LOOP;
    #     END $$;
    #     """)
    #     conn.commit()
    #     print("All tables dropped successfully.")
    # except Exception as e:
    #     print(f"Error: {e}")
    # finally:
    #     cursor.close()
    #     conn.close()

    # course_categories=[
    #      {
    #          "title":"Web Dev",
    #          "desc":"""Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sunt, nulla, maxime quae deserunt asperiores itaque voluptatem, assumenda magni quas nesciunt
    #                      incidunt? Veniam, repellat officia! Ipsa quasi voluptatum modi nisi repellat""",
    #      },
    #      {
    #          "title":"Mobile Dev",
    #          "desc":"""Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sunt, nulla, maxime quae deserunt asperiores itaque voluptatem, assumenda magni quas nesciunt
    #                      incidunt? Veniam, repellat officia! Ipsa quasi voluptatum modi nisi repellat""",
    #      },
    #      {
    #          "title":"API Dev",
    #          "desc":"""Lorem ipsum dolor sit, amet consectetur adipisicing elit. Sunt, nulla, maxime quae deserunt asperiores itaque voluptatem, assumenda magni quas nesciunt
    #                      incidunt? Veniam, repellat officia! Ipsa quasi voluptatum modi nisi repellat""",
    #      }
    #  ]
    # return render(request,"course/home_page.html")

def aboutPage(request):
    return  render(request,"course/about.html",{"title":"About Page"})

def contactPage(request):
    return render(request,"course/contact.html",{"title":"Contact Page"})

def userCourses(request): 

    courses=Course1.objects.all()
    cats=CourseCategory.objects.all()
    di={}
    for c in cats:
        di[c.name]=[]
    print(di)
    for course in courses:
        if course.category.name in di.keys():
            di[course.category.name].append(course)
    print(di)        
    return render(request,"course/user_courses.html",{"title":"Courses","java_courses":di["Java"],"python_courses":di["Python"],"flutter_courses":di["Flutter"]})
    
    # flutter_courses=[
    #     {
    #     "title":"Dart Concepts",
    #     "duration" : "2 months",
    #     "start_date" : "01-11-2024",
    #     "time" : "09 AM - 11 AM",
    #     },
    #     {
    #     "title":"Dart Advance",
    #     "duration" : "2 months",
    #     "start_date" : "01-11-2024",
    #     "time" : "09 AM - 11 AM",
    #     },
    #     {
    #     "title":"Flutter Concepts",
    #     "duration" : "2 months",
    #     "start_date" : "01-11-2024",
    #     "time" : "09 AM - 11 AM",
    #     },
    # ]
    # java_courses=[
    #     {
    #     "title":"Java Dart Concepts",
    #     "duration" : "2 months",
    #     "start_date" : "01-11-2024",
    #     "time" : "09 AM - 11 AM",
    #     },
    #     {
    #     "title":"Java Advance",
    #     "duration" : "2 months",
    #     "start_date" : "01-11-2024",
    #     "time" : "09 AM - 11 AM",
    #     },
    #     {
    #     "title":"Java Web Concepts",
    #     "duration" : "2 months",
    #     "start_date" : "01-11-2024",
    #     "time" : "09 AM - 11 AM",
    #     },
    # ]
    # python_courses=[
    #     {
    #     "title":"Python Dart Concepts",
    #     "duration" : "2 months",
    #     "start_date" : "01-11-2024",
    #     "time" : "09 AM - 11 AM",
    #     },
    #     {
    #     "title":"Python Advance",
    #     "duration" : "2 months",
    #     "start_date" : "01-11-2024",
    #     "time" : "09 AM - 11 AM",
    #     },
    #     {
    #     "title":"Python Web Concepts",
    #     "duration" : "2 months",
    #     "start_date" : "01-11-2024",
    #     "time" : "09 AM - 11 AM",
    #     },
    # ]
   

def register(request):
    courses=Course1.objects.all()
    # print("Method id",request.method)
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        phone=request.POST["phone"]
        address=request.POST["address"]
        course=request.POST["courses"]
        print(name,email,phone,address,course,sep=" , ")
        # c=Student(name=name,email=email,address=address,phone=phone,enrolled_courses=course)
        c=Student(name=name,email=email,phone=phone,address=address)
        c.save()
        c.enrolled_courses.add(course)
    return render(request,"course/register.html",{"title":"Register","courses":courses})

def login(request):
    if request.method=="POST":
        name=request.POST["name"]
        email=request.POST["email"]
        student=Student.objects.get(name=name,email=email)
        print("Student =>",student.name,student)
        if student:
            print("Login success")
            messages.add_message(request,messages.SUCCESS,'Login Success')
            return render(request,"course/home_page.html")
        else:
            return render(request,"course/login.html")
    return render(request,"course/login.html",{"title":"Login"})


def insertTr(request):
    if request.method=="POST":
        form=TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"course/home_page.html")
    else: 
        print("End")
        form=TeacherForm()
        return render(request,"course/insert_tr.html",{'form':form})