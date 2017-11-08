'''
name:test_cnn_predict.py
create_date:9/15/2017
modified_date:10/10/2017
author:jimchen1218@sina.com
purpose:Traffic Sign Recognition .The goal is to build a model that can detect and classify traffic signs in a video stream taken from a moving car.
'''

import os
import random
import skimage.data
import skimage.transform
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import time
import argparse
import sys
import tempfile
from skimage import color
from PIL import Image

print (__doc__)

EPOCH_SIZE = 50
BATCH_SIZE = 5
LEARNING_RATE =0.001
IMAGE_SIZE =32
HIDDEN_SIZE = 256
CLASS_LABELS = 62
CROP_SIZE = 32

DATASETS_PATH = "datasets"
train_data_dir = os.path.join(DATASETS_PATH,"BelgiumTS/Training")
test_data_dir = os.path.join(DATASETS_PATH,"BelgiumTS/Testing")

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
						image = skimage.transform.resize(img, (img_crop_size,img_crop_size ))
						image=color.rgb2gray(image)
						images.append(image)
						id = int(d)
						#print("\nid:%s"%id)
						labels.append(id)
		return images, labels

def load_datasets_norm(data_dir,img_crop_size):
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
						#print("\nid:%s"%id)
						label =[0]*CLASS_LABELS
						for i in range(CLASS_LABELS):
								if i == id:									
										label[i] = 1
						labels.append(label)
						
		images_a = np.array(images)
		images = images_a.reshape([-1,IMAGE_SIZE,IMAGE_SIZE,1])
		
		labels_a = np.array(labels)
		labels = labels_a.reshape([-1,CLASS_LABELS])
		print("\nload_datasets_norm images shape:", images.shape)
		print("\nload_datasets_norm labels shape:", labels.shape)
		return images, labels

def display_images_and_labels(images, labels):
		print("\ndisplay_images_and_labels labels:",labels)
		unique_labels = set(labels)
		print("\ndisplay_images_and_labels unique_labels:%s"%(unique_labels))
		plt.figure(figsize=(15, 15))
		i = 1
		for label in unique_labels:
				image = images[labels.index(label)]
				plt.subplot(8, 8, i)
				plt.axis('off')
				plt.title("Label {0} ({1})".format(label, labels.count(label)))
				i += 1
				_ = plt.imshow(image)
		plt.show()

def predict_testimages(data_dir,sess,predicted_labels,images_ph,imagesize=IMAGE_SIZE):
		# Load the test dataset.
		pred_labels =[]
		test_images, test_labels = load_datasets(data_dir,CROP_SIZE)
		test_images_a = np.array(test_images)
		test_images_a = test_images_a.reshape([-1,IMAGE_SIZE,IMAGE_SIZE,1])
		display_images_and_labels(test_images, test_labels)
	
		# Run predictions against the full test set.
		prediction = sess.run([predicted_labels],feed_dict={images_ph: test_images_a})
		#predlen = prediction.shape[1]
'''		
		print("predict_testimages predlen:%s"%(predlen))
		testlen = len(test_labels)
		print("predict_testimages testlen:%s"%(testlen))
		for i in range(testlen):
		    predicted = prediction[i]
		    pred = np.argmax(predicted)
		    pred_labels.append(pred)
		match_count = sum([int(y == y_) for y, y_ in zip(test_labels, pred_labels)])
		test_len = len(test_labels)
		accuracy = match_count / test_len
		
		print("match_count: {:.3f}".format(match_count),"test_len: {:.3f}".format(test_len))
		print("Accuracy: {:.3f}".format(accuracy))
		print("time_duration: {:.5f}s".format(time_duration))
'''

def input_layer():
    x = tf.placeholder(tf.float32, [None, IMAGE_SIZE,IMAGE_SIZE,1], name="x-input")
    y_ = tf.placeholder(tf.float32, [None, CLASS_LABELS], name="y-input")
    keep_prob = tf.placeholder(tf.float32)
    return x,y_,keep_prob


def compute_cross_entropy(x,y):
    diff = -(x * tf.log(y))
    cross_entropy = tf.reduce_mean(diff)
    return cross_entropy

def train_optimizer(cross_entropy):
    train_opt = tf.train.AdamOptimizer(LEARNING_RATE).minimize(cross_entropy)
    return train_opt
    
def correct_prediction(x,y):
		correct_prediction = tf.equal(tf.argmax(x, 1), tf.argmax(y, 1))
		accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
		return accuracy

