import face_recognition
import json
import numpy as np
import requests
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



json_data=json.dumps(data)


r = requests.get('https://localhost:5001/employers/',verify=False)  

print(r.text)

glob=r.json()

#inv_data=json.loads(glob[0])

encoding=np.array(glob[1]["features"]).astype(np.float32)

results = face_recognition.compare_faces( face_encoding, [encoding])
print(results)


