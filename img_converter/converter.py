#!/usr/bin/env python3

"""
This is a Python Program which converts PNG/JPG to JPG/PNG
"""

__author__ = "Ankit Mahor"


# Importing the module(s)
from PIL import Image
import os
import glob


# Global Variable(s)
if os.name == "nt":
    SLASH = "\\"
else:
    SLASH = "/"


class Convert:
    """
    An image converter class which can convert a PNG, JPEG to JPEG, PNG interchangably.
    """
    def __init__(self, source_directory, target_directory):
        self.source_directory = source_directory
        self.target_directory = target_directory

    def png_to_jpg(self) -> None:
        """
        This function converts a PNG image to a JPEG image.
        """

        if not os.path.exists(self.source_directory):
            print("Can't find source directory")
            print("Exiting...")
            exit(1)
        if not os.path.exists(self.target_directory):
            print("Can't find target directory, creating...")
            os.makedirs(self.target_directory)
            print(f"Created target directory: {self.target_directory}")
            print("")

        for file in glob.glob(f"{self.source_directory}{SLASH}*.png"):
            if file.endswith(".png"):
                print("Converting: " + file)
                im = Image.open(file, "r")
                rgb_image = im.convert("RGB")
                target_file = self.target_directory + SLASH + file.split(SLASH)[-1].split(".")[0] + ".jpg"
                rgb_image.save(target_file)
                print("Converted: " + target_file)
                print("")

    def jpg_to_png(self) -> None:
        """
        This function converts a JPEG image to a PNG image.
        """

        if not os.path.exists(self.source_directory):
            print("Can't find source directory")
            print("Exiting...")
            exit(1)
        if not os.path.exists(self.target_directory):
            print("Can't find target directory, creating...")
            os.makedirs(self.target_directory)
            print(f"Created target directory: {self.target_directory}")
            print("")

        for file in glob.glob(f"{self.source_directory}{SLASH}*.jpg"):
            if file.endswith(".jpg"):
                print("Converting: " + file)
                im = Image.open(file, "r")
                rgb_image = im.convert("RGB")
                target_file = self.target_directory + SLASH + file.split(SLASH)[-1].split(".")[0] + ".png"
                rgb_image.save(target_file)
                print("Converted: " + target_file)
                print("")


def main():
    print("Image Converter")
    print("")
    print(" 1. Convert PNG to JPG/JPEG")
    print(" 2. Convert JPG/JPEG to PNG")
    print(" Nothing (press enter) to exit!")
    print("")
    choice = input("Enter your choice: ")
    if not choice:
        print("Exiting...")
        exit(0)

    print("")
    source_directory = str(input("Please enter the source directory: "))
    print("")
    target_directory = str(input("Please enter the destination directory: "))
    print("")

    if choice == "1":
        converter = Convert(source_directory, target_directory)
        converter.png_to_jpg()
    elif choice == "2":
        converter = Convert(source_directory, target_directory)
        converter.jpg_to_png()


if __name__ == "__main__":
    main()
