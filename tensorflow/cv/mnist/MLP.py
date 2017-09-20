'''
name:MLP.py
created date:5/11/2017
modified date:9/13/2017 reconstructure code
email:jimchen1218@sina.com
predict accuracy:98%
'''

from tensorflow.examples.tutorials.mnist import input_data
import tensorflow as tf
import time
import argparse
import sys
import tempfile


print(__doc__)

mnist=input_data.read_data_sets("MNIST_data/",one_hot=True)
path_mnist = "MNIST_data/"

in_units=784
h1_units=300
out_units=10

EPOCH_SIZE=10000
batch_size=50
LEARNING_RATE = 0.05

def weight_variable(input,hide,output):
		w1=tf.Variable(tf.truncated_normal([input,hide],stddev=.1))
		w2=tf.Variable(tf.zeros([hide,output]))
		return w1,w2

def bias_variable(hide,output):
		b1=tf.Variable(tf.zeros([hide]))
		b2=tf.Variable(tf.zeros([output]))
		return b1,b2

def input_layer(input,output):
		x=tf.placeholder(tf.float32,[None,input])
		keep_prob=tf.placeholder(tf.float32)
		y_=tf.placeholder(tf.float32,[None,output])
		return x,y_,keep_prob
		
def nn_layer(x,w1,b1,w2,b2,keep_prob):
		hidden1=tf.nn.relu(tf.matmul(x,w1)+b1)
		#hidden1_drop=tf.nn.dropout(hidden1,keep_prob)
		y=tf.nn.softmax(tf.matmul(hidden1,w2)+b2)
		return y

def compute_cost(predict_y,true_y,learning_rate):
		cost=tf.reduce_mean(-tf.reduce_sum(true_y*tf.log(predict_y),reduction_indices=[1]))
		opt=tf.train.AdagradOptimizer(learning_rate).minimize(cost)
		return cost,opt
	
def compute_precision(predict_y,true_y):
		correct_prediction=tf.equal(tf.argmax(predict_y,1),tf.argmax(true_y,1))
		accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))
		return accuracy

def mlp_model(x,true_y,input,hide1,output,keep_prob):
		weight1,weight2 = weight_variable(input,hide1,output)
		bias1,bias2 = bias_variable(hide1,output)
		pred_y = nn_layer(x,weight1,bias1,weight2,bias2,keep_prob)
		cost,opt = compute_cost(pred_y,true_y,LEARNING_RATE)
		acc = compute_precision(pred_y,true_y)
		return cost,opt,acc

def main(_):
		sess=tf.InteractiveSession()
		x,y_,keep_prob = input_layer(in_units,out_units)
		cost,opt,acc = mlp_model(x,y_,in_units,h1_units,out_units,keep_prob)
		tf.global_variables_initializer().run()
		
		start_time=time.time()
		for i in range(EPOCH_SIZE):
				batch_xs,batch_ys=mnist.train.next_batch(batch_size)
				cost_val,_,accuracy= sess.run([cost,opt,acc],feed_dict = {x:batch_xs,y_:batch_ys,keep_prob:.75})
				if i % batch_size == 0:
						print("train i:%d \ncost_val:%s \naccuracy:%s"%(i,cost_val,accuracy))
		
		duration=time.time()-start_time
		print("MLP Total used time:%s"%(duration))
		
		print("The test accuracy :%s"%sess.run([acc],feed_dict = {x:mnist.test.images,y_:mnist.test.labels,keep_prob:1.0}))

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
				default=path_mnist,
				help="Directory for storing data")
		FLAGS, unparsed = parser.parse_known_args()
		tf.app.run(main=main, argv=[sys.argv[0]] + unparsed)