from django.db import models

# Create your models here.

class CourseCategory(models.Model):
    name=models.CharField(max_length=225,null=True, blank=True)
    description=models.TextField()
    def __str__(self):
        return self.name

class Course1(models.Model):
    title=models.CharField(max_length=200,null=True, blank=True)
    description=models.TextField(null=True, blank=True)
    start_date=models.DateField(null=True, blank=True)
    end_data=models.DateField(null=True, blank=True)
    price=models.IntegerField(null=True, blank=True) 
    image=models.ImageField(upload_to='courses/images/',null=True, blank=True)
    category=models.ForeignKey(CourseCategory,on_delete=models.CASCADE,related_name='courses')
    

    def __str__(self):
        return self.title
    
class Student(models.Model):
    name=models.CharField(max_length=100,null=True, blank=True)
    email=models.EmailField(max_length=100,null=True, blank=True)
    address=models.TextField(null=True, blank=True)
    phone=models.CharField(max_length=100,null=True, blank=True)
    enrolled_courses=models.ManyToManyField(Course1,related_name='students')

    def __str__(self):
        return self.name
    
