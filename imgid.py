from clarifai.rest import ClarifaiApp
from clarifai.rest import Image as ClImage
import json
import fs


app = ClarifaiApp(api_key='444fb551757f45e0b124892399e5b760')

model = app.models.get('general-v1.3')
image = ClImage(file_obj=open('imgCapture.jpg', 'rb'))

content = json.dumps(model.predict([image]))
strings = json.loads(content)

imageText = "There is a " + strings["outputs"][0]["data"]["concepts"][0]["name"]+ " ahead!"

print(imageText)

#for x in strings["outputs"][0]["data"]["concepts"]:
#    print("There is a", x["name"], "ahead")
    
    
fs = open("textToSpeech.txt", "w")
fs.write(imageText)
fs.close();

