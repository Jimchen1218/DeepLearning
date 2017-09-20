'''
Name:queue.py
Create date:8/17/2017
Author:Jim<jimchen1218@sina.com>
'''

print(__doc__)

import tensorflow as tf


def FIFOQueue():
	q=tf.FIFOQueue(3,"float")
	init=q.enqueue_many(([0.1,0.2,0.3],))
	
	x=q.dequeue()
	y=x+1
	q_inc=q.enqueue(y)
	
	with tf.Session() as sess:
		sess.run(init)
		quelen=sess.run(q.size())
		for i in range(3):
			sess.run(q_inc)
		quelen=sess.run(q.size())
		for i in range(quelen):
			print (sess.run(q.dequeue()))

def RandomShuffleQueue():
	q=tf.RandomShuffleQueue(capacity=10,min_after_dequeue=2,dtypes="float")

	with tf.Session() as sess:
		for i in range(0,10):
			sess.run(q.enqueue(i))
		
		for i in range(0,8):
			run_options=tf.RunOptions(timeout_in_ms=5000)
			try:				
				print(sess.run(q.dequeue(),options=run_options))
			except tf.errors.DeadlineExceededError:
				print('out of range')


def QueueRunner():
'''
all QueueRunner in tf.GraphKeys.QUEUE_RUNNERS collections
'''
	q=tf.FIFOQueue(10,"float")
	counter=tf.Variable(0.0)
	increment_op=tf.assign_add(counter,tf.constant(1.0))
	enqueue_op=q.enqueue(counter)
	qr=tf.train.QueueRunner(q,enqueue_ops=[increment_op,enqueue_op])
	
	with tf.Session() as sess:
		sess.run(tf.global_variables_initializer())
		#sess.run(tf.initialize_all_variables())
		coord=tf.train.Coordinator()
		enqueue_threads=qr.create_threads(sess,coord=coord,start=True)

		coord.request_stop()
		for i in range(10):
			try:
				print (sess.run(q.dequeue()))
			except tf.errors.OutOfRangeError:
				break
		coord.join(enqueue_threads)


#to do here
#FIFOQueue()
#RandomShuffleQueue()
QueueRunner()







