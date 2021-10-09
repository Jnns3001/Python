#Decode
from PIL import Image
from pyzbar.pyzbar import decode
data = decode(Image.open("QRCode/QR.png"))
url = bytes.decode(data[0][0])
print(url)

#Generate
import pyqrcode
qr = pyqrcode.create(url)
print(qr.png("QRCode/qrcode.png", scale=5))
