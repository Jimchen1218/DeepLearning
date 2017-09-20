'''
nn type:softmax regression
name:linearregression_softmax_mnist.py
author:jimchen
date:8/12/2017
'''

print(__doc__)

import tensorflow as tf
import tensorflow.examples.tutorials.mnist.input_data as input_data
import logging
import time

tf.logging.set_verbosity(tf.logging.ERROR)

in_units=784
out_units=10
learning_rate=0.01
epoch_num=10000
batch_num=50

data_dir='/tmp/mnist/input_data'
log_dir='/tmp/mnist/logs/mnist_with_summaries'

time_begin=time.time()
mnist = input_data.read_data_sets(data_dir, one_hot=True)
time_duration = time.time() - time_begin
print ("jim download dataset time:%ss" % time_duration)


def variable_summaries(var):
    with tf.name_scope('summaries'):
        mean=tf.reduce_mean(var)
        tf.summary.scalar('mean',mean)
        with tf.name_scope('stddev'):
            stddev=tf.sqrt(tf.reduce_mean(tf.square(var-mean)))
        tf.summary.scalar('stddev',stddev)
        tf.summary.scalar('max',tf.reduce_max(var))
        tf.summary.histogram('histogram',var)
        


with tf.name_scope('input'):
    x = tf.placeholder(tf.float32, shape=[None, in_units],name='x-input')
    y = tf.placeholder(tf.float32, shape=[None, out_units],name='y-input')
with tf.name_scope('weight'):
    W = tf.Variable(tf.zeros([in_units,out_units]))
with tf.name_scope('bias'):    
    b = tf.Variable(tf.zeros([out_units]))
with tf.name_scope('softmax'): 
    y_ = tf.nn.softmax(tf.matmul(x,W) + b)

with tf.name_scope('cross_entropy'): 
    cross_entropy = tf.reduce_mean(-tf.reduce_sum(y*tf.log(y_),reduction_indices=1))
with tf.name_scope('train_step'):    
    train_step = tf.train.GradientDescentOptimizer(learning_rate).minimize(cross_entropy)
with tf.name_scope('correct_prediction'):
    correct_prediction = tf.equal(tf.argmax(y_,1), tf.argmax(y,1))
with tf.name_scope('accuracy'):        
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))


merged=tf.merge_all_summaries()

time_begin=time.time()
init = tf.initialize_all_variables()
with tf.Session() as sess:
    train_writer = tf.train.SummaryWriter(log_dir + '/train', sess.graph)
    test_writer = tf.train.SummaryWriter(log_dir + '/test', sess.graph)
    sess.run(init)
    for i in range(epoch_num):
        batch_xs, batch_ys = mnist.train.next_batch(batch_num)
        sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})
        train_writer.add_summary(merged,i)
        if(i%batch_num==0):
            print "jim test accuracy:",sess.run(accuracy, feed_dict={x: mnist.test.images, y: mnist.test.labels})
            test_writer.add_summary(merged,i)
    time_duration=time.time()-time_begin
    print ("jim time_duration:%ss"%time_duration)
    
train_writer.close()
test_writer.close()

