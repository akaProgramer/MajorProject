#!/usr/bin/env python3

"""
This is a Python Program which converts PNG/JPG image(s) to JPG/PNG image(s).
Also, it can generate PDF file from JPG/PNG image(s).
"""

__author__ = "Ankit Mahor"


# Importing the module(s)
from PIL import Image
from fpdf import FPDF
import os
import glob


# Global Variable(s)
if os.name == "nt":
    SLASH = "\\"
else:
    SLASH = "/"


class Convert:
    """
    An image converter class which can convert PNG, JPG image(s) to JPG, PNG image(s),
    and vice versa. Also, it can convert JPG, PNG image(s) to PDF file(s).
    """

    def __init__(self, source_directory, target_directory):
        self.source_directory = source_directory
        self.target_directory = target_directory

        if not os.path.exists(self.source_directory):
            print("Can't find source directory")
            print("Exiting...")
            exit(1)
        if not os.path.exists(self.target_directory):
            print("Can't find target directory, creating...")
            os.makedirs(self.target_directory)
            print(f"Created target directory: {self.target_directory}")
            print("")

    def png_to_jpg(self) -> None:
        """
        This function converts PNG image(s) to JPG image(s).
        """

        file_list = glob.glob(f"{self.source_directory}{SLASH}*.png")
        if not file_list:
            print("No PNG file(s) found in source directory: " + self.source_directory)
            print("Exiting...")
            exit(1)
        for file in file_list:
            print("Converting: " + file)
            im = Image.open(file, "r")
            rgb_image = im.convert("RGB")
            target_file = self.target_directory + SLASH + file.split(SLASH)[-1].split(".")[0] + ".jpg"
            rgb_image.save(target_file)
            print("Converted: " + target_file)
            print("")

    def jpg_to_png(self) -> None:
        """
        This function converts a JPG image to a PNG image.
        """

        file_list = glob.glob(f"{self.source_directory}{SLASH}*.jpg")
        if not file_list:
            print("No JPG file(s) found in source directory: " + self.source_directory)
            print("Exiting...")
            exit(1)
        for file in file_list:
            print("Converting: " + file)
            im = Image.open(file, "r")
            rgb_image = im.convert("RGB")
            target_file = self.target_directory + SLASH + file.split(SLASH)[-1].split(".")[0] + ".png"
            rgb_image.save(target_file)
            print("Converted: " + target_file)
            print("")

    def jgp_to_pdf(self) -> None:
        """
        This function converts JPG image(s) to a PDF file.
        """

        file_list = glob.glob(f"{self.source_directory}{SLASH}*.jpg")
        if not file_list:
            print("No JPG file(s) found in source directory: " + self.source_directory)
            print("Exiting...")
            exit(1)

        pdf = FPDF()
        for file in file_list:
            print("Adding file: " + file)
            pdf.add_page()
            pdf.image(file, 0, 0, 210, 297)
        target_file = f"{self.target_directory}{SLASH}output.pdf"
        pdf.output(target_file, "F")
        print("")
        print("Created PDF File -> " + target_file)

    def png_to_pdf(self) -> None:
        """
        This function converts PNG image(s) to a PDF File.
        """

        file_list = glob.glob(f"{self.source_directory}{SLASH}*.png")
        if not file_list:
            print("No PNG file(s) found in source directory: " + self.source_directory)
            print("Exiting...")
            exit(1)

        pdf = FPDF()
        for file in file_list:
            print("Adding file: " + file)
            pdf.add_page()
            pdf.image(file, 0, 0, 210, 297)
        target_file = f"{self.target_directory}{SLASH}output.pdf"
        pdf.output(target_file, "F")
        print("")
        print("Created PDF File -> " + target_file)


def main():
    print("Image Converter")
    print("")
    print(" 1. Convert PNG image(s) to JPG/JPEG image(s)")
    print(" 2. Convert JPG/JPEG image(s) to PNG image(s)")
    print(" 3. Convert JPG/JPEG image(s) to PDF File")
    print(" 4. Convert PNG image(s) to PDF File")
    print("")
    print(" Nothing (press enter) to exit!")
    print("")
    choice = input("Enter your choice: ")
    if not choice:
        print("Exiting...")
        exit(0)
    if type(choice) is not int:
        print("Invalid choice, exiting...")
        exit(1)

    print("")
    source_directory = str(input("Please enter the source directory: "))
    print("")
    if not source_directory:
        print("Exiting...")
        exit(1)
    target_directory = str(input("Please enter the destination directory: "))
    print("")
    if not target_directory:
        print("Exiting...")
        exit(1)

    if choice == "1":
        converter = Convert(source_directory, target_directory)
        converter.png_to_jpg()
    elif choice == "2":
        converter = Convert(source_directory, target_directory)
        converter.jpg_to_png()
    elif choice == "3":
        converter = Convert(source_directory, target_directory)
        converter.jgp_to_pdf()
    elif choice == "4":
        converter = Convert(source_directory, target_directory)
        converter.png_to_pdf()

if __name__ == "__main__":
    main()
