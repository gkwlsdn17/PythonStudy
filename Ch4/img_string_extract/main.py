from PIL import Image
import pytesseract

image_path = r'image.PNG'

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

laguages = pytesseract.get_languages(config='')
print(laguages)
print("========" * 5)
text = pytesseract.image_to_string(Image.open(image_path), lang='kor')      # 한글 추출
print(text)
print("========" * 5)
text = pytesseract.image_to_string(Image.open(image_path), lang='kor+eng')      # 한글, 영어 추출
print(text)

with open(r'translation.txt', 'w', encoding='utf8') as f:
    f.write(text)