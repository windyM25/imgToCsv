from PIL import Image
import pytesseract
import pandas as pd

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\tesseract.exe"

im = Image.open("11. Masimo Chemicals.jpg")


content = pd.DataFrame()
text = pytesseract.image_to_string(im, lang= 'eng')
temp = pd.DataFrame({'Words':[text]})
content.append(temp)

content.head()

print(text)
writer = pd.ExcelWriter('BEE PILOT.xlsx')
content.to_csv('BEE PILOT.csv',sep=',')
writer.save()
