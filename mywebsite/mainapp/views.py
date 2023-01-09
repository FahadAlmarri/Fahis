from django.shortcuts import render, HttpResponseRedirect, redirect
from .models import Sample
import hashlib
from django.core.files.uploadedfile import TemporaryUploadedFile
from django.urls import reverse
# Create your views here.
file_dic={}

def home(request):
	try:
		if(request.method=='POST'):
			uploaded_file=request.FILES['file']
			temp = TemporaryUploadedFile(charset=uploaded_file.charset, name=uploaded_file.name, content_type=uploaded_file.content_type, size= uploaded_file.size)
			hashed_temp = hash(temp)
			if(checkDublicateFiles(hashed_temp)==False):
				# get reportID
				# file_dic[hashed_temp]=reportID
				pass	
			#redirct to report
			return redirect(reverse('report'))
	except:
		pass
		
	return render(request, 'mainapp/home.html', {})

def report(request):
	return render(request,'mainapp/report.html')

def checkDublicateFiles(hash):
	if hash in file_dic:
		return True
	else: return False

def hash(file):
	file.open(mode='rb')
	bytes = file.read() 
	readable_hash = hashlib.sha256(bytes).hexdigest()
	return readable_hash

def dbList(rquest):
	sample_list = Sample.objects.all()
	return render(rquest, 'mainapp/dbList.html', {'sample_list': sample_list})