import easyocr
from PIL import Image as img

pic = img.open("Pic_1.jpg")
text = pytesseract.image_to_string(pic)
print(text)