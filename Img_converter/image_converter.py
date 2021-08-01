#importing The Modules
from PIL import Image
import os
import glob

class convert:

    def PNG_TO_JPG(self):

        target_directory = r"C:\Users\rinku\Pictures\Screenshots\JPG"
        for File in glob.glob(r"C:\Users\rinku\Pictures\Screenshots\*.png"):
            
            # check if directory exist in the given path
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)

            # Open Image & Convert it Into RGB Format
            image = Image.open(File)
            rgb_image = image.convert("RGB")

            # Change File Extension And its Location or (Path)
            To_File = File.split("\\")
            To_File = To_File[-1]
            filename = To_File[:-4]
            Save_file = target_directory + "\\" + str(filename) + ".jpg"   
            print(Save_file)
            
            # Save File Into That Location
            rgb_image.save(Save_file)

    def PNG_TO_JPEG(self):

        target_directory = r"C:\Users\rinku\Pictures\Screenshots\JPEG"
        for File in glob.glob(r"C:\Users\rinku\Pictures\Screenshots\*.png"):
            
            # check if directory exist in the given path
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)

            # Open Image & Convert it Into RGB Format
            image = Image.open(File)
            rgb_image = image.convert("RGB")

            # Change File Extension And its Location or (Path)
            To_File = File.split("\\")
            To_File = To_File[-1]
            filename = To_File[:-4]
            Save_file = target_directory + "\\" + str(filename) + ".jpeg"   
            print(Save_file)
            
            # Save File Into That Location
            rgb_image.save(Save_file)

    def JPG_TO_JPEG(self):
        target_directory = r"C:\Users\rinku\Pictures\Screenshots\JPG_TO_JPEG"
        for File in glob.glob(r"C:\Users\rinku\Pictures\Screenshots\JPG\*.jpg"):

            
            # check if directory exist in the given path
            if not os.path.exists(target_directory):
                os.makedirs(target_directory)

            # Open Image & Convert it Into RGB Format
            image = Image.open(File)
            #rgb_image = image.convert("RGB")

            # Change File Extension And its Location or (Path)
            To_File = File.split("\\")
            To_File = To_File[-1]
            filename = To_File[:-4]
            Save_file = target_directory + "\\" + str(filename) + ".jpeg"   
            print(Save_file)
            
            # Save File Into That Location
            image.save(Save_file)
        

obj = convert()
#obj.PNG_TO_JPG()
#obj.PNG_TO_JPEG()
obj.JPG_TO_JPEG()
