import qrcode
import sys
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
website = str(input("Link: "))
if "https://" not in website:
    sys.exit("Link Needs To Have https:// In It")
file_name = str(input("File Name Example code.png: "))
if ".jpg" ".png" ".jpeg" in file_name:
    sys.exit("Please Just Add The Name Example: qrcode")


qr.add_data(website)
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white")

img.save(f"{file_name}.png")
