'''
filename: model.py
createdate:2/8/2018
author:jim.chen
'''

import numpy as np
import tensorflow as tf
import os
import glob
from skimage import io, transform

print(__doc__)

IMAGE_WIDTH = 224
IMAGE_HEIGHT = 224
IMAGE_CHANNEL = 3

def build_datasets(path,width,height,channel,ratio = 0.8):
    
    def read_imgs(path,width,height,channel):
        imgs   = []
        labels = []
        cate   = [path + x for x in os.listdir(path) if os.path.isdir(path + x)]
        for idx, folder in enumerate(cate):
            for im in glob.glob(folder + '/*.jpg'):
                print('read_img_datasets reading the image: %s' % (im))
                img = io.imread(im)
                img = transform.resize(img, (width, height, channel))
                imgs.append(img)
                labels.append(idx)
        return np.asarray(imgs, np.float32), np.asarray(labels, np.int32)

    data, label = read_imgs(path,width,height,channel)
    num_sample = data.shape[0]
    arr = np.arange(num_sample)
    np.random.shuffle(arr)
    data = data[arr]
    label = label[arr]
    #print('read_img_datasets reading the image: %s' % (data))
    #print('read_img_datasets reading the label: %s' % (label))
    s = np.int(num_sample * ratio)
    train_x = data[:s]
    train_y = label[:s]
    val_x  = data[s:]
    val_y   = label[s:]
    #print('read_img_datasets reading the train_y: %s' % (train_y))
    #print('read_img_datasets reading the val_y: %s' % (val_y))
    return train_x,train_y,val_x,val_y

def build_mobilenet(height, width, channel):
    x = tf.placeholder(tf.float32, shape=[None, height, width, channel], name='input')
    y = tf.placeholder(tf.int64, shape=[None, 2], name='labels')

    def weight_variable(shape, name="weights"):
        initial = tf.truncated_normal(shape, dtype=tf.float32, stddev=0.1)
        return tf.Variable(initial, name=name)

    def bias_variable(shape, name="biases"):
        initial = tf.constant(0.1, dtype=tf.float32, shape=shape)
        return tf.Variable(initial, name=name)

    def conv2d(input, kernel, stride):
        return tf.nn.conv2d(input, filter=kernel, strides=stride, padding='SAME')

    def conv2d_dw(input, kernel, stride):
        return tf.nn.depthwise_conv2d(input, filter=kernel, strides=stride, rate=[1,1], padding='SAME')

    def pool_avg(input):
        return tf.nn.avg_pool(input,ksize=[1, 7, 7, 1],strides=[1, 2, 2, 1],padding='SAME', name='pool1')

    def fc(input, w, b):
        return tf.matmul(input, w) + b

    #build mobilenet
    with tf.name_scope('l1_conv2d') as scope:
        kernel = weight_variable([3, 3, 3, 32])
        biases = bias_variable([32])
        l1 = tf.nn.relu(conv2d(x, kernel,[1,2,2,1]) + biases, name=scope)

    with tf.name_scope('l2_conv2d_dw') as scope:
        kernel = weight_variable([3, 3, 32, 1])
        biases = bias_variable([1])
        l2 = tf.nn.relu(conv2d_dw(l1, kernel,[1,2,2,1]) + biases, name=scope)

    with tf.name_scope('l3_conv2d') as scope:
        kernel = weight_variable([1, 1, 32, 64])
        biases = bias_variable([64])
        l3 = tf.nn.relu(conv2d(l2, kernel,[1,1,1,1]) + biases, name=scope)

    with tf.name_scope('l4_conv2d_dw') as scope:
        kernel = weight_variable([3, 3, 64, 1])
        biases = bias_variable([1])
        l4 = tf.nn.relu(conv2d_dw(l3, kernel,[1,2,2,1]) + biases, name=scope)

    with tf.name_scope('l5_conv2d') as scope:
        kernel = weight_variable([1, 1, 64, 128])
        biases = bias_variable([128])
        l5 = tf.nn.relu(conv2d(l4, kernel,[1,1,1,1]) + biases, name=scope)

    with tf.name_scope('l6_conv2d_dw') as scope:
        kernel = weight_variable([3, 3, 128, 1])
        biases = bias_variable([1])
        l6 = tf.nn.relu(conv2d_dw(l5, kernel,[1,2,2,1]) + biases, name=scope)

    with tf.name_scope('l9_conv2d') as scope:
        kernel = weight_variable([1, 1, 128, 256])
        biases = bias_variable([256])
        l9 = tf.nn.relu(conv2d(l6, kernel,[1,1,1,1]) + biases, name=scope)

    with tf.name_scope('l10_conv2d_dw') as scope:
        kernel = weight_variable([3, 3, 256, 1])
        biases = bias_variable([1])
        l10 = tf.nn.relu(conv2d_dw(l9, kernel,[1,2,2,1]) + biases, name=scope)
        
    with tf.name_scope('l13_conv2d') as scope:
        kernel = weight_variable([1, 1, 256, 512])
        biases = bias_variable([512])
        l13 = tf.nn.relu(conv2d(l10, kernel,[1,1,1,1]) + biases, name=scope)
    
    with tf.name_scope('l24_conv2d_dw') as scope:
        kernel = weight_variable([3, 3, 512, 1])
        biases = bias_variable([1])
        l24 = tf.nn.relu(conv2d_dw(l13, kernel,[1,2,2,1]) + biases, name=scope)
        
    with tf.name_scope('l25_conv2d') as scope:
        kernel = weight_variable([1, 1, 512, 1024])
        biases = bias_variable([1024])
        l25 = tf.nn.relu(conv2d(l24, kernel,[1,1,1,1]) + biases, name=scope)
        
    with tf.name_scope('l26_conv2d_dw') as scope:
        kernel = weight_variable([3, 3, 1024, 1])
        biases = bias_variable([1])
        l26 = tf.nn.relu(conv2d_dw(l25, kernel,[1,2,2,1]) + biases, name=scope)
  
    with tf.name_scope('l27_conv2d') as scope:
        kernel = weight_variable([1, 1, 1024, 1024])
        biases = bias_variable([1024])
        l27 = tf.nn.relu(conv2d(l26, kernel,[1,1,1,1]) + biases, name=scope)
        
    with tf.name_scope('l28_pool_avg') as scope:
        l28 = tf.nn.relu(pool_avg(l27), name=scope)

    with tf.name_scope('l29') as scope:
        l29_reshape = tf.reshape(l28,[-1,1024])
        kernel = weight_variable([1024, 2])
        biases = bias_variable([2])
        l29 = tf.nn.relu(fc(l29_reshape, kernel, biases), name=scope)

    logit = tf.nn.softmax(l29, name="softmax")
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=logit, labels=y))
    opt = tf.train.AdamOptimizer(learning_rate=1e-4).minimize(cost)

    pred_labels = tf.argmax(logit, axis=1, name="output")
    true_labels = y
    print('build_mobilenet reading the pred_labels: %s' % (pred_labels))
    print('build_mobilenet reading the true_labels: %s' % (true_labels))
    #true_labels = tf.reshape(true_labels,[4])
    correct_pred = tf.equal(pred_labels, true_labels)
    
    acc = tf.reduce_mean(tf.cast(correct_pred, tf.float32))

    correct_times_in_batch = tf.reduce_sum(tf.cast(correct_pred, tf.int32))

    return dict(
        x=x,
        y=y,
        optimize=opt,
        correct_prediction=correct_pred,
        correct_times_in_batch=correct_times_in_batch,
        cost=cost,
        accuracy=acc,
    )




