# -*- coding: utf-8 -*-
"""
name:objectextraction.py
@author: jimchen1218@sina.com
"""

import cv2
import matplotlib.pyplot as plt
from PIL import Image
import matplotlib.image as mpimg 
import gc
print(__doc__)


import numpy as np  
import cv2  
from matplotlib import pyplot as plt
  
#open a image 
def img_open(img_file):
		ret_img = cv2.imread(img_file)
		return ret_img

def img_get_width_height(image):
		ret_w,ret_h = image.shape[:2]
		print("img_get_width_height width:%d,height:%d\n"%(ret_w,ret_h))
		return ret_w,ret_h

def mask_build(image):
		ret_mask = np.zeros(image.shape[:2], np.uint8)
		return ret_mask

def img_grabcut(image,mask):
		cut_align = 5
		iterator_times = 5
		width,height = img_get_width_height(image)
		rect = (cut_align, cut_align, width-20, height-20) #need to adjust to adapt each image for best cut effect
		bgdModel = np.zeros((1, 65), np.float64)
		fgdModel = np.zeros((1, 65), np.float64)
		ret_mask,bgdModel,fgdModel = cv2.grabCut(image, mask, rect, bgdModel, fgdModel, iterator_times, cv2.GC_INIT_WITH_RECT)  
		#print("img_grabcut ret_mask:%s\n"%(ret_mask))
		mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
		ret_img = image * mask2[:, :, np.newaxis]
		return ret_img

def img_bgr2gray(image):
		gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		return gray

def img_gray2bgr(image):
		bgr=cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
		#img += 255 * (1 - cv2.cvtColor(mask2, cv2.COLOR_GRAY2BGR))	
		return bgr

def img_erode_dilate(image):
		erode=cv2.erode(image,None,iterations=1)
		dilate=cv2.dilate(erode,None,iterations=1)
		#print("dilate:%s\n"%(dilate))		
		return dilate

def img_addnoise(image):
		width,height = image.shape[:2]
		for i in range(2000):
				noise_x = np.random.randint(0,width)
				noise_y = np.random.randint(0,height)
				image[noise_x][noise_y] = 255
		return image
		
def img_blur(image):
		image = cv2.blur(image,(3,5))	
		print("img_blur image:%s\n"%(image))
		return image
		
def img_medianblur(image):
		image = cv2.medianBlur(image,5)
		print("img_medianblur image:%s\n"%(image))
		return image		
		
def img_filter2D(image):
		kernel = np.ones((10,10),np.float32)/25
		image = cv2.filter2D(image,-1,kernel)
		return image	
		
def img_resize_interpolation(image):
		blur_cubic = cv2.resize(blur,(width,height),interpolation=cv2.INTER_CUBIC)
		return dilate		
		
def img_change_bg(image_orig,image_bg,img_erode):
		width,height = img_get_width_height(image_orig)
		bg_width,bg_height = img_get_width_height(image_bg)
		image_bg_resize = image_bg[0:width, 0:height]
		center_x = np.floor(bg_width/2)
		center_y = np.floor(bg_height/2)
		#print("center_x:%d,center_y:%d\n"%(center_x,center_y))

		for i in range(width):
			for j in range(height):
				if img_erode[i,j]!=0:
					#print("i:%d,j:%d,blur[i,j]:%s\n"%(i,j,dilate[i,j]))
					image_bg_resize[i,j]=image_orig[i,j]
		return image_bg_resize

def img_sub_mean(image):
		#print("image:%s\n"%(image))
		img = np.array(img)
		mean = np.mean(img)
		img = img - mean
		img = img * 0.9 + mean * 0.9
		img /= 255
		return img

def main():	
		image_orig = img_open('coat.jpg')
		mask = mask_build(image_orig)
		image = img_grabcut(image_orig,mask)
		#print("img:%s\n"%(image))
		cv2.imshow('image',image)
		cv2.waitKey(0)
		image = img_bgr2gray(image)
		#cv2.imshow('img_gray',image)
		#cv2.waitKey(0)		
		image = img_erode_dilate(image)
		#cv2.imshow('image',image)
		#cv2.waitKey(0)			
		image = img_medianblur(image)
		
		image_bg = img_open('bg.bmp')
		image_change_bg=img_change_bg(image_orig,image_bg,image)
		cv2.imshow('image_change_bg',image_change_bg)
		cv2.waitKey(0)

if __name__ == "__main__":
		main()
		gc.collect()