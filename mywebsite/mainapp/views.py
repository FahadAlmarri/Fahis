from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import *
import pickle
from django.urls import reverse
from .apiFunc import *

# Create your views here.



def report(request,reportID):
	#report=getreport(reportID)
	context={"task_id":reportID}
	return render(request,'frontend/result.html',context)

def home(request):
		if(request.method=='POST'):
			uploaded_file=request.FILES['file']
			reportID=uploadfile(uploaded_file)	
			#redirct to report
			return redirect(f"report/{reportID}")
		return render(request, 'frontend/index.html', {},)

def login(request):
	return render(request,'frontend/login.html')

def register(request):
	return render(request,'frontend/register.html')

def history(request):
	return render(request,'frontend/history.html')

def forgot(request):
	return render(request,'frontend/forgot.html')


def dbList(rquest):
	sample_list = Sample.objects.all()
	return render(rquest, 'mainapp/dbList.html', {'sample_list': sample_list})

# Add your code to error checking for r.status_code.

	
