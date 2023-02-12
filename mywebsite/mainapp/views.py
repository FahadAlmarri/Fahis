from django.shortcuts import render, HttpResponseRedirect, redirect,HttpResponse
from .models import *
import pickle
from django.urls import reverse
from .apiFunc import uploadfile,task_screenshots
import requests
from django.http import JsonResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.request import Request

# Create your views here.



def report(request,sampleID):
	#report=getreport(reportID)
	sample = Sample.objects.get(id=sampleID)
	report=Report.objects.get(Report_ID=sample.ReportID)
	
		
	if sample.Privacy_Type== 'private':
		if request.user == sample.UserID:
			context={"sample":sample, "report":report,"screenshots":task_screenshots(report.task_id)}
			return render(request,'frontend/result.html',context)
		else:
			return redirect('history')
	else:
		context={"sample":sample, "report":report,"screenshots":task_screenshots(report.task_id)}
		return render(request,'frontend/result.html',context)

def home(request):
	if(request.method=='POST'):
		privacy=request.POST.get('privacy')
		environment=request.POST.get("environment")
		if not (request.user.is_authenticated):
			if privacy =="private":
				return redirect('/members/login_user')
		#url coming soon
		# uploaded_url=request.POST.get('url')
		# if uploaded_url == None or uploaded_url=="":
		
		uploaded_file=request.FILES['file']

		sampleID=uploadfile(uploaded_file,privacy,request,environment)
		# else:
		# 	url = 'https://www.virustotal.com/vtapi/v2/url/scan'
		return redirect(f"report/{sampleID}")
	return render(request, 'frontend/index.html', {},)


def history(request): 
	if not (request.user.is_authenticated):
		sample_list = Sample.objects.filter(Privacy_Type="public")
		
		return render(request,'frontend/history.html', {'sample_list': sample_list})
	else:
		sample_list = Sample.objects.filter(Privacy_Type="public")
		user_list = Sample.objects.filter(UserID_id=request.user)
		return render(request,'frontend/history.html', {'sample_list': sample_list,"user_list":user_list})
	

def custom404(request,exception=None):
	return render(request,'frontend/page404.html')


def api(request):
	return render(request,'frontend/api.html')
	
#Add your code to error checking for r.status_code.
@api_view(["POST"])	
def apiUpload(request):


	# uploaded_file=(request.data)["file"]
	environment=(request.data)["environment"]
	
	uploaded_file=request.FILES['my_file']
	
	sampleID=uploadfile(temp=uploaded_file,request=request,environment=environment,privacy="public")


	return Response({"resultID":sampleID})
	# except:
	# 	return Response({"error":"please upload a file"})

	

@api_view(["POST"])	
def apiResult(request):
	
	resultID=(request.data)["resultID"]
	
	try:
		sample=Sample.objects.get(id=resultID)
		if sample.Privacy_Type=="public":
			reportID=sample.ReportID
			report=Report.objects.get(Report_ID=reportID)
			return Response({'score':report.Score,'network':report.Network,'processes':report.Processes,'duration':report.Duration})
		else:
			return Response({"error":"sample is private"})
	except:
		return Response({'error':'the id does not exist'})
			
	return JsonResponse({'error':'invalid request method'})
	
	