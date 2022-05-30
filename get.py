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
for s in os.listdir('Topshiriq2'):
    # print(s)
    for a in os.listdir(f'Topshiriq2/{s}'):
        # print(s, a)
        name = a.split(".")[0]
        # print(name)
        path = f"Topshiriq2/{s}/{a}"
        # print(path)
        pic = face_recognition.load_image_file(path)
        encode_pic = face_recognition.face_encodings(pic)[0]
#
        i = {'name':name,
             'path':path,
             'dir':s,
             'encode': encode_pic}
        data.append(i)
        # print(data)
#
encodednumpydata = json.dumps(data, cls=numpyarrayencoder)
# print(encodednumpydata)


def main():
    with open('astrum.json', 'w') as outfile:
        outfile.write(encodednumpydata)
main()

