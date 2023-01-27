import requests
import hashlib
import pickle
from apscheduler.schedulers.background import BackgroundScheduler
from django.urls import reverse
from .models import *
import random
file_dic=pickle.load(open('file_dic.json',mode='rb'))

task_queue=[]

def uploadfile(uploaded_file):
    temp = uploaded_file
    hashed_temp = hash(temp)
    print(hashed_temp)
    if(checkDublicateFiles(hashed_temp)==False):
        reportID=file_api(temp)
        print(reportID)
        file_dic[hashed_temp]=reportID
        Report.objects.create(Report_ID = reportID)
        pickle.dump(file_dic,open('file_dic.json',mode='wb'))
    else:
        reportID=file_dic[hashed_temp]
    Sample.objects.create(ReportID = reportID, Privacy_Type ='public', Create_Date ='2022-12-27 12:21:46', Sample_Type ='file', UserID =1, Sample_Address = hashed_temp)
    return reportID
def getreport():
    
    if len(task_queue) ==0:
        print("no tasks waiting")
        return
    try:
        print(task_queue)
        REST_URL = f"http://localhost:8900/tasks/report/{task_queue[0]}"
        HEADERS = {"Authorization": "Bearer 4THnM7z6a1T3NcqP8KHUGg"}
        r = requests.get(REST_URL, headers=HEADERS )
        score = r.json()["info"]["score"]
        print(score)
        score_as_string=str(score)
        Report.objects.filter(Report_ID = task_queue[0]).update(Others=score_as_string)
        
        
        task_queue.pop(0)
        print(task_queue)
    except:
        print(f"{task_queue[0]} is not ready")

def start():
    schedular= BackgroundScheduler()
    schedular.add_job(getreport,'interval',seconds=10)
    schedular.start()
	

def hash(file):
	file.open(mode='rb')
	bytes = file.read() 
	
	readable_hash = hashlib.sha256(bytes).hexdigest()
	return readable_hash


def checkDublicateFiles(hash):
	if hash in file_dic:
		return True
	else: return False


def file_api(file):
    REST_URL = "http://localhost:8900/tasks/create/file"
    HEADERS = {"Authorization": "Bearer 4THnM7z6a1T3NcqP8KHUGg"}
    sample=file.open(mode="rb")
    files = {"file": ("sample", sample)}
    r = requests.post(REST_URL, headers=HEADERS, files=files,timeout=10)
    taskID=r.json()['task_id']
    task_queue.append(taskID)
    return taskID
