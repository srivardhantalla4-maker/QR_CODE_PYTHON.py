import qrcode

url = input("Enter the URL to generate QR code: ").strip()
file_path = "C:\\Users\\admin\Desktop\\qrcode.png"

qr = qrcode.QRCode()
qr.add_data(url)

# Generate the QR code image

img = qr.make_image()
img.save(file_path)
print("qr code generated")