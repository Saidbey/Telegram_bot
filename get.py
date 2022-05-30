import os
import json
from json import JSONEncoder
import numpy as np
import face_recognition

class numpyarrayencoder(JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

data = []
# Coming steps you should give the adress of the pictures, should be encoded
for s in os.listdir('Topshiriq2'):# This code enters the folders located in Topshiriq2 folder
    for a in os.listdir(f'Topshiriq2/{s}'): # There three folders in Topshiriq2 and this code enters every single one and takes pictures from them
        name = a.split(".")[0]#Pictuers in folders is in like someone.jpg and this code split them and takes just the name of the picture(someone)
        path = f"Topshiriq2/{s}/{a}"#This is all path
        pic = face_recognition.load_image_file(path)
        encode_pic = face_recognition.face_encodings(pic)[0]#This encodes all the pictures

        i = {'name':name,
             'path':path,
             'dir':s,
             'encode': encode_pic}
        data.append(i)

encodednumpydata = json.dumps(data, cls=numpyarrayencoder)

def main():
    with open('astrum.json', 'w') as outfile:
        outfile.write(encodednumpydata)
main()

