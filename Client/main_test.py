import os
import glob
import face_recognition
import json
import numpy as np
import requests
from Models import *


images='test'
jpg_filepaths=glob.glob(os.path.join(images,'*.jpg'))

url="https://facerecognitiondbapi20201027214040.azurewebsites.net/employers"

Data=GetFullData(url);

for filepath in jpg_filepaths:
    image=face_recognition.load_image_file(filepath)
    try:
        face_locations = face_recognition.face_locations(image)
        face_encodings = face_recognition.face_encodings(image, face_locations)      

    except IndexError:
        print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
        quit()
    print(f"File {filepath}")
    for j in face_encodings:
        for i in (Data):
            results = face_recognition.compare_faces(j, [i["features"]])
                      
            if (results[0]==True):
                print(f'This is a  {i["name"]}')
    print("End")