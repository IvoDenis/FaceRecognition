import os
import glob
import face_recognition
import json
import numpy as np
import requests
from Models import *


images='card'
jpg_filepaths=glob.glob(os.path.join(images,'*.png'))

url="https://facerecognitiondbapi20201027214040.azurewebsites.net/employers"

Data=GetFullData(url);

list_encodings=[]

list_names=[]

for j in Data:
    list_encodings.append(j["features"])
    list_names.append(j["name"])


for filepath in jpg_filepaths:
    image=face_recognition.load_image_file(filepath)
    try:
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)      

    except IndexError:
        print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
        quit()
    print(f"File {filepath}")
    for face_encoding in face_encodings:
        results = face_recognition.compare_faces(list_encodings, face_encoding)
        face_distances = face_recognition.face_distance(list_encodings,face_encoding)
        best_match_index=np.argmin(face_distances)
        if (results[best_match_index]):
            person=Data[best_match_index]["name"]
            print(f'This is {person}')  
    print("End")