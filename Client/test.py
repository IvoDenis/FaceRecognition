import face_recognition
import json
import numpy as np
import requests
from Mode
obama_image = face_recognition.load_image_file("biden.jpg")

try:
    face_encoding = face_recognition.face_encodings(obama_image)[0]
  
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

data = {
    "name": "Biden",
    "features":face_encoding.tolist(),
}
Get