from django.shortcuts import render, HttpResponseRedirect, redirect,HttpResponse
from .models import *
import pickle
from django.urls import reverse
from .apiFunc import uploadfile




# Create your views here.



def report(request,sampleID):
	#report=getreport(reportID)
	sample = Sample.objects.get(id=sampleID)
	report=Report.objects.get(Report_ID=sample.ReportID)
	
	context={"sample":sample, "report":report}
	return render(request,'frontend/result.html',context)

def home(request):
		if(request.method=='POST'):
			privacy=request.POST.get('privacy')
			if not (request.user.is_authenticated):
				if privacy =="private":
					return redirect('/members/login_user')
			
			uploaded_url=request.POST.get('url')
			if uploaded_url == None or uploaded_url=="":
				uploaded_file=request.FILES['file']
				sampleID=uploadfile(uploaded_file,privacy,request)
			else:
				url = 'https://www.virustotal.com/vtapi/v2/url/scan'


			

			
			
			

				
			#redirct to report
			
			return redirect(f"report/{sampleID}")
		return render(request, 'frontend/index.html', {},)


def history(request): 
	hash = request.POST.get("hash")
	print(hash)
	if not (request.user.is_authenticated):
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
	else:
		if(hash!=None and hash!=""):
			print(hash)
			sample_list = Sample.objects.filter(Privacy_Type="public", Sample_Address=hash)
			allReports = Report.objects.all()
			user_list = Sample.objects.filter(UserID_id=request.user,Sample_Address=hash)
			print(sample_list)
			return render(request,'frontend/history.html', {'sample_list': sample_list,'allReports':allReports,"user_list":user_list})
		else:
			sample_list = Sample.objects.filter(Privacy_Type="public")
			print(sample_list)
			allReports = Report.objects.all()
			user_list = Sample.objects.filter(UserID_id=request.user)
			return render(request,'frontend/history.html', {'sample_list': sample_list,'allReports':allReports,"user_list":user_list})
	

def forgot(request):
	return render(request,'frontend/forgot.html')


# Add your code to error checking for r.status_code.
def apiUpload(request):
	# if request.method =="POST":
	# 	try:

	# 		uploaded_file=request.FILES['file']
	# 		sampleID=uploadfile(uploaded_file,request)
	# 		return JsonResponse({"resultID":sampleID})
	# 	except:
	# 		return JsonResponse({"error":"please upload a file"})

	# return JsonResponse({'error':'invalid request method'})
	return HttpResponse("")

def apiResult(request):
	# if request.method =="POST":
	# 	resultID=request.post.get("resultID")
	# 	try:

	# 		reportID=Sample.objects.get(id=resultID).ReportID
	# 		report=Report.objects.get(Report_ID=reportID)
	# 		return JsonResponse({'score':report.Score,'network':report.Network,'processes':report.Processes,'duration':report.Duration})
	# 	except:
	# 		return JsonResponse({'error':'the id does not exist'})
			
	# return JsonResponse({'error':'invalid request method'})
	return HttpResponse("")
	