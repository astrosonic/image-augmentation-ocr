from django.contrib import admin 
from django.urls import path 
from django.conf import settings 
from django.conf.urls.static import static 
from . import views

urlpatterns = [ 
	path('', views.home, name = 'home'),
	path('augmentation',views.augmentation, name='augmentation'),
	path('image_ocr',views.ocr, name = 'ocr'),
	path('success', views.success, name = 'success'), 
	path('ocr_display', views.ocr_display, name = 'ocr_display')
] 

if settings.DEBUG: 
		urlpatterns += static(settings.MEDIA_URL, 
							document_root=settings.MEDIA_ROOT) 
