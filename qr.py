import qrcode

qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data('http://your-office-url.com/verify')
qr.make(fit=True)

img = qr.make_image(fill='black', back_color='white')
img.save('qr(1).png')