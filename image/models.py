from django.db import models

from django.utils.text import slugify
from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver
# Create your models here.
# models.py 
class Image(models.Model): 
	uploaded_Img = models.ImageField(upload_to='images/') 
	hue = models.BooleanField(default = False)
	blur = models.BooleanField(default = False)
	gaussianNoise = models.BooleanField(default = False)
	grayscale = models.BooleanField(default= False)
	color_temperature = models.BooleanField(default=False)
	random = models.BooleanField(default = False)

class AugmentedImages(models.Model):
	original_image = models.ForeignKey(Image, default=None, on_delete=models.CASCADE)
	augmented_image = models.ImageField(upload_to='augmenteed_images/')

class OCR(models.Model):
	original_image = models.ForeignKey(Image, default=None, on_delete=models.CASCADE)
	OCR_txt = models.FileField(upload_to='ocr/')
	OCR_pdf = models.FileField(upload_to='ocr/')

@receiver(post_delete,sender=Image)
def submission_delete(sender,instance,**kwargs):
	instance.uploaded_Img.delete(False)