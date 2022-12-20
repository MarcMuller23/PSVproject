import RPi.GPIO as GPIO
import time
import subprocess
from mfrc522 import SimpleMFRC522
from PIL import Image

rfid = SimpleMFRC522()

while True:
    id, text = rfid.read()
    viewer = subprocess.Popen(['python3','/home/marc/Documents/PSVproject/viewer.py'])
    print(id)
    print(text)
    time.sleep(10)
    viewer.kill()
