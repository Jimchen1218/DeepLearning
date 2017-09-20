'''
title:softmax_regression.py
source:Tensorflow practise
create date:5/7/2017
author czm
email:jimchen1218@sina.com
'''

print(__doc__)

from tensorflow.examples.tutorials.mnist import input_data
mnist=input_data.read_data_sets("MNIST_data/",one_hot=True)

print(mnist.train.images.shape,mnist.train.labels.shape)
print(mnist.test.images.shape,mnist.test.labels.shape)
print(mnist.validation.images.shape,mnist.validation.labels.shape)


import tensorflow as tf
import time

in_units=784
h1_units=10
epochs=6000
batch_size=100

t0=time.time()
sess=tf.InteractiveSession()
x=tf.placeholder(tf.float32,[None,in_units])

W=tf.Variable(tf.zeros([in_units,h1_units]))
b=tf.Variable(tf.zeros([h1_units]))

y=tf.nn.softmax(tf.matmul(x,W)+b)

y_=tf.placeholder(tf.float32,[None,h1_units])
cross_entropy=tf.reduce_mean(-tf.reduce_sum(y_*tf.log(y),reduction_indices=[1]))
train_step=tf.train.GradientDescentOptimizer(0.5).minimize(cross_entropy)

#tf.global_variables_initializer().run()
tf.initialize_all_variables().run()

for i in range(epochs):
    batch_xs,batch_ys=mnist.train.next_batch(batch_size)
    train_step.run({x:batch_xs,y_:batch_ys})
    
correct_prediction=tf.equal(tf.argmax(y,1),tf.argmax(y_,1))
accuracy=tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

print("Total used time:%f"%(time.time()-t0))
print("The accuracy percent:%s"%accuracy.eval({x:mnist.test.images,y_:mnist.test.labels}))
