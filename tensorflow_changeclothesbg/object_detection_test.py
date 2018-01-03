'''
name:object_detection_test.py
date:11/23/2017
author:jimchen1218@sina.com
'''

import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile

from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image

import cv2
import matplotlib.image as mpimg 
import gc
print(__doc__)

#if tf.__version__ != '1.4.0':
#  raise ImportError('Please upgrade your tensorflow installation to v1.4.0!')
  
#%matplotlib inline

# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")

import label_map_util
import visualization_utils as vis_util


def img_open(img_file):
		ret_img = cv2.imread(img_file)
		return ret_img
		
def img_save(img_file,filename):
	  cv2.imwrite(filename,img_file)

def img_get_height_width(image):
		ret_h,ret_w = image.shape[:2]
		print("img_get_width_height width:%d,height:%d\n"%(ret_w,ret_h))
		return ret_h,ret_w

def mask_build(image):
		ret_mask = np.zeros(image.shape[:2], np.uint8)
		return ret_mask
		
def mask_while_build(image):
		ret_mask = np.ones(image.shape[:2], np.uint8)
		return ret_mask		

def img_bgr2gray(image):
		gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
		return gray

def img_gray2bgr(image):
		bgr=cv2.cvtColor(image,cv2.COLOR_GRAY2BGR)
		#img += 255 * (1 - cv2.cvtColor(mask2, cv2.COLOR_GRAY2BGR))	
		return bgr

def img_erode_dilate(image):
		erode=cv2.erode(image,None,iterations=1)
		dilate=cv2.dilate(erode,None,iterations=2)
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
		#print("img_blur image:%s\n"%(image))
		return image

def img_gaussianblur(image):
		image=cv2.GaussianBlur(image, (3, 3), 0)
		#print("img_blur image:%s\n"%(image))
		return image		
		
def img_medianblur(image):
		image = np.hstack([cv2.medianBlur(image,3),
		                     cv2.medianBlur(image,5),
		                     cv2.medianBlur(image,7)
		                     ])	
		#image = cv2.medianBlur(image,5)
		#print("img_medianblur image:%s\n"%(image))
		return image		
		
def img_filter2D(image):
		kernel = np.ones((10,10),np.float32)/25
		image = cv2.filter2D(image,-1,kernel)
		return image	
		
def img_resize_interpolation_cubic(image):
		width,height = img_get_width_height(image)
		blur_cubic = cv2.resize(image,(width,height),interpolation=cv2.INTER_CUBIC)
		return dilate	
		
def img_resize_interpolation_bilinear(image):
		width,height = img_get_width_height(image)
		blur_cubic = cv2.resize(image,(width,height),interpolation=cv2.INTER_LINEAR)
		return dilate

def img_sub_mean(image):
		#print("image:%s\n"%(image))
		img = np.array(img)
		mean = np.mean(img)
		img = img - mean
		img = img * 0.9 + mean * 0.9
		img /= 255
		return img
		
def img_inverse(image):		
		image = np.array(image)
		image = 255 -image
		return image

def img_contour(image):
		gray = img_bgr2gray(image)
		cv2.imshow("gray", gray)
		cv2.waitKey(0)
		inverse = img_inverse(gray)
		cv2.imshow("inverse", inverse)
		cv2.waitKey(0)
		ret, binary = cv2.threshold(inverse,127,255,cv2.THRESH_BINARY)
		#print("img_contour ret:%s\n"%(ret))
		img, contours, hierarchy = cv2.findContours(binary,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
		print("img_contour contours:%s,hierarchy:%s\n"%(contours,hierarchy))
		ret = cv2.drawContours(inverse,contours,-1,(0,0,255),3)
		cnt = len(contours)
		print("cnt:%s\n"%(cnt))
		print("contours[0][0]:%s\n"%(contours[0][0]))

		#x,y,w,h = contours[0]
		x, y, w, h = cv2.boundingRect(cnt)
		print("x:%s,y:%s,w:%s,h:%s\n"%(x,y, w, h))
		cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 1)
		
		cv2.imshow("img", img)
		cv2.waitKey(0)
		#return (x, y, w, h)

