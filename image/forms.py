# forms.py 
from django import forms 
from .models import *

class ImageForm(forms.ModelForm): 

	class Meta: 
		model = Image 
		fields = ['uploaded_Img','hue','blur','gaussianNoise','grayscale','color_temperature','random'] 

class OCRForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ['uploaded_Img']