import easyocr
import cv2
import numpy as np
reader = easyocr.Reader(['en','hi'])
results = reader.readtext("OCR/test.png")
text= ''
for result in results:
    text += result[1] + " \n"
print(text)