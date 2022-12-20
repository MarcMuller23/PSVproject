from PIL import Image
import time

value = True
while value:    
    im = Image.open('data.jpeg')
    im.show()
    time.sleep(10)
    value= False
