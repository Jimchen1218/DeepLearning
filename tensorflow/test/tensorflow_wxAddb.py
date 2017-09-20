'''
name:tensorflow_wxaddb.py
create_date:8/29/2017
author:jimchen1218@sina.com
'''
			
			
import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt


print (__doc__)



# Parameters
learning_rate = 0.8
training_epochs = 100
display_step = 20

# Training Data
train_X = np.asarray([1,0,1,1])
train_Y = np.asarray([1])
n_samples = train_X.shape[0]

# tf Graph Input
X = tf.placeholder("float")
Y = tf.placeholder("float")

# Set model weights
W11= [.5,-.2,.8,.6]
W12=[.2,.3,.-.6,.5]
W13=[-.5,.4,.4,-.1]
W21=[.6,-.2,.1]

b11=[.2]
b12=[-.5]
b13=[.4]
b21=[.6]


# Construct a linear model
pred = tf.add(tf.multiply(X, W), b)
# Mean squared error
cost = tf.reduce_sum(tf.pow(pred-Y, 2))/(2*n_samples)
# Gradient descent
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(cost)

# Initializing the variables
init = tf.initialize_all_variables()

# Launch the graph
with tf.Session() as sess:
    sess.run(init)
    # Fit all training data
    for epoch in range(training_epochs):
        for (x, y) in zip(train_X, train_Y):
            sess.run(optimizer, feed_dict={X: x, Y: y})

        # Display logs per epoch step
        if (epoch+1) % display_step == 0:
            c = sess.run(cost, feed_dict={X: train_X, Y:train_Y})
            print("Epoch:", '%4d' % (epoch+1), "cost:", "{:.5f}".format(c), "W:", "{:.3f}".format(sess.run(W)), "b:", "{:.3f}".format(sess.run(b)))

    print("Optimization Finished!")
    training_cost = sess.run(cost, feed_dict={X: train_X, Y: train_Y})
    print("Training cost:", training_cost, "W=", sess.run(W), "b=", sess.run(b), '\n')			
			
			
			
			
'''
Method1:Linear model

	EPOCH_TIMES = 1000
	LEARNING_RATE=0.5
	
	x=tf.constant([])
	y_=tf.constant([1])
	
	w=tf.Variable([])
	b=tf.Variable([])
	
	y=tf.add(tf.matmul(w,x)+b)

	loss = tf.nn.softmax_cross_entropy_with_logits(y)
	optimizer = tf.train.GradientDescentOptimizer(LEARNING_RATE).minimize(loss)
	
	with tf.Session(graph=graph) as session:
		tf.initialize_all_variables().run()
		for step in range(EPOCH_TIMES):
			_, l, predictions = session.run([optimizer, loss, train_prediction])
			
	for i in range(layer_cnt - 2):
 y1 = tf.matmul(hidden_drop, weights[i]) + biases[i]
 hidden_drop = tf.nn.relu(y1)
 if drop_out:
     keep_prob += 0.5 * i / (layer_cnt + 1)
     hidden_drop = tf.nn.dropout(hidden_drop, keep_prob)		
'''			
			
			
			
			