'''
name:test_traffic_signals.py
create_date:9/15/2017
author:jimchen1218@sina.com
purpose:Traffic Sign Recognition .The goal is to build a model that can detect and classify traffic signs in a video stream taken from a moving car.
fullconnect 
	epochsize:500,learningrate:0.01 accuracy:8%
	epochsize:2000,learningrate:0.01 accuracy:35.6%,34.2%,39.5%
	epochsize:3000,10000,learningrate:0.01 accuracy:3.3%
	epochsize:2000,learningrate:0.1 accuracy:8.9%
	epochsize:1000,learningrate:0.01 accuracy:8.8%
	epochsize:2500,learningrate:0.01 accuracy:52.2%
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

RAND_SEED = 42
EPOCH_SIZE = 2500
BATCH_SIZE = 128
LEARNING_RATE =0.01
IMAGE_SIZE =32
HIDDEN_SIZE = 256
CLASS_LABELS = 62
CROP_SIZE = 32

DATASETS_PATH = "traffic_signs"
train_data_dir = os.path.join(DATASETS_PATH,"datasets/BelgiumTS/Training")
test_data_dir = os.path.join(DATASETS_PATH,"datasets/BelgiumTS/Testing")

def load_datasets(data_dir,img_crop_size):
		directories = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]
		print("load_datasets directories:%s"%(directories))
		images = []
		labels = []
		for d in directories:
				label_dir = os.path.join(data_dir, d)
				file_names = [os.path.join(label_dir, f) for f in os.listdir(label_dir) if f.endswith(".ppm")]
				for f in file_names:
						img = skimage.data.imread(f)
						image = skimage.transform.resize(img, (img_crop_size,img_crop_size ))
						images.append(image)
						labels.append(int(d))
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
										#print("\ni==id i:%d,id:%d"%(i,id))
										label[i] = 1
						#print("\nlabel:",label)
						labels.append(label)
						
		images_a = np.array(images)
		print("\nload_datasets_norm images shape:", images_a.shape)
		images = images_a.reshape([-1,IMAGE_SIZE,IMAGE_SIZE,1])				
		return images, labels


def display_images_and_labels(images, labels):
    unique_labels = set(labels)
    print("display_images_and_labels unique_labels:%s"%(unique_labels))
    plt.figure(figsize=(15, 15))
    i = 1
    for label in unique_labels:
        image = images[labels.index(label)]
        plt.subplot(8, 8, i)
        plt.axis('off')
        plt.title("Label {0} ({1})".format(label, labels.count(label)))
        i += 1
        _ = plt.imshow(image)
    #plt.show()


def simple_input_layer(layer_name):
    with tf.name_scope(layer_name):
        x = tf.placeholder(tf.float32, [None, IMAGE_SIZE,IMAGE_SIZE,1], name="x-input")
        y_ = tf.placeholder(tf.int32, [None], name="y-input")
        keep_prob = tf.placeholder(tf.float32)
    return x,y_,keep_prob

def simple_fc_model(layer_name,images_ph,labels_ph,output_size):
		with tf.name_scope(layer_name):
				images_flat = tf.contrib.layers.flatten(images_ph)
				logits = tf.contrib.layers.fully_connected(images_flat,output_size, tf.nn.relu)
				predicted_labels = tf.argmax(logits, 1)
		with tf.name_scope('loss'): 
				loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=labels_ph,logits=logits))
		with tf.name_scope('train'):
				train = tf.train.AdamOptimizer(learning_rate=LEARNING_RATE).minimize(loss)
		#accuracy = correct_prediction(predicted_labels,labels_ph)
		tf.summary.scalar('cross_entropy', loss)
		return train,loss,predicted_labels

'''	
cnn
		for i in range(FLAGS.max_steps):
			if i % BATCH_SIZE == 0:
					summary, acc = sess.run([merged, accuracy], feed_dict={x: images_a, y_: labels_a, keep_prob: 1.0})
					print('Accuracy at step %s: %s' % (i, acc))
			else:
					summary, _ = sess.run([merged, train_opt], feed_dict={x: images_a, y_: labels_a, keep_prob: 1.0})
					
fc					
		for i in range(FLAGS.max_steps):
				summary,_ ,loss_val = sess.run([merged,train,loss],feed_dict={x: images_a, y_: labels_a})
				#_ ,loss_val = sess.run([train,loss],feed_dict={x: images_a, y_: labels_a})
				train_writer.add_summary(summary, i)
				if i % BATCH_SIZE == 0:
						print("i:%d \nloss_val:%s"%(i,loss_val))					
