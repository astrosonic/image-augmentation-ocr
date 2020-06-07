# forms.py 
from django import forms 
from .models import *

class ImageForm(forms.ModelForm):	
	
	#Text field to accept number of random images to generate
	random_images = forms.IntegerField(required=False,widget=forms.NumberInput(attrs={'disabled':'True','value':'5'}),max_value=1000,label='Enter number of images to generate')	
	
	#Since random_images is not present in model, the field preceeding it will be by default required.
	#To override the behaviour we have added an extra hidden field after image since Image is the actual reuired field here.
	extra_hidden = forms.CharField(widget=forms.HiddenInput(),required=False)

	class Meta: 
		model = Image 
		fields = ['uploaded_Img','extra_hidden','hue','blur','gaussianNoise','grayscale','color_temperature','random','random_images']
		
		widgets = {
			'random' : forms.CheckboxInput(attrs = {
            			'onclick' : '$("#id_random_images").prop("disabled", !$(this).prop("checked"))'
            			})
		}



class OCRForm(forms.ModelForm):
	class Meta:
		model = Image
		fields = ['uploaded_Img']
