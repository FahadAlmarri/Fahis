import requests
import hashlib
import requests
import pickle
from apscheduler.schedulers.background import BackgroundScheduler
from django.urls import reverse
file_dic=pickle.load(open('file_dic.json',mode='rb'))

task_queue=[]


def getreport():
    
    if len(task_queue) ==0:
        print("no tasks waiting")
        return
    try:
        print(task_queue)
        REST_URL = f"http://localhost:8900/tasks/report/{task_queue[0]}"
        HEADERS = {"Authorization": "Bearer 4THnM7z6a1T3NcqP8KHUGg"}
        r = requests.get(REST_URL, headers=HEADERS )
        print(r.json()["info"]["score"])
        
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
