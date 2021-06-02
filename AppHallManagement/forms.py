from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Student_Allocation,frmGeneralInstructions
from flatpickr import DatePickerInput, TimePickerInput, DateTimePickerInput

class registeruser(UserCreationForm):
	c =[("1", "Professor"), ("2", "Associate Professor"),("3","Assistant Professor"),("4","Lecturer"),("5","Office Stuff")]
	choice = forms.ChoiceField(choices=c, label="Designation")
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
	   ("15","Dept. of Chemistry (Chem)"),
	   ("16","Dept. of Mathematics (Math)"),
	   ("17","Dept. of Physics (Phy)"),
	   ("18","Dept. of Humanities (Hum"),
	   ("19","Other")]
	depart = forms.ChoiceField(choices=d, label="Department")
	e=[("1","Hall Provost"),("2","Hall Assistant Provost"),("3","Hall Officer")]
	hall=forms.ChoiceField(choices=e,label="Hall's Responsibility")
	class Meta:
		model=User
		fields=[
		'first_name',
		'last_name',
		'email',
		'username',
		'choice',
		'depart',
		'hall',
		'password1',
		'password2',





		]
class createform(forms.ModelForm):
	class Meta:
		model=Student_Allocation
		fields=[

                'name',
		       'phone_number',
		       'gender',
		       'your_image',
		       'gmail',
		       'department',
		       'roll_number',
		       'registration_number',
		       'current_education_year',
		       'result',
		       'birth',
		       'religion',
		       'nationality',
		       'father_name',
		       'father_income',
		       'guardian_name',
		       'relation_guardin',
		       'guardina_occupation',
		       'permanent_address',
		       'post_office_address',
		       'guardian_phone',
		       'hall_choice',
		       'address_local_guardian',
		       'previous_year_residence_details',
		       'bank_money_receipt_number',
		       'bank_money_receipt',
		       'date_deposite',
		       'roommate',
		       'submission_date',

		]
		widgets = {
            'birth': DatePickerInput(),
            'date_deposite':DatePickerInput(),
            'submission_date': DatePickerInput(),
        }
class forInstructionsForm(forms.ModelForm):
	class Meta:
		model=frmGeneralInstructions
		fields=[
		'author_main',
		'title',
		'instruction',
		'category',
		]
