import requests
import time
import concurrent.futures
# REST_URL = "http://localhost:8000/api/result"

# DATA={
#     "resultID":157
# }

# r = requests.post(REST_URL,data=DATA)
# print(r.json())
    
REST_URL = "http://localhost:8000/api/upload"
file=open("/home/fahad/git/Fahis/mywebsite/Screenshot from 2022-12-04 22-34-35.png","rb")
DATA={
    "environment":"Windows 7",
    
}

def req():
    requests.post(REST_URL,files={"my_file":file},data=DATA)
t0=time.time()
with concurrent.futures.ThreadPoolExecutor() as executer:
    features=[executer.submit(req) for i in range(1)]

    concurrent.futures.wait(features)
t1=time.time()
print(t1-t0)