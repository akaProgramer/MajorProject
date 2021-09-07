# image compressor

import PIL
from PIL import Image
import os

mywidth = 2000
source_dir = 'C:/Users/Bhanu Pratap Singh/Desktop/agra'
destination_dir = 'C:/Users/Bhanu Pratap Singh/Desktop/agra1'


class Compress:

    def resize_pic(self, oldpic, newpic, mywidth):
        try:
            img = Image.open(oldpic)
            width_size = (mywidth / float(img.size[0]))
            img_size = int((float(img.size[1]) * float(width_size)))
            img = img.resize((mywidth, img_size), PIL.Image.ANTIALIAS)
            img.save(newpic)
        except:
            print("pass")

    def entire_dir(self, source_dir, destination_dir, width):

        self.width = width

        files = os.listdir(source_dir)
        i = 0
        for file in files:

            i += 1
            oldpic = source_dir + "/" + file
            newpic = destination_dir + "/" + file
            self.resize_pic(oldpic, newpic, width)
            print("pic", i, "done")


obj = Compress()
obj.entire_dir(source_dir, destination_dir, mywidth)
