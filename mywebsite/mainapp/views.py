from django.shortcuts import render
from .models import Sample

# Create your views here.
def home(request):
	return render(request, 'mainapp/home.html', {})

def dbList(rquest):
	sample_list = Sample.objects.all()
	return render(rquest, 'mainapp/dbList.html', {'sample_list': sample_list})