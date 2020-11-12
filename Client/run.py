import face_recognition
import json
import numpy as np
import requests
import cv2
from Models import *

url="https://facerecognitiondbapi20201027214040.azurewebsites.net/employers"

cap = cv2.VideoCapture(1)
hasFrame,frame=cap.read()

data=GetFullData(url)


list_encodings=[]

list_names=[]

for j in data:
    list_encodings.append(j["features"])
    list_names.append(j["name"])

while(1):
    hasFrame,frame=cap.read()
    if not hasFrame:
        break
    try:
        face_encoding = face_recognition.face_encodings(frame)[0]
    except IndexError:
        cv2.imshow("Result",frame)
        k=cv2.waitKey(20)
        print("not encoded")
        k=cv2.waitKey(20)

        if k==27:
            break
        continue

    results = face_recognition.compare_faces(list_encodings, face_encoding)
    face_distances = face_recognition.face_distance(list_encodings,face_encoding)
    best_match_index=np.argmin(face_distances)
    if (results[best_match_index]):
        person=data[best_match_index]["name"]
        print(f'This is {person}')
        cv2.putText(frame,f'In front of us {person}', (10,50), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1,cv2.LINE_AA)

    cv2.imshow("Result",frame)
    k=cv2.waitKey(20)

    if k==27:
        break



