import pytesseract
from .models import Image
import os
import cv2
class OCRgeneration:
	def __init__(self):
		self.image = os.getcwd()+Image.objects.filter().order_by('-id')[0].uploaded_Img.url

	def OcrText(self):
		img_text = pytesseract.image_to_string(self.image.replace("\n", " "))
		with open('media/ocr/test.txt', 'w') as f:
			f.write(img_text)
		return img_text

	def OcrPdf(self):
		pdf = pytesseract.image_to_pdf_or_hocr(self.image, extension='pdf')
		print(type(pdf))
		with open('media/ocr/test.pdf', 'w+b') as f:
			f.write(pdf) # pdf type is bytes by default
		return f