from PIL import Image
import os
import glob

class convert:

    def PNG_TO_JPG(self,):
        target_directory = r"C:\Users\rinku\Pictures\Screenshots\converted"
        for File in glob.glob(r"C:\Users\rinku\Pictures\Screenshots\*.png"):
        
            #image = Image.open(File)
            #filename = File[:-4]
            #print(filename)
        
            #rgb_image = image.convert("RGB")
            To_File = File.split("\\")
            print(To_File)
            To_File = To_File[-1]
            #print(To_File)
            Save_file = str(To_File) + ".jpg"
            #print(Save_file)
            To_save_path = target_directory + "\\" +  Save_file
            #print(To_save_path)
            #rgb_image.save(f"C:\\Users\\rinku\\Pictures\\Screenshots\\JPG\\" + str(rgb_image) + ".jpg")
            #Full_Path = os.path.join(target_directory, Save_file) chodu dino ankit fatua saala gufa manav
     
            #print(Full_Path)
            #rgb_image.save(To_save_path)
        #print(Save_file)
        #print(os.path.join(target_directory, Save_file)) 

obj = convert()
obj.PNG_TO_JPG()
