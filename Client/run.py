import face_recognition
import json
import numpy as np
import requests
import cv2
from Models import *

url="https://facerecognitiondbapi20201027214040.azurewebsites.net/employers"

cap = cv2.VideoCapture(0)
hasFrame,frame=cap.read()

data=GetFullData(url)

while(1):
    hasFrame,frame=cap.read()
    if not hasFrame:
        break
    try:
        face_encoding = face_recognition.face_encodings(frame)[0]
    except IndexError:
        print("not encoded") 

    for miniData in data:
        results = face_recognition.compare_faces(face_encoding, [miniData["features"]])
        if (results[0]==True):
            person=miniData["name"]
            print(f'This is {miniData["name"]}')
            cv2.putText(frame,f"Перед нами {person}", (10,50), cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,255),1,cv2.LINE_AA)
            break 

    cv2.imshow("Result",frame)
    k=cv2.waitKey(20)

    if k==27:
        break

cv2.destroyAllWindows()

