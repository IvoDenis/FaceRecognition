import face_recognition
import json
import numpy as np
import requests
from Models import *
import cv2

maksim_image1=face_recognition.load_image_file("jason_statham.jpg")
maksim_image2=face_recognition.load_image_file("jason_statham2.jpg")

url="https://facerecognitiondbapi20201027214040.azurewebsites.net/employers"

try:

    face_encoding_maksim1=face_recognition.face_encodings(maksim_image1)[0]
    face_encoding_maksim2=face_recognition.face_encodings(maksim_image2)[0]
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

results = face_recognition.compare_faces(face_encoding_maksim1,[face_encoding_maksim2])

if (results[0]==True):
    print(f'This is a Jason Statham')

photo = cv2.imread("jason_statham.jpg")
rgb_small_frame = photo[:, :, ::-1]
face_locations = face_recognition.face_locations(rgb_small_frame)


for (top, right, bottom, left) in face_locations:
    # Scale back up face locations since the frame we detected in was scaled to 1/4 size

    # Draw a box around the face
    cv2.rectangle(photo, (left, top), (right, bottom), (0, 0, 255), 2)

    # Draw a label with a name below the face
    cv2.rectangle(photo, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
    font = cv2.FONT_HERSHEY_DUPLEX
    cv2.putText(photo, 'Jason Statham', (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

cv2.imwrite('Jason_Statham.jpg',photo)
cv2.waitKey(0)
