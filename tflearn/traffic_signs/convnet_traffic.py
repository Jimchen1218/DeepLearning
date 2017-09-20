'''
name:convnet_traffic.py
create_date:9/19/2017
author:jimchen1218@sina.com
purpose:Traffic Sign Recognition .The goal is to build a model that can detect and classify traffic signs in a video stream taken from a moving car.
'''

from __future__ import division, print_function, absolute_import  
  
import tflearn  
from tflearn.layers.core import input_data, dropout, fully_connected  
from tflearn.layers.conv import conv_2d, max_pool_2d  
from tflearn.layers.normalization import local_response_normalization  
from tflearn.layers.estimator import regression  

import os
import random
import skimage.data
import skimage.transform
from skimage import color
from PIL import Image
import numpy as np
import tensorflow as tf
import time
import argparse
import sys
import tempfile
import tflearn.datasets.mnist as mnist



print(__doc__)


IMAGE_SIZE =32
CLASS_LABELS =62
DATASETS_PATH = "traffic_signs"
train_data_dir = os.path.join(DATASETS_PATH,"datasets/BelgiumTS/Training")
test_data_dir = os.path.join(DATASETS_PATH,"datasets/BelgiumTS/Testing")
predict_image_dir = os.path.join(DATASETS_PATH,"4.ppm")

def load_datasets(data_dir,img_crop_size):
		directories = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]
		#print("load_datasets directories:%s"%(directories))
		images = []
		labels = []
		for d in directories:
				label_dir = os.path.join(data_dir, d)
				file_names = [os.path.join(label_dir, f) for f in os.listdir(label_dir) if f.endswith(".ppm")]
				for f in file_names:
						img = skimage.data.imread(f)
						image = skimage.transform.resize(img, (img_crop_size,img_crop_size))
						image=color.rgb2gray(image)
						images.append(image)
						id = int(d)
						label =[0]*CLASS_LABELS
						for i in range(CLASS_LABELS):
								if i == id:
										#print("\ni==id i:%d,id:%d"%(i,id))
										label[i] = 1
						#print("\nlabel:",label)
						labels.append(label)
		return images, labels

def resize_image(in_image, new_width, new_height, out_image=None,
                 resize_mode=Image.ANTIALIAS):
    img = in_image.resize((new_width, new_height), resize_mode)
    if out_image:
        img.save(out_image)
    return img

def pil_to_nparray(pil_image):
    pil_image.load()
    return np.asarray(pil_image, dtype="float32")


def load_dataset_mnist(path_dir):
		import tflearn.datasets.mnist as mnist  
		X, Y, testX, testY = mnist.load_data(one_hot=True)
		X = X.reshape([-1, 28, 28, 1])  
		testX = testX.reshape([-1, 28, 28, 1]) 
		return X,Y,testX,testY 


def load_dataset_traffic(path_dir):
		images, labels = load_datasets(path_dir,IMAGE_SIZE)
		images_a = np.array(images)
		labels_a = np.array(labels)
		print("\nimages shape:", images_a.shape)
		print("\nlabels shape:", labels_a.shape)
		images = images_a.reshape([-1,IMAGE_SIZE,IMAGE_SIZE,1])
		print("\nimages shape:", images.shape)
		return images,labels


def convnet(img_crop_size,num_classes):
		network = input_data(shape=[None, img_crop_size, img_crop_size, 1], name='input')
		# CNN
		network = conv_2d(network, 32, 3, activation='relu', regularizer="L2")  
		network = max_pool_2d(network, 4)  
		network = local_response_normalization(network)  
		network = conv_2d(network, 64, 3, activation='relu', regularizer="L2")
		network = max_pool_2d(network, 2)  
		network = local_response_normalization(network)
		# Full connection
		network = fully_connected(network, 128, activation='tanh')
		network = dropout(network, 0.5)  
		network = fully_connected(network, num_classes, activation='softmax')
		# Regression
		network = regression(network, optimizer='adam', learning_rate=0.01,
		                     loss='categorical_crossentropy', name='target') 
		return network 
  

def train(network, X, Y):
    model = tflearn.DNN(network)
    if os.path.isfile('model_convnet.model'):
        model.load('model_convnet.model')
    model.fit(X, Y, n_epoch=10, validation_set=0.1, shuffle=True,
              show_metric=True, batch_size=64, snapshot_step=200,
              snapshot_epoch=False, run_id='convnet')
    model.save('model_convnet.model')
    return model


def load_predict_image(img_path,img_crop_size):
		img = skimage.data.imread(img_path)
		image = skimage.transform.resize(img, (img_crop_size,img_crop_size))
		image=color.rgb2gray(image)
		image = image.reshape([-1,IMAGE_SIZE,IMAGE_SIZE,1])
		return image

# Training
if __name__ == '__main__':
		images,labels = load_dataset_traffic(train_data_dir)
		time_start = time.time()
		net = convnet(IMAGE_SIZE,CLASS_LABELS)
		model = train(net,images,labels)
		predict_image = load_predict_image(predict_image_dir,IMAGE_SIZE)
		pred = model.predict(predict_image)
		print("\nmain pred:%s"%pred)
		time_duration = time.time() - time_start
		print("\nmodel training duration:%ss"%time_duration)
		
		

           
        
