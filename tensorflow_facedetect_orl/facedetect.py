'''
name:facedetect.py
create date:10/11/2017
author:jimchen1218@sina.com
datasets:orl face datasets
'''

import tensorflow as tf
from skimage import color
#from PIL import Image
import skimage.data
import skimage.transform
#import matplotlib
import matplotlib.pyplot as plt
import numpy as np

import time
import argparse
import sys
import os
import random
#import tempfile

print (__doc__)

EPOCH_SIZE = 30    #30 best value ;50 overfit;10 underfit
BATCH_SIZE = 5
LEARNING_RATE =0.001
CROP_IMAGE_SIZE =64
KERNEL_SIZE = 3
C1_HIDDEN_SIZE = 128
FC_HIDDEN_SIZE = 1024
CLASS_LABELS = 40
PREDICT_RANDOM_SIZE = 5

ROOT_DIRECTORY_NAME = "firstjob"
train_data_dir ="datasets/Face/Training"
test_data_dir ="datasets/Face/Testing"

#加载数据集
def load_datasets(data_dir,img_crop_size):
    directories = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]
    #print("load_datasets directories:%s"%(directories))
    images = []
    labels = []
    for d in directories:
        label_dir = os.path.join(data_dir, d)
        file_names = [os.path.join(label_dir, f) for f in os.listdir(label_dir) if f.endswith(".bmp")]
        for f in file_names:
            img = skimage.data.imread(f)
            #width,height,colors = img.shape
            #print("\nwidth:%d,height:%d"%(width,height))
            image = skimage.transform.resize(img, (CROP_IMAGE_SIZE,CROP_IMAGE_SIZE ))
            #image=color.rgb2gray(image)
            images.append(image)
            id = int(d)
            #print("\nid:%s"%id)
            labels.append(id)
    return images, labels

#加载数据集，返回指定格式用于图像模型训练
def load_datasets_ext(data_dir,img_crop_size):
    directories = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]
    images = []
    labels = []
    
    for d in directories:
        label_dir = os.path.join(data_dir, d)
        file_names = [os.path.join(label_dir, f) for f in os.listdir(label_dir) if f.endswith(".bmp")]
        for f in file_names:
            img = skimage.data.imread(f)
            image = skimage.transform.resize(img, (CROP_IMAGE_SIZE,CROP_IMAGE_SIZE))
            #image=color.rgb2gray(image)
            images.append(image)
            id = int(d)
            label =[0]*CLASS_LABELS
            for i in range(CLASS_LABELS):
                if i == id:
                    label[i] = 1
            labels.append(label)

    images_a = np.array(images)
    images = images_a.reshape([-1,CROP_IMAGE_SIZE,CROP_IMAGE_SIZE,3])
    labels_a = np.array(labels)
    labels = labels_a.reshape([-1,CLASS_LABELS])
    print("\nload_datasets_ext images shape:", images.shape)
    print("\nload_datasets_ext labels shape:", labels.shape)
    return images, labels

#输入层
def input_layer():
    x = tf.placeholder(tf.float32, [None, CROP_IMAGE_SIZE,CROP_IMAGE_SIZE,3], name="x-input")
    y_ = tf.placeholder(tf.float32, [None, CLASS_LABELS], name="y-input")
    keep_prob = tf.placeholder(tf.float32)
    return x,y_,keep_prob

#计算交叉熵
def compute_crossentropy(x,y):
    diff = -(x * tf.log(y))
    cross_entropy = tf.reduce_mean(diff)
    return cross_entropy

#BP算法：使用ADAM优化器来最小化交叉熵
def train_optimizer(cross_entropy):
    train_opt = tf.train.AdamOptimizer(LEARNING_RATE).minimize(cross_entropy)
    return train_opt

