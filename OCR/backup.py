    def __init__(self,path):
        reader = easyocr.Reader(['en','hi'])
        self.results = reader.readtext(path)
        self.text= ''
    def extrated_text(self): 
        for self.result in self.results:
            self.text += self.result[1] + " \n"
        print(self.text)
        try:
            if self.text=="":
                print("no text detected")
        except:
            with open('extracted.txt', 'w' , encoding='utf-8') as f:
                f.write(self.text)
            os.system('extracted.txt')
