import face_recognition
import json
import numpy as np
import requests

#https://facerecognitiondbapi20201027214040.azurewebsites.net/employers
def GetFullData(url:str):
    r = requests.get(url)  
    return r.json()

def DeleteData(url:str,Data,Name):
    for data in Data:
        if data["name"]==Name:
            localId=data["id"]
            break
        else:
            print(f"{Name} was not found")
    curl = url+f"/{localId}"
    r = requests.delete(curl)
    if (r.status_code==200):
        print(f"{Name} was deleted")
    else:
        print("Feels bad man")


