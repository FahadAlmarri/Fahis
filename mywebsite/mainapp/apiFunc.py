import requests
import hashlib
import pickle
from apscheduler.schedulers.background import BackgroundScheduler
from django.urls import reverse
from .models import *
import time
 
file_dic=pickle.load(open('file_dic.json',mode='rb'))

task_queue=[]
#we cant check use authenticated unless we move to view so we can use request variable
#we add report create object also pu a check if user auth we add user to sample
#we after we need try multiple accounts at the same time
def uploadfile(temp):
    hashed_temp = hash(temp)
    print(hashed_temp)
    if(checkDublicateFiles(hashed_temp)==False):
        reportID=file_api(temp)
        print(reportID)
        file_dic[hashed_temp]=reportID
        Report.objects.create(Report_ID = reportID,Report_Address=hashed_temp,Report_Type="file")
        pickle.dump(file_dic,open('file_dic.json',mode='wb'))
    else:
        reportID=file_dic[hashed_temp]
    foreignReport=Report.objects.get(Report_ID = reportID)

    Sample.objects.create(ReportID = foreignReport, Privacy_Type ='public', Create_Date ='2022-12-27 12:21:46', Sample_Type ='file', Sample_Address = hashed_temp)

    last_added_sample=Sample.objects.filter(ReportID=foreignReport).latest("id")
    print(last_added_sample)
    return last_added_sample.id

def getreport():
    
    if len(task_queue) ==0:
        print("no tasks waiting")
        return
    try:
        print(task_queue)
        REST_URL = f"http://localhost:8900/tasks/report/{task_queue[0]}"
        HEADERS = {"Authorization": "Bearer 4THnM7z6a1T3NcqP8KHUGg"}
        r = requests.get(REST_URL, headers=HEADERS )
        score = float(r.json()["info"]["score"])*10
        processes = r.json()['behavior']['processes']
        network = r.json()['network']['domains']
        duration=r.json()['info']['duration']
        processes_json=[]
        for process in processes:
            processes_json.append({'pid':process['pid'],"process_name":process['process_name'],'command_line':process['command_line']})
        print(score)
        
        Report.objects.filter(Report_ID = task_queue[0]).update(Network=network,Processes=processes_json,Duration=duration,Score=score)
        
        
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
    files = {"file": (file, sample)}
    r = requests.post(REST_URL, headers=HEADERS, files=files,timeout=10)
    taskID=r.json()['task_id']
    task_queue.append(taskID)
    return taskID
