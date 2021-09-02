import easyocr
import os

class text_extracter:
    def __init__(self):
        reader = easyocr.Reader(['en','hi'])
        self.results = reader.readtext("OCR/test.png")
        self.text= ''
    def extrated_text(self): 
        for self.result in self.results:
            self.text += self.result[1] + " \n"
        print(self.text)
        with open('extracted.txt', 'w' , encoding='utf-8') as f:
            f.write(self.text)
        os.system('extracted.txt')


def main():
    obj = text_extracter()
    obj.extrated_text()

if __name__ == "__main__":
    main()