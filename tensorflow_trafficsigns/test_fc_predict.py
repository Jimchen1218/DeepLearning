
'''
name:test_fc_predict.py
create_date:9/15/2017
author:jimchen1218@sina.com
purposeTraffic Sign Recognition .The goal is to build a model that can detect and classify traffic signs in a video stream taken from a moving car.
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

EPOCH_SIZE = 3000
BATCH_SIZE = 10
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
						labels.append(id)
		return images, labels

def simple_input_layer(layer_name):
    x = tf.placeholder(tf.float32, [None, IMAGE_SIZE,IMAGE_SIZE], name="x-input")
    y_ = tf.placeholder(tf.int32, [None], name="y-input")
    keep_prob = tf.placeholder(tf.float32)
    return x,y_,keep_prob

def correct_prediction(x,y):
		correct_prediction = tf.equal(tf.argmax(x, 1), tf.argmax(y, 1))
		accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
		return accuracy

def simple_fc_model(layer_name,images_ph,labels_ph,output_size):
		images_flat = tf.contrib.layers.flatten(images_ph)
		logits = tf.contrib.layers.fully_connected(images_flat,output_size, tf.nn.relu)
		predicted_labels = tf.argmax(logits, 1)
		loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=labels_ph,logits=logits))
		train = tf.train.AdamOptimizer(learning_rate=LEARNING_RATE).minimize(loss)
		#accuracy = correct_prediction(predicted_labels,labels_ph)
		#tf.summary.scalar('cross_entropy', loss)
		return train,loss,predicted_labels

def predict_testrandomimages(data_dir,sess,predicted_labels,images_ph,imagesize=IMAGE_SIZE):
		images, labels = load_datasets(data_dir,CROP_SIZE)
		# Pick 10 random images
		sample_indexes = random.sample(range(len(images)), 5)
		sample_images = [images[i] for i in sample_indexes]
		sample_labels = [labels[i] for i in sample_indexes]
		sample_images_a = np.array(sample_images)
		sample_images_a = sample_images_a.reshape([-1,IMAGE_SIZE,IMAGE_SIZE])
		predicted = sess.run([predicted_labels],feed_dict={images_ph:sample_images_a})[0]
		print(sample_labels)
		print(predicted)
		
		fig = plt.figure(figsize=(10, 10))
		for i in range(len(sample_images)):
		    truth = sample_labels[i]
		    pred_label = predicted[i]
		    #pred_label = np.argmax(prediction)
			  #max = np.max(prediction)	    
		    print("\npredict_testrandomimages truth:%s pred_label:%s"%(truth,pred_label))
				#pred_label = prediction
		    plt.subplot(5, 1,1+i)
		    plt.axis('off')
		    if truth == pred_label:
		    		color = 'green'
		    else:
		    		color = 'red'
		    plt.text(40, 10,"Truth:{0} Prediction:{1}".format(truth, pred_label),fontsize=12, color=color)
		    plt.imshow(sample_images[i])
		plt.show()

def main(_):
		sess = tf.InteractiveSession()
		tempdir = os.getcwd()
		time_start=time.time()
		images, labels = load_datasets(train_data_dir,CROP_SIZE)

		x,y_,keep_prob = simple_input_layer("input_layer")
		train,loss,predicted_labels = simple_fc_model("simple_fc_model",x,y_,CLASS_LABELS)
		tf.global_variables_initializer().run()
		for i in range(FLAGS.max_steps):
				_,l = sess.run([train,loss], feed_dict={x:images, y_:labels, keep_prob:0.8})
				if i % BATCH_SIZE == 0:
					print("\nLoss at step %s loss:%s"%(i, l))
		predict_testrandomimages(test_data_dir,sess,predicted_labels,x)
		time_duration=time.time() - time_start
		
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.register("type", "bool", lambda v:v.lower() == "true")
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