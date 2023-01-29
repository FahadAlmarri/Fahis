from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import *
import pickle
from django.urls import reverse
from .apiFunc import *


# Create your views here.



def report(request,reportID):
	#report=getreport(reportID)
	sample = Sample.objects.filter(ReportID=reportID)[0]
	score = float(Report.objects.get(Report_ID=reportID).Others)
	if score>10:
		score=10
	context={"task_id":reportID, "sample":sample, "score": score*10}
	return render(request,'frontend/result.html',context)

def home(request):
		if(request.method=='POST'):
			uploaded_file=request.FILES['file']
			reportID=uploadfile(uploaded_file)	
			#redirct to report
			return redirect(f"report/{reportID}")
		return render(request, 'frontend/index.html', {},)



def history(request):
	sample_list = Sample.objects.filter(Privacy_Type="public")
	allReports = Report.objects.all()
	return render(request,'frontend/history.html', {'sample_list': sample_list,'allReports':allReports})

def forgot(request):
	return render(request,'frontend/forgot.html')


# Add your code to error checking for r.status_code.

	
