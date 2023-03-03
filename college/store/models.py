from django.db import models
from multiselectfield import MultiSelectField

# Create your models here.
GENDER_CHOICES = (
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other')
)
PURPOSES = (
    ('Enquiry', 'Enquiry'),
    ('Place Order', 'Place Order'),
    ('Return', 'Return')
)
DEPARTMENTS = (
    ('Computer Science', 'Computer Science'),
    ("Mathematics", "Mathematics"),
    ("Physics", "Physics"),
    ("Chemistry", "chemistry"),
    ("Commerce", "Commerce")
)
COURSES = (
    ('Bachelor', 'Bachelor'),
    ("Master", "Master"),
    ("M.Phil", "M.Phil"),
    ("PhD", "PhD")
)
MATERIAL = (
    ('notebook', 'Debit Note Book'),
    ('pen', 'Pen'),
    ('exam_paper', 'Exam Papers')
)


class StudentDetails(models.Model):
    name = models.CharField(max_length=50)
    dob = models.DateField()
    age = models.CharField(max_length=3)
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, default='male')
    phone_number = models.CharField(max_length=13)
    mail_id = models.CharField(max_length=30)
    address = models.TextField()
    department = models.CharField(max_length=25, choices=DEPARTMENTS)
    course = models.CharField(max_length=25, choices=COURSES)
    purpose = models.CharField(max_length=11, choices=PURPOSES)
    materials_provide = MultiSelectField(choices=MATERIAL, max_length=50)


class Department(models.Model):
    name = models.CharField(max_length=100)