def cnn_model(input_x,input_y,keep_prob):
		weight1=tf.Variable(tf.truncated_normal(shape=[3,3,1,32],stddev=5e-2))
		kernel1=tf.nn.conv2d(input_x,weight1,[1,1,1,1],padding='SAME')
		bias1=tf.Variable(tf.constant(0.0,shape=[32]))
		conv1=tf.nn.relu(tf.nn.bias_add(kernel1,bias1))
		pool1=tf.nn.max_pool(conv1,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
		
		weight2=tf.Variable(tf.truncated_normal(shape=[3,3,32,64],stddev=5e-2))
		kernel2=tf.nn.conv2d(pool1,weight2,[1,1,1,1],padding='SAME')
		bias2=tf.Variable(tf.constant(0.0,shape=[64]))
		conv2=tf.nn.relu(tf.nn.bias_add(kernel2,bias2))
		pool2=tf.nn.max_pool(conv2,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')
		
		pool2_flat = tf.reshape(pool2, [-1, 8*8*64])
		
		weight3=tf.Variable(tf.truncated_normal(shape=[8*8*64,1024],stddev=0.04))
		bias3=tf.Variable(tf.constant(0.1,shape=[1024]))
		local3=tf.nn.relu(tf.matmul(pool2_flat,weight3)+bias3)
		
		weight4=tf.Variable(tf.truncated_normal(shape=[1024,CLASS_LABELS],stddev=5e-2))
		bias4=tf.Variable(tf.constant(0.1,shape=[CLASS_LABELS]))
		y=tf.nn.softmax(tf.matmul(local3,weight4)+bias4)
		
		cross_entropy = compute_cross_entropy(input_y,y)
		train_opt = train_optimizer(cross_entropy)
		accuracy = correct_prediction(y,input_y)
		return train_opt,accuracy,y


def predict_testrandomimages(data_dir,sess,predicted_labels,images_ph,imagesize=IMAGE_SIZE):
		# Load the test dataset.
		images, labels = load_datasets(data_dir,CROP_SIZE)
		# Pick 10 random images
		sample_indexes = random.sample(range(len(images)), 10)
		sample_images = [images[i] for i in sample_indexes]
		sample_labels = [labels[i] for i in sample_indexes]
		sample_images_a = np.array(sample_images)
		sample_images_a = sample_images_a.reshape([-1,IMAGE_SIZE,IMAGE_SIZE,1])
		predicted = sess.run([predicted_labels],feed_dict={images_ph: sample_images_a})[0]
		#print(sample_labels)
		#print(predicted)
		
		# Display the predictions and the ground truth visually.
		fig = plt.figure(figsize=(10, 10))
		for i in range(len(sample_images)):
		    truth = sample_labels[i]
		    prediction = predicted[i]
		    pred_label = np.argmax(prediction)
		    max = np.max(prediction)
		    print("max:%s"%(max))
		    print("pred_label:%s"%(pred_label))
		    print("total truth:%s \nprediction:%s \npredicted_label:%s"%(truth,prediction,pred_label))
		    plt.subplot(5, 2,1+i)
		    plt.axis('off')
		    if truth == pred_label:
		    		color = 'green'
		    else:
		    		color = 'red'
		    plt.text(40, 10,"Truth:{0} Prediction: {1}".format(truth, pred_label),fontsize=12, color=color)
		    plt.imshow(sample_images[i])
		plt.show()

def main(_):
		sess = tf.InteractiveSession()
		tempdir = os.getcwd()
		print("tempdir:%s"%(tempdir))
		time_start=time.time()
		images, labels = load_datasets_norm(train_data_dir,CROP_SIZE)

		x,y_,keep_prob = input_layer()
		train_opt,accuracy,predicted_labels = cnn_model(x,y_,keep_prob)
		
		merged = tf.summary.merge_all()
		train_writer = tf.summary.FileWriter(tempdir + '/train',sess.graph)
		test_writer = tf.summary.FileWriter(tempdir + '/test')

		tf.global_variables_initializer().run()
		
		for i in range(FLAGS.max_steps):
				_,acc = sess.run([train_opt,accuracy], feed_dict={x: images, y_: labels, keep_prob: 0.8})
				if i % BATCH_SIZE == 0:
					print('Accuracy at step %s: %s' % (i, acc))
		predict_testrandomimages(test_data_dir,sess,predicted_labels,x)
		#predict_testimages(test_data_dir,sess,predicted_labels,x)
		time_duration=time.time() - time_start
		print("total time_duration:%ss"%(time_duration))
		
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.register("type", "bool", lambda v: v.lower() == "true")
    parser.add_argument(
        "--max_steps",
        type=int,
        default=EPOCH_SIZE,
        help="Number of steps to run trainer.")
    parser.add_argument(
        "--learning_rate",
        type=float,
        default=LEARNING_RATE,
        help="Initial learning rate.")
    parser.add_argument(
        "--data_dir",
        type=str,
        default=DATASETS_PATH,
        help="Directory for storing data")
    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)