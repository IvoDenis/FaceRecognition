import face_recognition
import json
import numpy as np

obama_image = face_recognition.load_image_file("obama.jpg")

try:
    face_encoding = face_recognition.face_encodings(obama_image)[0]
  
except IndexError:
    print("I wasn't able to locate any faces in at least one of the images. Check the image files. Aborting...")
    quit()

data = {
    "name": "Obama",
    "features":face_encoding.tolist(),
}

json_data=json.dumps(data)

inv_data=json.loads(json_data)

encoding=np.array(inv_data["features"])

results = face_recognition.compare_faces(face_encoding,[encoding] )
if results[0]==True:
    print("Is the unknown face a picture of Obama? {}".format(inv_data["name"]))