# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 18:29:50 2018

@author: Jim.chen
"""

'''
    #repeat 5 times begin
    with tf.name_scope('l14_conv2d_dw') as scope:
        kernel = weight_variable([3, 3, 512, 1])
        biases = bias_variable([1])
        l14 = tf.nn.relu(conv2d_dw(l13, kernel,[1,1,1,1]) + biases, name=scope)

    with tf.name_scope('l15_conv2d') as scope:
        kernel = weight_variable([1, 1, 512, 512])
        biases = bias_variable([512])
        l15 = tf.nn.relu(conv2d(l14, kernel,[1,1,1,1]) + biases, name=scope)

    with tf.name_scope('l16_conv2d_dw') as scope:
        kernel = weight_variable([3, 3, 512, 1])
        biases = bias_variable([1])
        l16 = tf.nn.relu(conv2d_dw(l15, kernel,[1,1,1,1]) + biases, name=scope)

    with tf.name_scope('l17_conv2d') as scope:
        kernel = weight_variable([1, 1, 512, 512])
        biases = bias_variable([512])
        l17 = tf.nn.relu(conv2d(l16, kernel,[1,1,1,1]) + biases, name=scope)

    with tf.name_scope('l18_conv2d_dw') as scope:
        kernel = weight_variable([3, 3, 512, 1])
        biases = bias_variable([1])
        l18 = tf.nn.relu(conv2d_dw(l17, kernel,[1,1,1,1]) + biases, name=scope)

    with tf.name_scope('l19_conv2d') as scope:
        kernel = weight_variable([1, 1, 512, 512])
        biases = bias_variable([512])
        l19 = tf.nn.relu(conv2d(l18, kernel,[1,1,1,1]) + biases, name=scope)

    with tf.name_scope('l20_conv2d_dw') as scope:
        kernel = weight_variable([3, 3, 512, 1])
        biases = bias_variable([1])
        l20 = tf.nn.relu(conv2d_dw(l19, kernel,[1,1,1,1]) + biases, name=scope)

    with tf.name_scope('l21_conv2d') as scope:
        kernel = weight_variable([1, 1, 512, 512])
        biases = bias_variable([512])
        l21 = tf.nn.relu(conv2d(l20, kernel,[1,1,1,1]) + biases, name=scope)

    with tf.name_scope('l22_conv2d_dw') as scope:
        kernel = weight_variable([3, 3, 512, 1])
        biases = bias_variable([1])
        l22 = tf.nn.relu(conv2d_dw(l21, kernel,[1,1,1,1]) + biases, name=scope)

    with tf.name_scope('l23_conv2d') as scope:
        kernel = weight_variable([1, 1, 512, 512])
        biases = bias_variable([512])
        l23 = tf.nn.relu(conv2d(l22, kernel,[1,1,1,1]) + biases, name=scope)
'''