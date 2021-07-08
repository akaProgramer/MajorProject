import easyocr
import cv2
import numpy as np

class text_extracter:
    def __init__(self):
        reader = easyocr.Reader(['en','hi'])
        self.results = reader.readtext("OCR/test.png")
        self.text= ''
    def extrated_text(self): 
        for self.result in self.results:
            self.text += self.result[1] + " \n"
        print(self.text)

obj = text_extracter()
obj.extrated_text()
