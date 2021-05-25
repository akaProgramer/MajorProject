#!/usr/bin/env python3

"""
This is a Python Program to display QR Code from an input.
"""

__author__ = "Jugal Kishore"


import qrcode

print("QR Code Generator")
print("")
print("Enter String Value: ")
data = input()
print("")
print(f"Generating QR Code for: {data}")
print("")

# Create an instance of QRCode object
qr = qrcode.QRCode(version=1, box_size=10, border=5)

# Generate QR Code
qr.add_data(data)
qr.make(fit=True)

# Generate Image and Save it
img = qr.make_image(fill="black", back_color="white")
img.save("qrcode.png")

print("Your QR Code was saved to 'qrcode.png' file.")
