import face_recognition
import json
import numpy as np
import requests
from Models import *

maksim=face_recognition.load_image_file("./train/Maksim.jpg")
anastasia=face_recognition.load_image_file("./train/Anastasia.jpg")
artem=face_recognition.load_image_file("./train/Artem.jpg")
dmitriy=face_recognition.load_image_file("./train/Dmitriy.jpg")
pavel=face_recognition.load_image_file("./train/Pavel.jpg")
kan=face_recognition.load_image_file("./train/Kan-Demir.jpg")

url="https://facerecognitiondbapi20201027214040.azurewebsites.net/employers"

try:
    face_encoding_maksim = face_recognition.face_encodings(maksim)[0]
    face_encoding_anastasia = face_recognition.face_encodings(anastasia)[0]
    face_encoding_artem=face_recognition.face_encodings(artem)[0]
    face_encoding_dmitriy=face_recognition.face_encodings(dmitriy)[0]
    face_encoding_pavel=face_recognition.face_encodings(pavel)[0]
    face_encoding_kan=face_recognition.face_encodings(kan)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

#подготовка к очистке от старого эксперимента
Data=GetFullData(url)

DeleteData(url,Data,"Максим")
DeleteData(url,Data,"Анастасия")
DeleteData(url,Data,"Артем")
DeleteData(url,Data,"Дима")
DeleteData(url,Data,"Паша")
DeleteData(url,Data,"Кан-Демир")

#добавление данных
info_post_1=AddData(url,"Максим",face_encoding_maksim.tolist())
info_post_2=AddData(url,"Анастасия",face_encoding_anastasia.tolist())
info_post_3=AddData(url,"Артем",face_encoding_artem.tolist())
info_post_4=AddData(url,"Дима",face_encoding_dmitriy.tolist())
info_post_5=AddData(url,"Паша",face_encoding_pavel.tolist())
info_post_6=AddData(url,"Кан-Демир",face_encoding_kan.tolist())
