import PIL
from PIL import Image
import os
# image compressor

mywidth = 2000

source_dir = 'C:/Users/Bhanu Pratap Singh/Desktop/agra'
destination_dir = 'C:/Users/Bhanu Pratap Singh/Desktop/agra1'

def resize_pic(oldpic, newpic, mywidth):
    img = Image.open(oldpic)
    width_size = (mywidth/float(img.size[0]))
    img_size = int((float(img.size[1])*float(width_size)))
    img = img.resize((mywidth,img_size), PIL.Image.ANTIALIAS)
    img.save(newpic)


def entire_dir(source_dir, destination_dir, width):
    files = os.listdir(source_dir)
    i=0
    for file in files:
        i+=1
        oldpic = source_dir + "/" + file
        newpic = destination_dir + "/" + file
        print("pic" , i, "done")

        resize_pic(oldpic, newpic, width)



entire_dir(source_dir, destination_dir, mywidth)