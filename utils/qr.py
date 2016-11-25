import qrcode

qr = qrcode.QRCode(
    version=3,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('2013090307')
qr.make(fit=True)

img = qr.make_image()

# img = qrcode.make("Hola desde Recursos Python!")
# f = open("output.png", "wb")
# img.save(f)
# f.close()
