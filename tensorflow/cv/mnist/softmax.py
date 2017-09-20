'''
title:softmax_regression.py
create date:5/7/2017
email:jimchen1218@sina.com
accuracy:92%
'''

print(__doc__)

from tensorflow.examples.tutorials.mnist import input_data

import tensorflow as tf
import logging
import time
import argparse
import sys
import tempfile

tf.logging.set_verbosity(tf.logging.ERROR)

mnist=input_data.read_data_sets("MNIST_data/",one_hot=True)


in_units=784
out_units=10
epochs=10000
batch_size=100
LEARNING_RATE = 0.08

log_dir='/tmp/mnist/logs/mnist_with_summaries'

def variable_summaries(var):
  with tf.name_scope('summaries'):
    mean = tf.reduce_mean(var)
    tf.summary.scalar('mean', mean)
    with tf.name_scope('stddev'):
      stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
    tf.summary.scalar('stddev', stddev)
    tf.summary.scalar('max', tf.reduce_max(var))
    tf.summary.scalar('min', tf.reduce_min(var))
    #tf.summary.histogram('histogram', var)


def weight_bias_variable(input,out):
		with tf.name_scope('weight'):
				w=tf.Variable(tf.zeros([input,out]))
		with tf.name_scope('bias'): 		
				b=tf.Variable(tf.zeros([out]))
		return w,b

def input_layer(input,output):
		with tf.name_scope('input'):
				x=tf.placeholder(tf.float32,[None,input])
				y_=tf.placeholder(tf.float32,[None,output])
		return x,y_

def nn_layer(x,w,b):
		with tf.name_scope('softmax'): 
				y=tf.nn.softmax(tf.matmul(x,w)+b)
		return y
		
def compute_cost(pred_y,true_y,learning_rate):
		with tf.name_scope('cost'):
				cost=tf.reduce_mean(-tf.reduce_sum(true_y*tf.log(pred_y),reduction_indices=[1]))
		with tf.name_scope('optimizer'): 
				opt=tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)
		tf.summary.scalar('cost', cost)
		return cost,opt

def compute_accuracy(pred_y,true_y):
		with tf.name_scope('correct_prediction'):
				correct_prediction=tf.equal(tf.argmax(pred_y,1),tf.argmax(true_y,1))
		with tf.name_scope('accuracy'):
				accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
		tf.summary.scalar('accuracy', accuracy)
		return accuracy

def softmax_model(x,true_y,input,output):
		with tf.name_scope('weights'):
				weight,bias = weight_bias_variable(input,output)
				variable_summaries(weight)
				variable_summaries(bias)
		pred_y = nn_layer(x,weight,bias)
		cost,opt = compute_cost(pred_y,true_y,LEARNING_RATE)
		accuracy = compute_accuracy(pred_y,true_y)
		return cost,opt,accuracy
	
def main(_):
		t0=time.time()
		sess=tf.InteractiveSession()
		merged=tf.summary.merge_all()
		x,y_ = input_layer(in_units,out_units)
		cost,opt,acc = softmax_model(x,y_,in_units,out_units)
		tf.global_variables_initializer().run()
		print("log dir path is :%s"%(log_dir))
		train_writer = tf.summary.FileWriter(log_dir + '/train', sess.graph)
		#test_writer = tf.summary.FileWriter(log_dir + '/test', sess.graph)
		for i in range(epochs):
				batch_xs,batch_ys=mnist.train.next_batch(batch_size)
				accuracy,_,cost_val = sess.run([acc,opt,cost],feed_dict = {x:batch_xs,y_:batch_ys})
				#train_writer.add_summary(summary,i)
				if i % batch_size == 0:
						print("train i:%d \ncost:%s\naccuracy:%s"%(i,cost_val,accuracy))

		print("Total train used time:%f"%(time.time()-t0))
		_,accuracy = sess.run([opt,acc],feed_dict={x:mnist.test.images,y_:mnist.test.labels})
		print("The accuracy percent:%s"%accuracy)
		train_writer.close()

if __name__ == "__main__":
		parser = argparse.ArgumentParser()
		parser.register("type", "bool", lambda v: v.lower() == "true")
		parser.add_argument(
				"--learning_rate",
				type=float,
				default=LEARNING_RATE,
				help="Initial learning rate.")
		FLAGS, unparsed = parser.parse_known_args()
		tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)

