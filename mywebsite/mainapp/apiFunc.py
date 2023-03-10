import requests
import hashlib
import pickle
from apscheduler.schedulers.background import BackgroundScheduler
from django.urls import reverse
from .models import *
import time
import datetime
import os
from os import listdir



import base64




file_dic=pickle.load(open('file_dic.json',mode='rb'))
url_queue=[]
task_queue=[]
#we cant check use authenticated unless we move to view so we can use request variable
#we add report create object also pu a check if user auth we add user to sample
#we after we need try multiple accounts at the same time
def uploadURL(url,privacy,request):

    
    


    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if(checkDublicateFiles(url)==False):
        
        params = {'apikey': 'b230a88ab3d6f90eaa945eaec05eea799676f78a1c1559bb245a67820b6eacbb', 'url':url}
        requests.post(url, data=params)
        Report.objects.create(Report_Address=url,Report_Type="url")
        foreignReport=Report.objects.get(Report_Address=url)
        file_dic[url]=foreignReport.Report_ID
        url_queue.append((url,foreignReport.Report_ID))
        pickle.dump(file_dic,open('file_dic.json',mode='wb'))
    else:
        
        foreignReport=Report.objects.get(Report_Address=url)
    if  (request.user.is_authenticated):
        Sample.objects.create(ReportID = foreignReport, Privacy_Type =privacy, Create_Date =current_time, Sample_Type ='url', Sample_Address = url,UserID=request.user,Sample_name=url)
    else:
        Sample.objects.create(ReportID = foreignReport, Privacy_Type ="public", Create_Date =current_time, Sample_Type ='url', Sample_Address = url,Sample_name=url)

    
    last_added_sample=Sample.objects.filter(ReportID=foreignReport).latest("id")
   
    return last_added_sample.id








    
def uploadfile(temp,privacy,request,environment):
    
    hashed_temp = hash(temp)
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if(checkDublicateFiles(hashed_temp)==False):
        task_id=file_api(temp)
        Report.objects.create(Report_Address=hashed_temp,Report_Type="file",task_id=task_id)
        foreignReport=Report.objects.get(Report_Address=hashed_temp)
        task_queue.append((task_id,foreignReport.Report_ID))

        file_dic[hashed_temp]=foreignReport.Report_ID
        pickle.dump(file_dic,open('file_dic.json',mode='wb'))
    else:
       
        reportID=file_dic[hashed_temp]
        foreignReport=Report.objects.get(Report_ID = reportID)
    if  (request.user.is_authenticated):
        Sample.objects.create(ReportID = foreignReport, Privacy_Type =privacy, Create_Date =current_time, Sample_Type ='file', Sample_Address = hashed_temp,UserID=request.user,Sample_name=temp,Environment=environment)
    else:
        Sample.objects.create(ReportID = foreignReport, Privacy_Type ="public", Create_Date =current_time, Sample_Type ='file', Sample_Address = hashed_temp,Sample_name=temp,Environment=environment)

    
    last_added_sample=Sample.objects.filter(ReportID=foreignReport).latest("id")
    return last_added_sample.id
# def getUrlReport():
    
#     if len(url_queue) ==0:
#         print("no url tasks waiting")
#         return
#     try:

#         print(url_queue[0][0])

#         url = "https://www.virustotal.com/api/v3/urls/id"

#         headers = {"accept": "application/json"}

#         r = requests.get(url, headers=headers)

        
        
        
#         score = float(r.json()["info"]["score"])*10
#         print(score)
#         processes = r.json()['behavior']['processes']
#         network = r.json()['network']['domains']
#         duration=r.json()['info']['duration']
#         processes_json=[]
#         for process in processes:
#             processes_json.append({'pid':process['pid'],"process_name":process['process_name'],'command_line':process['command_line']})
#         print(score)
        
#         Report.objects.filter(Report_ID = url_queue[0][1]).update(Network=network,Processes=processes_json,Duration=duration,Score=score)
        
        
#         url_queue.pop(0)
#         print(f"url queue : {url_queue}")
    
#     except:

#         print(f" url {url_queue[0]} is not ready")
def getFileReport():
    
    if len(task_queue) ==0:
        return
    try:

        print(task_queue[0][0])
        REST_URL = f"http://localhost:8900/tasks/report/{task_queue[0][0]}"
        HEADERS = {"Authorization": "Bearer 4THnM7z6a1T3NcqP8KHUGg"}
        r = requests.get(REST_URL, headers=HEADERS )
        
        score = float(r.json()["info"]["score"])*10
        
        processes = r.json()['behavior']['processes']
        network = r.json()['network']['domains']
        duration=r.json()['info']['duration']
        processes_json=[]
        for process in processes:
            processes_json.append({'pid':process['pid'],"process_name":process['process_name'],'command_line':process['command_line']})
        
        Report.objects.filter(Report_ID = task_queue[0][1]).update(Network=network,Processes=processes_json,Duration=duration,Score=score)
        
        
        task_queue.pop(0)
        print(task_queue)
    
    except:

        print(f"{task_queue[0]} is not ready")

def start():
    schedular= BackgroundScheduler()
    schedular.add_job(getFileReport,'interval',seconds=10)
    # schedular.add_job(getUrlReport,'interval',seconds=10)
    schedular.start()
	

def hash(file):
	# file.open(mode='rb')
	bytes = file.read() 
	
	readable_hash = hashlib.sha256(bytes).hexdigest()
	return readable_hash


def checkDublicateFiles(address):
    
	if address in file_dic:
		return True
	else: return False


def file_api(file):
    REST_URL = "http://localhost:8900/tasks/create/file"
    HEADERS = {"Authorization": "Bearer 4THnM7z6a1T3NcqP8KHUGg"}

    if str(type(file))=="<class 'django.core.files.uploadedfile.InMemoryUploadedFile'>":
        sample=file.open(mode="rb")
        files = {"file": (str(file), sample)}
        r = requests.post(REST_URL, headers=HEADERS, files=files,timeout=10)
        taskID=r.json()['task_id']
        sample.close()
        return taskID
    else:
        files = {"file": (str(file), file)}
        r = requests.post(REST_URL, headers=HEADERS, files=files,timeout=10)
        taskID=r.json()['task_id']
        return taskID




def task_screenshots(task_id=0):
    folder_path = f"/home/fahad/.cuckoo/storage/analyses/{task_id}/shots/"
    sceenshots=[]
    if not os.path.exists(folder_path):
        return (404, "Task not found")
    for image in listdir(folder_path):
        if "small" not in image:
            image_path=f"{folder_path}{image}"
            with open (image_path,"rb") as f:
                image_read=f.read()
            image_b64=base64.b64encode(image_read).decode("utf-8")
            sceenshots.append(image_b64)
        # TODO: Add content disposition.
    #screenshot = open(folder_path, "rb").read()
    
    return sceenshots


#print("hhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh",task_screenshots())
