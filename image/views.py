from django.http import HttpResponse 
from django.shortcuts import render, redirect 
from .forms import *
from .models import Image, AugmentedImages, OCR
from .image_augmentation import ImageAugmentation
from .ocr import OCRgeneration
import cv2
import os
# Create your views here.

def home(request):
	return render(request, 'image/home.html')

def augmentation(request): 
	if request.method == 'POST':
		form = ImageForm(request.POST, request.FILES) 
		if form.is_valid():
			form.save()
			images = Image.objects.all()
			img_aug_obj = ImageAugmentation() 			
			if Image.objects.filter().order_by('-id')[0].hue==True:
				aug_img = AugmentedImages()
				img_hue = img_aug_obj.Hue()
				aug_img.original_image = Image.objects.filter().order_by('-id')[0]
				cv2.imwrite("media/augmented_images/hue.png",img_hue)
				aug_img.augmented_image = '/augmented_images/hue.png'
				aug_img.save()
			if Image.objects.filter().order_by('-id')[0].gaussianNoise==True:
				img_blur = img_aug_obj.GaussianNoise()
				aug_img2 = AugmentedImages()
				aug_img2.original_image = Image.objects.filter().order_by('-id')[0]
				cv2.imwrite("media/augmented_images/blur.png",img_blur)
				aug_img2.augmented_image = '/augmented_images/blur.png'
				aug_img2.save()
			if Image.objects.filter().order_by('-id')[0].grayscale==True:
				img_gray = img_aug_obj.Grayscale()
				aug_img3 = AugmentedImages()
				aug_img3.original_image = Image.objects.filter().order_by('-id')[0]
				cv2.imwrite("media/augmented_images/gray.png",img_gray)
				aug_img3.augmented_image = '/augmented_images/gray.png'
				aug_img3.save()
			if Image.objects.filter().order_by('-id')[0].color_temperature==True:
				img_temp = img_aug_obj.ColorTemperature()
				aug_img4 = AugmentedImages()
				aug_img4.original_image = Image.objects.filter().order_by('-id')[0]
				cv2.imwrite("media/augmented_images/temp.png",img_temp)
				aug_img4.augmented_image = '/augmented_images/temp.png'
				aug_img4.save()
			if Image.objects.filter().order_by('-id')[0].blur==True:
				img_blur = img_aug_obj.Blur()
				aug_img5 = AugmentedImages()
				aug_img5.original_image = Image.objects.filter().order_by('-id')[0]
				cv2.imwrite("media/augmented_images/blur.png",img_blur)
				aug_img5.augmented_image = '/augmented_images/blur.png'
				aug_img5.save()
			if Image.objects.filter().order_by('-id')[0].random==True:
				#Number of random images to generate.
				n = form.cleaned_data.get('random_images')
				
				aug_imgs, n = img_aug_obj.Random(n)
				aug_img_obj_list = []
				for i in range(n):
					a_img = AugmentedImages()
					aug_img_obj_list.append(a_img)
					aug_img_obj_list[i].original_image = Image.objects.filter().order_by('-id')[0]
					cv2.imwrite("media/augmented_images/rand"+str(i)+".png",aug_imgs[i])
					aug_img_obj_list[i].augmented_image = '/augmented_images/rand'+str(i)+'.png'
					aug_img_obj_list[i].save()
			return redirect('success') 
	else: 
		Image.objects.all().delete()
		AugmentedImages.objects.all().delete()
		form = ImageForm() 
	return render(request, 'image/augmentation.html', {'form' : form}) 


def success(request):
	if request.method == 'GET':
		images = Image.objects.all()
		aug_imgs = AugmentedImages.objects.all().filter(original_image=Image.objects.filter().order_by('-id')[0])
	return render(request,'image/result.html',{'images':images,'augment_images':aug_imgs}) 

def ocr_display(request):
	if request.method == 'GET':
		images = Image.objects.all()
		ocr_objs = OCR.objects.all().filter(original_image=Image.objects.filter().order_by('-id')[0])
	return render(request,'image/ocr_result.html',{'images':images,'ocr_objs':ocr_objs}) 

def ocr(request):
	if request.method == 'POST':
		form2 = OCRForm(request.POST, request.FILES) 
		if form2.is_valid():
			form2.save()
			images = Image.objects.all()
			ocr_obj = OCR()
			ocr_gen_obj = OCRgeneration()
			ocr_obj.original_image = Image.objects.filter().order_by('-id')[0]
			text = ocr_gen_obj.OcrText()
			file = ocr_gen_obj.OcrPdf()
			ocr_obj.OCR_txt = '/ocr/test.txt'
			ocr_obj.OCR_pdf = '/ocr/test.pdf'
			ocr_obj.save()
		return redirect("ocr_display")
	else:
		Image.objects.all().delete()
		OCR.objects.all().delete()
		form = OCRForm()
	return render(request, 'image/ocr.html', {'form' : form}) 
