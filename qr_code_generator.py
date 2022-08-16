import pyqrcode
import png

def qr_code():
    s='Welcome To my Qr-Code'
    d=pyqrcode.create(s)
    d.png('my_img.png',scale=10)
    print('Code Executed properly')

if __name__=='__main__':
    qr_code()