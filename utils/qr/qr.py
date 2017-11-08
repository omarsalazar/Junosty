#from usuario.models import datosusuario
import qrcode

boleta = input("Cual es tu boleta? ")
img = qrcode.make(boleta)
f = open(boleta + ".png", "wb")
img.save(f)
f.close()


# qr = qrcode.QRCode(
#     version=3,uns
#     error_correction=qrcode.constants.ERROR_CORRECT_L,
#     box_size=10,
#     border=4,
# )
# boleta = datosusuario.objects.get("no_boleta")
# qr.add_data(boleta)
# qr.make(fit=True)
#
# img = qr.make_image()

# img = qrcode.make("Hola desde Recursos Python!")
# f = open("output.png", "wb")
# img.save(f)
# f.close()
