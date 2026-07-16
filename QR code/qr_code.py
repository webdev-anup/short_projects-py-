import qrcode as qr
img = qr.make("https://www.youtube.com/results?search_query=code+with+harry")
img.save("youtube_qr.png")
