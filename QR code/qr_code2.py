import qrcode
from PIL import Image

qr = qrcode.QRCode(version=1,
                   error_correction=qrcode.constants.ERROR_CORRECT_H,
                   box_size=10,
                   border=4,)
qr.add_data("https://www.youtube.com/results?search_query=code+with+harry")
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")
img.save("youtube_qr.png")

print("QR Code ban gaya! youtube_qr.png save ho gaya.") 
