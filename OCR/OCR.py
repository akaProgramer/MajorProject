import easyocr
import os

class text_extracter:
    def __init__(self):
        self.text= ''
    def extrated_text(self,path): 
        try:
            reader = easyocr.Reader(['en','hi'])
            self.results = reader.readtext(path)
            for self.result in self.results:
                self.text += self.result[1] + " \n"     
        except:
            print("something went wrong")
            pass 

        if self.text!="":
            with open('extracted.txt', 'w' , encoding='utf-8') as f:
                f.write(self.text)
            os.system('extracted.txt')
        else:
            print("no text detected")

def main():
    path = "OCR/sample.jpeg"
    obj = text_extracter()
    obj.extrated_text(path)

if __name__ == "__main__":
    main()