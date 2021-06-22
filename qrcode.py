import pyqrcode

code = pyqrcode.create("EU TE AMO!")
code.png("qrcode.png", scale=6)

if code != 0:
    print("QrCODE gerado!")
