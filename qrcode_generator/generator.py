#!/usr/bin/env python3

"""
This is a Python Program to generate QR Code from an input.
"""

__author__ = "Jugal Kishore"


try:
    import qrcode
except ImportError as e:
    print("Importing of 'qrcode' library failed with error")
    print("")
    print(e)
    exit(1)


def generate_qrcode(message):
    """
    Generates a QR Code
    :param message: Data to generate QR Code from.
    """

    # Create an instance of QRCode object
    qr = qrcode.QRCode(version=1, box_size=10, border=5)

    # Generate QR Code
    qr.add_data(message)
    qr.make(fit=True)

    return qr


def save_qrcode(qr_obj):
    """
    Generates a png picture and saves it.
    :param qr_obj: QRCode object.
    """

    # Generate Image and Save it
    img = qr_obj.make_image(fill="black", back_color="white")
    img.save("qrcode.png")


def main():
    """
    Main Function of the QR Code Generator Program.
    """
    print("QR Code Generator")
    print("")
    print("Enter String Value: ")
    data = input()
    print("")
    print(f"Generating QR Code for: {data}")
    print("")

    generated = generate_qrcode(data)
    save_qrcode(generated)

    print("Your QR Code was saved to 'qrcode.png' file.")


if __name__ == "__main__":
    main()
