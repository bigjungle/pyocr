#TESSDATA_PREFIX C:\Program Files (x86)\Tesseract-OCR\tessdata
from PIL import Image
import pytesseract
tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
text=pytesseract.image_to_string(Image.open('denggao.jpg'),lang='chi_sim', config=tessdata_dir_config)
print(text)
text=pytesseract.image_to_string(Image.open('idcard.png'),lang='chi_sim', config=tessdata_dir_config)
print(text)
text=pytesseract.image_to_string(Image.open('zh2.png'),lang='chi_sim', config=tessdata_dir_config)
print(text)
text=pytesseract.image_to_string(Image.open('zh3.png'),lang='chi_sim', config=tessdata_dir_config)
print(text)
