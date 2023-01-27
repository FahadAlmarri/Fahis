from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import *
import pickle
from django.urls import reverse
from .apiFunc import *

# Create your views here.



def report(request,reportID):
	#report=getreport(reportID)
	context={"task_id":reportID}
	return render(request,'mainapp/report.html',context)

def home(request):
		if(request.method=='POST'):
			uploaded_file=request.FILES['file']
			reportID=uploadfile(uploaded_file)	
			#redirct to report
			return redirect(f"report/{reportID}")
		return render(request, 'mainapp/home.html', {})




def dbList(rquest):
	sample_list = Sample.objects.all()
	return render(rquest, 'mainapp/dbList.html', {'sample_list': sample_list})

# Add your code to error checking for r.status_code.

	
