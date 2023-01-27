from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Sample
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
			temp = uploaded_file
			hashed_temp = hash(temp)
			print(hashed_temp)
			if(checkDublicateFiles(hashed_temp)==False):

				reportID=file_api(temp)
				file_dic[hashed_temp]=reportID
				
				pickle.dump(file_dic,open('file_dic.json',mode='wb'))
			else:
				reportID=file_dic[hashed_temp]
				
			#redirct to report
			return redirect(f"report/{reportID}")
			 
	
		
		return render(request, 'mainapp/home.html', {})




def dbList(rquest):
	sample_list = Sample.objects.all()
	return render(rquest, 'mainapp/dbList.html', {'sample_list': sample_list})

# Add your code to error checking for r.status_code.

	
