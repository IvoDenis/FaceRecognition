import face_recognition
import json
import numpy as np
import requests
from Models import *
obama_image = face_recognition.load_image_file("obama.jpg")
biden_image = face_recognition.load_image_file("biden.jpg")

url="https://facerecognitiondbapi20201027214040.azurewebsites.net/employers"

try:
    face_encoding_obama = face_recognition.face_encodings(obama_image)[0]
    face_encoding_biden = face_recognition.face_encodings(biden_image)[0]
  
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()



#добавление данных
# info_post_1=AddData(url,"Obama",face_encoding_obama.tolist())
# info_post_2=AddData(url,"Biden",face_encoding_biden.tolist())

# print(info_post_1)
# print(info_post_2)

#получение данных
Data=GetFullData(url)

results = face_recognition.compare_faces(face_encoding_obama, [Data[0]["features"]])

if (results[0]==True):
    print(Data[0]["name"])

#удаление данных
DeleteData(url,Data,"Yura")
DeleteData(url,Data,"Obama")
DeleteData(url,Data,"Biden")
    