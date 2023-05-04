#attempt to learn python to import Snapshot .JPG from my IP Camera
import requests
import datetime
import os

#datetime configuration
now = datetime.datetime.now()
date = now.strftime("%m%y")
time = now.strftime("%H%M%S")

#Sequentially numbered filename - uplifted from some random internet help article
counter = 10001
filename = date + '-' + "lawn{}.jpg"
while os.path.isfile(filename.format(counter)):
    counter += 1
filename = filename.format(counter)

#streamsnap_shot is the address of the snapshot
stream_snapshot = ('http://192.168.0.192/snap.jpeg')

r = requests.get(stream_snapshot)

with open(filename, 'wb') as f:
    f.write(r.content)
 
