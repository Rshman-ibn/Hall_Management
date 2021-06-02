from django.db import models
from django.contrib.auth.models import User
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column

# Create your models here.

class author(models.Model):
 	name=models.ForeignKey(User,on_delete=models.CASCADE)
 	details=models.TextField()
 	def __str__(self):
 		return self.name.username
class category(models.Model):
 	name=models.CharField(max_length=100)
 	def __str__(self):
 		return self.name
class notice(models.Model):
	author_main=models.ForeignKey(author,on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	notic=models.TextField()
	posted_on=models.DateTimeField(auto_now=False,auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True,auto_now_add=False)
	category=models.ForeignKey(category,on_delete=models.CASCADE)


	def __str__(self):
		return self.title
class frmGeneralInstructions(models.Model):
	author_main=models.ForeignKey(author,on_delete=models.CASCADE)
	title=models.CharField(max_length=100)
	instruction=models.FileField(upload_to='media/files')
	posted_on=models.DateTimeField(auto_now=False,auto_now_add=True)
	updated_on=models.DateTimeField(auto_now=True,auto_now_add=False)
	category=models.ForeignKey(category,on_delete=models.CASCADE)
	def __str__(self):
		return self.title
	def instruction_url(self):
		if self.instruction and hasattr(self.instruction, 'url'):
			return self.instruction.url



class Student_Allocation(models.Model):
    g=[ ("1","Male"), ("2" , "Female"), ("3" , "Others") ]
    name=models.CharField(max_length=100)
    phone_number=models.IntegerField()
    gender=models.CharField(max_length=100,choices=g)
    your_image=models.ImageField(upload_to='files/Media',null=True)
    gmail=models.EmailField(max_length=100,default='ranaruet344@gmail.com')
    d=[("1","Dept. of Electrical and Electronic Engineering (EEE)"),
       ("2","Dept. of Computer Science & Engineering (CSE)"),
	   ("3","Department of Electrical and Computer Engineering"),
	   ("4","Dept. of Electronics and Telecommunication Engineering"),
	   ("5","Dept. of Civil Engineering (CE)"),
	   ("6","Dept. of Architecture (Architecture)"),
	   ("7","Dept. of Urban & Regional Planning (URP)"),
	   ("8","Building Engineering & Construction Management"),
	   ("9","Dept. of Industrial & Production Engineering (IPE)"),
	   ("10","Dept. of Glass and Ceramic Engineering (GCE)"),
	   ("11","Dept. of Mechatronics Engineering (MTE)"),
	   ("12","Dept. of Mechanical Engineering (ME)"),
	   ("13","Department of Chemical and Food Process Engineering"),
	   ("14","Materials Science & Engineering (MSE)"),

	   ("15","Other")]

    department=models.CharField(max_length=100,choices=d)
    roll_number=models.IntegerField()
    registration_number=models.IntegerField()
    t=[("1","1st Year"),("2","2nd Year"),("3","3rd Year"),("4","4rth Year")]
    current_education_year=models.CharField(max_length=100,choices=t)
    result=models.FloatField()
    birth=models.DateField()
    religion=models.CharField(max_length=100)
    nationality=models.CharField(max_length=100)
    father_name=models.CharField(max_length=100)
    father_income=models.PositiveIntegerField()
    guardian_name=models.CharField(max_length=100)
    relation_guardin=models.CharField(max_length=100)
    guardina_occupation=models.CharField(max_length=100)
    permanent_address=models.TextField()
    post_office_address=models.TextField()
    guardian_phone=models.PositiveIntegerField()
    hall_choice=models.TextField()
    address_local_guardian=models.TextField()
    previous_year_residence_details=models.TextField()
    bank_money_receipt_number=models.PositiveIntegerField()
    bank_money_receipt=models.FileField(null=True, blank=True, upload_to='files/Media')
    date_deposite=models.DateField()
    roommate=models.TextField()
    submission_date=models.DateField()


    def  __str__(self):
        return self.name
