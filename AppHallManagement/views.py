from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import notice,author,category,Student_Allocation,frmGeneralInstructions
from django.contrib.auth import authenticate,login,logout
from .forms import registeruser,createform,forInstructionsForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import Q


# Create your views here.
def index(request):
	return HttpResponse("Hi my name is Rana")
def  HomeView(request):
	post=notice.objects.latest('id')
	context={
	'post':post
	}
	return render(request,'forhome.html',context)
def Contact(request):

	return render(request,'frmContact.html')
def GeneralInstructions(request):
	fil=frmGeneralInstructions.objects.all()
	context={"files":fil}
	return render(request,'frmGeneralInstructions.html',context)
def generalInstructionsform(request):
	if request.method=="POST":
		form=forInstructionsForm(request.POST,request.FILES)
		if form.is_valid():
			form.save()
			return redirect('GeneralInstructions')
	else:
		form=forInstructionsForm()
	return render(request,'updload_instructs.html',{"form":form})

def frmStudentManual(request):
	return render(request,'frmStudentManual.html')
def frmUserManual(request):
	return render(request,'frmUserManual.html')
def newallocation(request):
	form = createform(request.POST,request.FILES)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()
		if request.user.is_authenticated:
			return redirect('profile')
		else:
			return redirect('home')
	context={

	'form':form,
	}
	return render(request,'allocation.html',context)
def  frmLogin(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method =="POST":
			name=request.POST.get('name')
			passb=request.POST.get('pass')
			auth=authenticate(request,username=name,password=passb)
			if auth is not None:
				login(request,auth)
				return redirect('profile')
			else:
				return render(request,'frmLogin.html',{'ami':"You press Wrong username or password here"})

	return render(request,'frmLogin.html')

def forlogout(request):
	logout(request)
	return redirect('home')
def register(request):
	form=registeruser(request.POST or None)
	if form.is_valid():
		instance=form.save(commit=False)
		instance.save()
		messages.success(request,"You are register successfully")
		return redirect('frmLogin')
	return render(request,'registerr.html',{'form':form})




def adminpanel(request,name):
	post_author=get_object_or_404(User,username=name)
	auth=get_object_or_404(author,name=post_author.id)

	context={
	   "auth":auth,


	}
	return render(request,'aadmi.html',context)

def profile(request):
	if request.user.is_authenticated:
		post=Student_Allocation.objects.all()
		search=request.GET.get('q')
		if search:
			post=post.filter(
				Q(name__icontains=search)|Q(phone_number__icontains=search)|Q(roll_number__icontains=search)
				|Q(father_name__icontains=search)|Q(bank_money_receipt_number__icontains=search)

				)
		return render(request,'foradmi.html',{"post":post})
	else:
		return redirect('frmLogin')
def profile_show(request):
	return render(request,'profile_show.html')
def studentOut(request,pid):
	if request.user.is_authenticated:
		if request.user.is_staff or request.user.is_superuser:
			post=get_object_or_404(Student_Allocation,id=pid)
			post.delete()
			return redirect('profile')
		else:
			return HttpResponse("Sorry You are not authorized")
	else:
		return redirect('frmLogin')

def newup(request,pid):
	if request.user.is_authenticated:
		#u=get_object_or_404(author,name=request.user.id)
		if request.user.is_staff or request.user.is_superuser:
			post=get_object_or_404(Student_Allocation,id=pid)
			form = createform(request.POST or None, request.FILES or None,instance=post)
			if form.is_valid():
				instance = form.save(commit=False)
				instance.save()
				return redirect('profile')
			contet={
				'form':form,
			}
			return render(request,'allocation.html',contet)
		else:
			return HttpResponse("You are not authorized , please contact with main admin")
	else:
		return redirect('frmLogin')
