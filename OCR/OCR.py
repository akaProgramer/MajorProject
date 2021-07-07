import easyocr
import cv2
import numpy as np
reader = easyocr.Reader(['en','hi'])
result = reader.readtext("OCR/unknown.png")

print(result)