'''
def test_random_images(images,labels,images_ph,predicted_labels,sess):
		# Pick 10 random images
		sample_indexes = random.sample(range(len(images)), 10)
		sample_images = [images[i] for i in sample_indexes]
		sample_labels = [labels[i] for i in sample_indexes]
		predicted = sess.run([predicted_labels],feed_dict={images_ph: sample_images})[0]
		print(sample_labels)
		print(predicted)
		
		# Display the predictions and the ground truth visually.
		fig = plt.figure(figsize=(10, 10))
		for i in range(len(sample_images)):
		    truth = sample_labels[i]
		    prediction = predicted[i]
		    plt.subplot(5, 2,1+i)
		    plt.axis('off')
		    if truth == prediction:
		    		color = 'green'
		    else:
		    		color = 'red'
		    plt.text(40, 10,"Truth:{0} Prediction: {1}".format(truth, prediction),fontsize=12, color=color)
		    plt.imshow(sample_images[i])
		#plt.show()

def predict_testimages(data_dir,sess,predicted_labels,images_ph,imagesize=IMAGE_SIZE):
		# Load the test dataset.
		test_images, test_labels = load_datasets_norm(data_dir,CROP_SIZE)
		display_images_and_labels(test_images, test_labels)
		
		# Run predictions against the full test set.
		predicted = sess.run([predicted_labels],feed_dict={images_ph: test_images})[0]
		match_count = sum([int(y == y_) for y, y_ in zip(test_labels, predicted)])
		test_len = len(test_labels)
		accuracy = match_count / test_len
		
		print("match_count: {:.3f}".format(match_count),"test_len: {:.3f}".format(test_len))
		print("Accuracy: {:.3f}".format(accuracy))
		#print("time_duration: {:.5f}s".format(time_duration))

def input_layer():
    x = tf.placeholder(tf.float32, [None, IMAGE_SIZE,IMAGE_SIZE,1], name="x-input")
    y_ = tf.placeholder(tf.float32, [None, CLASS_LABELS], name="y-input")
    keep_prob = tf.placeholder(tf.float32)
    return x,y_,keep_prob


def compute_cross_entropy(x,y):
    #diff = tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y)
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
		pool1=tf.nn.max_pool(conv1,ksize=[1,3,3,1],strides=[1,2,2,1],padding='SAME')
		
		weight2=tf.Variable(tf.truncated_normal(shape=[3,3,32,64],stddev=5e-2))
		kernel2=tf.nn.conv2d(pool1,weight2,[1,1,1,1],padding='SAME')
		bias2=tf.Variable(tf.constant(0.0,shape=[64]))
		conv2=tf.nn.relu(tf.nn.bias_add(kernel2,bias2))
		pool2=tf.nn.max_pool(conv2,ksize=[1,3,3,1],strides=[1,2,2,1],padding='SAME')
		
		reshape=tf.reshape(pool2,[64,-1])
		dim=reshape.get_shape()[1].value
		
		weight3=tf.Variable(tf.truncated_normal(shape=[dim,192],stddev=0.04))
		bias3=tf.Variable(tf.constant(0.1,shape=[192]))
		local3=tf.nn.relu(tf.matmul(reshape,weight3)+bias3)
		
		weight4=tf.Variable(tf.truncated_normal(shape=[192,CLASS_LABELS],stddev=5e-2))
		bias4=tf.Variable(tf.constant(0.1,shape=[CLASS_LABELS]))
		y=tf.nn.softmax(tf.matmul(local3,weight4)+bias4)
		
		cross_entropy = compute_cross_entropy(input_y,y)
		train_opt = train_optimizer(cross_entropy)
		accuracy = correct_prediction(y,input_y)
		return train_opt,accuracy

def main(_):
		sess = tf.InteractiveSession()
		tempdir = os.getcwd()
		print("tempdir:%s"%(tempdir))
		time_start=time.time()
		images, labels = load_datasets_norm(train_data_dir,CROP_SIZE)


		x,y_,keep_prob = input_layer()
		train_opt,accuracy = cnn_model(x,y_,keep_prob)
		
		#x,y_,keep_prob = simple_input_layer("input_layer")
		#train,loss,predicted_labels = simple_fc_model("simple_fc_model",x,y_,CLASS_LABELS)
		merged = tf.summary.merge_all()
		train_writer = tf.summary.FileWriter(tempdir + '/train',sess.graph)
		test_writer = tf.summary.FileWriter(tempdir + '/test')

		tf.global_variables_initializer().run()
		
		for i in range(FLAGS.max_steps):
			if i % BATCH_SIZE == 0:
					summary, acc = sess.run([accuracy], feed_dict={x: images, y_: labels, keep_prob: 1.0})
					print('Accuracy at step %s: %s' % (i, acc))
			else:
					summary, _ = sess.run([train_opt], feed_dict={x: images, y_: labels, keep_prob: 1.0})
						
		#test_random_images(images,labels,x,predicted_labels,sess)
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



















