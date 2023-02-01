from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import *
import pickle
from django.urls import reverse
from .apiFunc import *


# Create your views here.



def report(request,sampleID):
	#report=getreport(reportID)
	
	sample = Sample.objects.get(id=sampleID)
	
	report=Report.objects.get(Report_ID=sample.ReportID)
	
	context={"sample":sample, "report":report}
	return render(request,'frontend/result.html',context)

def home(request):
		if(request.method=='POST'):
			uploaded_file=request.POST.get('file')
			print(f"*******************************************uploaded file: {uploaded_file}")

			uploaded_url=request.POST.get('url')
			print(f"*****************************************uploaded url: {uploaded_url}")
			

			sampleID=uploadfile(uploaded_file)	
			#redirct to report
			return redirect(f"report/{sampleID}")
		return render(request, 'frontend/index.html', {},)



def history(request): 
	hash = request.POST.get("hash")
	print(hash)
	if(hash!=None and hash!=""):
		print(hash)
		sample_list = Sample.objects.filter(Privacy_Type="public", Sample_Address=hash)
		allReports = Report.objects.all()
		print(sample_list)
		return render(request,'frontend/history.html', {'sample_list': sample_list,'allReports':allReports})
	else:
		sample_list = Sample.objects.filter(Privacy_Type="public")
		print(sample_list)
		allReports = Report.objects.all()
		return render(request,'frontend/history.html', {'sample_list': sample_list,'allReports':allReports})

def forgot(request):
	return render(request,'frontend/forgot.html')


# Add your code to error checking for r.status_code.

	
