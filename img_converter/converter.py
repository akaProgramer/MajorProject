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


class convert:
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


def main():
    print("Image Converter")
    print("")
    print("Please enter the source directory:")
    source_directory = str(input())
    print("")
    print("Please enter the destination directory:")
    target_directory = str(input())
    print("")

    converter = convert(source_directory, target_directory)
    converter.png_to_jpg()


if __name__ == "__main__":
    main()
