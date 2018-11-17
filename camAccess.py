import cv2
from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import json
import fs

cv2.namedWindow("preview")
vc = cv2.VideoCapture(0)

if vc.isOpened(): # try to get the first frame
    rval, frame = vc.read()
else:
    rval = False

while rval:
    cv2.imshow("preview", frame)
    cv2.imwrite('./imgCaptured.png',frame)
    rval, frame = vc.read()
    key = cv2.waitKey(20)
    if key == 27: # exit on ESC
        break
cv2.destroyWindow("preview")

app = ClarifaiApp(api_key='444fb551757f45e0b124892399e5b760')

model = app.models.get('general-v1.3')
image = ClImage(file_obj=open('./imgCaptured.png', 'rb'))

content = json.dumps(model.predict([image]))
strings = json.loads(content)

imageText = "There is a " + strings["outputs"][0]["data"]["concepts"][0]["name"]+ " ahead!"

print(imageText)
    
fs = open("textToSpeech.txt", "w")
fs.write(imageText)
fs.close();

