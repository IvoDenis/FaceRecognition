import face_recognition
import json
import numpy as np
import requests
from Models import *
# obama_image = face_recognition.load_image_file("obama.jpg")
# biden_image = face_recognition.load_image_file("biden.jpg")
jason_image = face_recognition.load_image_file("jason_statham.jpg")
jason_image2 = face_recognition.load_image_file("jason_statham2.jpg")

url="https://facerecognitiondbapi20201027214040.azurewebsites.net/employers"

try:
    # face_encoding_obama = face_recognition.face_encodings(obama_image)[0]
    # face_encoding_biden = face_recognition.face_encodings(biden_image)[0]
    face_encoding_jason=face_recognition.face_encodings(jason_image)[0]
    face_encoding_jason2=face_recognition.face_encodings(jason_image2)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

Data=GetFullData(url)
DeleteData(url,Data,"Jason Statham")

#добавление данных
info_post_1=AddData(url,"Jason Statham",face_encoding_jason.tolist())


#получение данных
Data=GetFullData(url)


for i in (Data):
    results = face_recognition.compare_faces(face_encoding_jason2, [i["features"]])

    if (results[0]==True):
        print(f'This is a  {i["name"]}')

# #удаление данных
# DeleteData(url,Data,"Yura")
# DeleteData(url,Data,"Obama")
# DeleteData(url,Data,"Biden")
