import pyqrcode
# Cadena de la que queremos generar el QR
s = "https://www.colegiovivas.com"
# Generación
url = pyqrcode.create(s)
# Se guarda como png
url.png("myqr.png", scale=6)