def img_grabcut(image,mask,radio_bbox):
		#cut_align = 1
		iterator_times = 3
		height,width = img_get_height_width(image)
		#rect = (cut_align, cut_align,width, height)
		#rect = (186,30,434,750)#pic_2.jpg

		#rect = (40,120,533,494)#pichw.jpg
		#rect = (80,0,452,705)#piczq.jpg
		box_y= int(np.floor(height*radio_bbox[0]))
		box_x=int(np.floor(width*radio_bbox[1]))
		box_dy =int(np.floor(height*radio_bbox[2]))
		box_dx = int(np.floor(width*radio_bbox[3]))
		bbox_rect = (box_x,box_y-20,box_dx,box_dy)
		print("bbox_rect\n",bbox_rect)		
		#bbox_rect = (70,40,320,720)#skirt_1.jpg
		#print("bbox_rect\n",bbox_rect)		

		#rect = (435,0,2249,3739)#lrj.jpg
		#rect = (80,10,330,310) #white_shirt_graybg.jpg
		#rect = (40,0,233,278)#whiteshirt_yellowbg.jpg
		#just for man jacket #need to adjust to adapt each image for best cut effect
		bgdModel = np.zeros((1, 65), np.float64)
		fgdModel = np.zeros((1, 65), np.float64)
		cv2.grabCut(image, mask, bbox_rect, bgdModel, fgdModel, iterator_times, cv2.GC_INIT_WITH_RECT)  
		#print("img_grabcut ret_mask:%s\n"%(ret_mask))
		mask2 = np.where((mask == 2) | (mask == 0), 0, 1).astype('uint8')
		
		print("img_grabcut width:%d,height:%d\n"%(width,height))
		if width > height:
				ret_img = image * mask2[:, :, np.newaxis]
		else:
				ret_img = mask2[:, :, np.newaxis]*image

		#cv2.imshow("ret_img", ret_img)
		return ret_img

def img_change_bg(image_orig,image_bg,img_erode):
		height,width = img_get_height_width(image_orig)
		bg_height,bg_width = img_get_height_width(image_bg)
		
		#if height > bg_height:	
		#	height 
		
		image_resize_bg = cv2.resize(image_bg,(width,height),interpolation=cv2.INTER_CUBIC)
		
		image_bg_resize = image_resize_bg[0:height,0:width]
		#center_x = np.floor(bg_width/2)
		#center_y = np.floor(bg_height/2)
		#print("center_x:%d,center_y:%d\n"%(center_x,center_y))

		for i in range(height):
			for j in range(width):
				if img_erode[i,j]!=0:
					#print("i:%d,j:%d,blur[i,j]:%s\n"%(i,j,dilate[i,j]))
					image_resize_bg[i,j]=image_orig[i,j]
				#else:
				#	image_resize_bg[i,j] = 255
					
		img_save(image_resize_bg,"pic_bg.jpg")		
		return image_resize_bg

def img_change_fg(image,image_cut):
		height,width = img_get_height_width(image)
		image_fg = image[0:height,0:width]

		#print("center_x:%d,center_y:%d\n"%(center_x,center_y))

		for i in range(height):
			for j in range(width):
				if image_cut[i,j]!=0:
					#print("i:%d,j:%d,blur[i,j]:%s\n"%(i,j,dilate[i,j]))
					image_fg[i,j]=image[i,j]+50
				else:
					image_fg[i,j] = 255
					
		img_save(image_fg,"pic_fg.jpg")
		return image_fg



# What model to download.
MODEL_NAME = 'rfcn_resnet101_clothes_11_23_2017'
#ssd_mobilenet_v1_clothes_11_22_2017
#'rfcn_resnet101_clothes_11_23_2017'
#'rfcn_resnet101_coco_11_06_2017'
#'ssd_mobilenet_v1_clothes_11_22_2017'  
#'ssd_mobilenet_v1_coco_11_06_2017' 
#'best rfcn_resnet101_coco_11_06_2017'  
#'faster_rcnn_resnet50_coco_2017_11_08.tar.gz'  
#ssd_inception_v2_coco_2017_11_08 
#'ssd_mobilenet_v1_coco_11_06_2017'
MODEL_FILE = MODEL_NAME + '.tar.gz'

# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'

# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join('data', 'clothes_label_map.pbtxt') #clocthes_label_map
NUM_CLASSES = 2

tar_file = tarfile.open(MODEL_FILE)
for file in tar_file.getmembers():
  file_name = os.path.basename(file.name)
  if 'frozen_inference_graph.pb' in file_name:
    tar_file.extract(file, os.getcwd())

detection_graph = tf.Graph()
with detection_graph.as_default():
  od_graph_def = tf.GraphDef()
  with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
    serialized_graph = fid.read()
    od_graph_def.ParseFromString(serialized_graph)
    tf.import_graph_def(od_graph_def, name='')

label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES, use_display_name=True)
category_index = label_map_util.create_category_index(categories)
  
def load_image_into_numpy_array(image):
  (im_width, im_height) = image.size
  print("boxes im_width:%d,im_height:%d"%(im_width,im_height))
  return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)
  

def img_grubcut_and_change_bg(img_path,img_bbox):
		#img_name = img_path.split('\\')[-1]
		#print("img_grubcut_and_change_bg img_name:%s"%(img_name))
		image_orig = img_open(img_path)
		mask = mask_build(image_orig)
		#image = img_contour(image_orig)	#must be gray	image
		image = img_grabcut(image_orig,mask,img_bbox) #must be bgr image
		#print("img:%s\n"%(image))
		image = img_bgr2gray(image)
		image = img_erode_dilate(image)
		image = img_medianblur(image)
		
		image_bg = img_open('blankit_bg.jpg')
		image_change_bg=img_change_bg(image_orig,image_bg,image)
		cv2.imshow('image_change_bg',image_change_bg)
		cv2.waitKey(0)
		
		#image_change_bg=img_change_fg(image_change_bg,image)
		#cv2.imshow('image_change_fg',image_change_fg)
		#cv2.waitKey(0)


def main():
		PATH_TO_TEST_IMAGES_DIR = 'test_images'
		TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image{}.jpg'.format(i)) for i in range(1, 5) ]
		IMAGE_SIZE = (12, 8)
		with detection_graph.as_default():
				with tf.Session(graph=detection_graph) as sess:
						# Definite input and output Tensors for detection_graph
						image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')
						# Each box represents a part of the image where a particular object was detected.
						detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')
						# Each score represent how level of confidence for each of the objects.
						# Score is shown on the result image, together with the class label.
						detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
						detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')
						num_detections = detection_graph.get_tensor_by_name('num_detections:0')
						#print("num_detections:%d"%(sess.run(num_detections)))
						for image_path in TEST_IMAGE_PATHS:
								print("image_path:%s"%(image_path))
								image = Image.open(image_path)

								# the array based representation of the image will be used later in order to prepare the
								# result image with boxes and labels on it.
								image_np = load_image_into_numpy_array(image)
								# Expand dimensions since the model expects images to have shape: [1, None, None, 3]
								image_np_expanded = np.expand_dims(image_np, axis=0)
								# Actual detection.
								(boxes, scores, classes, num) = sess.run(
								[detection_boxes, detection_scores, detection_classes, num_detections],
								feed_dict={image_tensor: image_np_expanded})
								image_bbox = boxes[0][0]
								print("image_bbox:%s"%(image_bbox))
								img_grubcut_and_change_bg(image_path,image_bbox)
								# Visualization of the results of a detection.
								vis_util.visualize_boxes_and_labels_on_image_array(
										image_np,
										np.squeeze(boxes),
										np.squeeze(classes).astype(np.int32),
										np.squeeze(scores),
										category_index,
										use_normalized_coordinates=True,
										line_thickness=2)
								plt.figure(figsize=IMAGE_SIZE)
								plt.imshow(image_np)
								plt.show()
								print("run success!!!")
	


if __name__ == "__main__":
		main()
		gc.collect() 
 
  
