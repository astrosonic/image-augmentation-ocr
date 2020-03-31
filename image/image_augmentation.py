
import imgaug.augmenters as iaa
import numpy as np
import cv2
import os 
from .models import AugmentedImages, Image
class ImageAugmentation:
	def __init__(self):
		self.image = cv2.imread(os.getcwd()+Image.objects.filter().order_by('-id')[0].uploaded_Img.url)

	def Hue(self):
		hue = iaa.AddToHueAndSaturation((-20,30),per_channel=True)
		image_hue = hue.augment_images([self.image])
		return image_hue[0]

	def Blur(self):
		blur = iaa.GaussianBlur(sigma=3)
		image_blur = blur.augment_images([self.image])
		return image_blur[0]

	def GaussianNoise(self):
		noise = iaa.AdditiveGaussianNoise(scale=0.2*255)	
		image_noise = noise.augment_images([self.image])
		return image_noise[0]

	def Grayscale(self):
		gray = iaa.Grayscale(alpha=(0.0, 1.0))
		image_gray = gray.augment_images([self.image])
		return image_gray[0]

	def ColorTemperature(self):
		temp = iaa.ChangeColorTemperature((1100, 10000))
		image_temp = temp.augment_images([self.image])
		return image_temp[0]

	def Random(self, n=5):
		seq = iaa.Sequential([
	    iaa.AddToHueAndSaturation((-20,30),per_channel=True),
	    iaa.GaussianBlur(sigma=2),
	    iaa.AdditiveGaussianNoise(scale=0.2*255),
	    iaa.geometric.Affine(rotate=(-25, 25)),
	    iaa.Crop(px=(0, 100)),
	    iaa.Grayscale(alpha=(0.0, 1.0)),
	    iaa.ChangeColorTemperature((1100, 10000))
		])
		images_aug=[seq(image=self.image) for _ in range(n)]
		print(len(images_aug))
		return images_aug, n 