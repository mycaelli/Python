"""
Gerates a qrcode associated to a data 

"""

import qrcode

#creating object qrcode
    #version -> sets the version of de qrcode (higher the number, bigger and more complicated the picture -> range = 1 to 40)
    #box_size -> controls how many pixels each "box" of the qrcode is
    #border -> controls how many boxes thick the border should be
qr = qrcode.QRCode(version = 15, box_size = 10, border = 5)

data = 1 #path of the qrcode - it can be a link or a text
qr.add_data(data)
qr.make(fit = True) # makes all of the qrcode dimensions be used
img = qr.make_image(fill="black", back_color="white")
img.save("test1.png")