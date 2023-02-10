import requests
# REST_URL = "http://localhost:8000/api/result"

# DATA={
#     "resultID":67
# }

# r = requests.post(REST_URL,data=DATA)
# print(r.json())
    
REST_URL = "http://localhost:8000/api/upload"
file=open("/home/fahad/git/Fahis/mywebsite/mainapp/urls.py","rb")
DATA={
    "file":file,
    "environment":"windows 7",
    'name':str(file)
}

r = requests.post(REST_URL,data=DATA)
print(r)
    