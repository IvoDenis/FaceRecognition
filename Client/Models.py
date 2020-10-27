import json
import numpy as np
import requests

#https://facerecognitiondbapi20201027214040.azurewebsites.net/employers
def GetFullData(url:str):
    r = requests.get(url)  
    if (r.status_code==200):
        print("The Data was got")
        return r.json()
    else:
        return NotImplementedError


def DeleteData(url:str,data,name):
    localId=None
    Deleted=False
    for data_i in data:
        if data_i["name"]==name:
            localId=data_i["id"]
            curl = url+f"/{localId}"
            r = requests.delete(curl)
            if (r.status_code==200):
                print(f"{name} was deleted")
                Deleted=True      
    if Deleted==False:
        print(f"{name} was not found")
            



def AddData(url:str,name,features):
    data={
        "name":name,
        "features":features
    }

    r = requests.post(url, json=data)
    if (r.status_code==200):
        print(f"{name} was added")
    else:
        print("Feels bad man")    

