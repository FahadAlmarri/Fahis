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
	if sample.Privacy_Type== 'private':
		if request.user == sample.UserID:
			context={"sample":sample, "report":report}
			return render(request,'frontend/result.html',context)
		else:
			return redirect('history')
	else:
		context={"sample":sample, "report":report}
		return render(request,'frontend/result.html',context)

def home(request):
	if(request.method=='POST'):
		privacy=request.POST.get('privacy')
		if not (request.user.is_authenticated):
			if privacy =="private":
				return redirect('/members/login_user')
		#url coming soon
		# uploaded_url=request.POST.get('url')
		# if uploaded_url == None or uploaded_url=="":
		uploaded_file=request.FILES['file']
		sampleID=uploadfile(uploaded_file,privacy,request)
		# else:
		# 	url = 'https://www.virustotal.com/vtapi/v2/url/scan'
		# return redirect(f"report/{sampleID}")
	return render(request, 'frontend/index.html', {},)


def history(request): 
	if not (request.user.is_authenticated):
		sample_list = Sample.objects.filter(Privacy_Type="public")
		print(sample_list)
		return render(request,'frontend/history.html', {'sample_list': sample_list})
	else:
		sample_list = Sample.objects.filter(Privacy_Type="public")
		print(sample_list)
		user_list = Sample.objects.filter(UserID_id=request.user)
		print(user_list)
		return render(request,'frontend/history.html', {'sample_list': sample_list,"user_list":user_list})
	

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
	