#统计正确率：计算预测值与真实值之间的比值
def correct_prediction(x,y):
    correct_prediction = tf.equal(tf.argmax(x, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    return accuracy

#使用TENSORFLOW搭建CNN模型：2个卷积层+2个最大池化层+1个全连接层+SOFTMAX分类层
def cnn_model(input_x,input_y,keep_prob,imagesize=CROP_IMAGE_SIZE):
    weight1=tf.Variable(tf.truncated_normal(shape=[KERNEL_SIZE,KERNEL_SIZE,3,imagesize],stddev=5e-2))
    kernel1=tf.nn.conv2d(input_x,weight1,[1,1,1,1],padding='SAME')
    bias1=tf.Variable(tf.constant(0.0,shape=[imagesize]))
    conv1=tf.nn.relu(tf.nn.bias_add(kernel1,bias1))
    pool1=tf.nn.max_pool(conv1,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

    weight2=tf.Variable(tf.truncated_normal(shape=[KERNEL_SIZE,KERNEL_SIZE,imagesize,C1_HIDDEN_SIZE],stddev=5e-2))
    kernel2=tf.nn.conv2d(pool1,weight2,[1,1,1,1],padding='SAME')
    bias2=tf.Variable(tf.constant(0.0,shape=[C1_HIDDEN_SIZE]))
    conv2=tf.nn.relu(tf.nn.bias_add(kernel2,bias2))
    pool2=tf.nn.max_pool(conv2,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

    pool2_flat = tf.reshape(pool2, [-1, 16*16*C1_HIDDEN_SIZE])

    weight3=tf.Variable(tf.truncated_normal(shape=[16*16*C1_HIDDEN_SIZE,FC_HIDDEN_SIZE],stddev=0.04))
    bias3=tf.Variable(tf.constant(0.1,shape=[FC_HIDDEN_SIZE]))
    fullconnection1=tf.nn.relu(tf.matmul(pool2_flat,weight3)+bias3)
    
    fullconnection1_drop = tf.nn.dropout(fullconnection1, keep_prob)

    weight4=tf.Variable(tf.truncated_normal(shape=[FC_HIDDEN_SIZE,CLASS_LABELS],stddev=5e-2))
    bias4=tf.Variable(tf.constant(0.1,shape=[CLASS_LABELS]))
    y=tf.nn.softmax(tf.matmul(fullconnection1_drop,weight4)+bias4)

    cross_entropy = compute_crossentropy(input_y,y)
    train_opt = train_optimizer(cross_entropy)
    accuracy = correct_prediction(y,input_y)
    return train_opt,accuracy,y

#随机选择若干目标图像进行预测，使用MATPLOTLIB显示图像。
def predict_randomimages(data_dir,sess,predicted_labels,images_ph,keep_prob,imagesize=CROP_IMAGE_SIZE):
    images, labels = load_datasets(data_dir,imagesize)
    sample_indexes = random.sample(range(len(images)), PREDICT_RANDOM_SIZE)
    sample_images = [images[i] for i in sample_indexes]
    sample_labels = [labels[i] for i in sample_indexes]
    sample_images_a = np.array(sample_images)
    sample_images_a = sample_images_a.reshape([-1,imagesize,imagesize,3])
    predicted = sess.run([predicted_labels],feed_dict={images_ph: sample_images_a, keep_prob: 1.0})[0]

    corr_num = 0
    total_num = len(sample_images)
    plt.figure(figsize=(10, 10))
    for i in range(total_num):
        true_label = sample_labels[i]
        prediction = predicted[i]
        pred_label = np.argmax(prediction)
        #max = np.max(prediction)
        #print("max:%s"%(max))
        print("\npredict label:%s \ntrue label:%d"%(pred_label,true_label))
        #print("total truth:%s \nprediction:%s \npredicted_label:%s"%(truth,prediction,pred_label))
        plt.subplot(PREDICT_RANDOM_SIZE, 1,1+i)
        plt.axis('off')
        if true_label == pred_label:
            corr_num  = corr_num + 1
            color = 'green'
        else:
            color = 'red'
        plt.text(40, 10,"Truth:{0} Prediction: {1}".format(true_label, pred_label),fontsize=12, color=color)
        plt.imshow(sample_images[i])
    plt.show()
    accuracy = int((corr_num / total_num)*100)
    print("\nmatch numbers: %d ,total numbers:%d"%(corr_num,total_num))
    print("Accuracy: %d%%"%(accuracy))

#主函数
def main(_):
    sess = tf.InteractiveSession()
    #tempdir = os.getcwd()
    #print("tempdir:%s"%(tempdir))
    time_start=time.time()
    images, labels = load_datasets_ext(train_data_dir,CROP_IMAGE_SIZE)
    x,y_,keep_prob = input_layer()
    train_opt,accuracy,predicted_labels = cnn_model(x,y_,keep_prob)
    tf.global_variables_initializer().run()
    for i in range(FLAGS.max_steps+1):
        _,acc = sess.run([train_opt,accuracy], feed_dict={x: images, y_: labels, keep_prob: 0.5})
        if i % BATCH_SIZE == 0:
        	print('Accuracy at step %s: %s' % (i, acc))
    predict_randomimages(test_data_dir,sess,predicted_labels,x,keep_prob)
    time_duration=int(time.time() - time_start)
    print("total time duration:%ss"%(time_duration))

#程序主入口
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
        default=ROOT_DIRECTORY_NAME,
        help="Directory for storing data")
    FLAGS, unparsed = parser.parse_known_args()
    tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)