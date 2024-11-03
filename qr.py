import qrcode
from qrcode import *

qr = qrcode.QRCode(
    version=7,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)


qr.add_data(input("Put link here") , optimize = 0)
qr.make(fit=False)

img = qr.make_image(fill='black', back_color='white')

img.save('qr.png')