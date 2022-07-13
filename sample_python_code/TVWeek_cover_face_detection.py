import matplotlib.pyplot as plt
import cv2
import requests
from urllib.request import urlopen
import numpy as np


# Load the face cascade for CV2 processing
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


url = "https://digital.lib.hkbu.edu.hk/api/tvweek/?startIssueNumber=1150&endIssueNumber=1155"
r = requests.get(url)
data = r.json()


for result in data['Results']:
    cover_img = result['coverThumbnail']
    
    req = urlopen(cover_img)
    arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
    img = cv2.imdecode(arr, -1) # 'Load it as it is'
    #img = cv2.imread(cover_img)
        
    # Convert image into grayscale
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  
    gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        
    # Detect faces and draw rectangle around the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)    
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
            
    # Display the output
    plt.imshow(img)
    plt.show()
