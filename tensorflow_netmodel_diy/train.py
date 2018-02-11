'''
filename: train.py
createdate:2/8/2018
author:jim.chen
'''
import numpy as np
import tensorflow as tf
from tensorflow.python.framework import graph_util
import model

print(__doc__)

path = "picture//"
pb_file_path = "mobilenet.pb"
w = 224
h = 224
c = 3
EPOCH_TIMES = 23
BATCH_SIZE = 2

def train_mobilenet(graph, batch_size, num_epochs, pb_file_path,train_x,train_y):
    init = tf.global_variables_initializer()
    with tf.Session() as sess:
        sess.run(init)

        for i in range(EPOCH_TIMES):
            sess.run([graph['optimize']], feed_dict={
                graph['x']: np.reshape(train_x[i], (1, 224, 224, 3)),
                graph['y']: ([[1, 0]] if train_y[i] == 0 else [[0, 1]])
            })
            if i % batch_size == 0:
                total_batches_in_train_set = 0
                total_correct_times_in_train_set = 0
                total_cost_in_train_set = 0.
                correct_times_in_batch = sess.run(graph['correct_times_in_batch'], feed_dict={
                    graph['x']: np.reshape(train_x[i], (1, 224, 224, 3)),
                    graph['y']: ([[1, 0]] if train_y[i] == 0 else [[0, 1]])
                })
                cost = sess.run(graph['cost'], feed_dict={
                    graph['x']: np.reshape(train_x[i], (1, 224, 224, 3)),
                    graph['y']: ([[1, 0]] if train_y[i] == 0 else [[0, 1]])
                })
                acc = sess.run(graph['accuracy'], feed_dict={
                    graph['x']: np.reshape(train_x[i], (1, 224, 224, 3)),
                    graph['y']: ([[1, 0]] if train_y[i] == 0 else [[0, 1]])
                })   
                total_batches_in_train_set += 1
                total_correct_times_in_train_set += correct_times_in_batch
                total_cost_in_train_set += (cost * batch_size)

                #acc_train = total_correct_times_in_train_set / float(total_batches_in_train_set * batch_size)
                print('Epoch-{:2d}, train accuracy:{:6.2f},train cost:{:4.1f} '.format(i, acc*100.0,cost))
                
            constant_graph = graph_util.convert_variables_to_constants(sess, sess.graph_def, ["output"])
            with tf.gfile.FastGFile(pb_file_path, mode='wb') as f:
                f.write(constant_graph.SerializeToString())


def main():
    train_x,train_y,val_x,val_y = model.build_datasets(path,height=224, width=224, channel=3)
    g = model.build_mobilenet(height=224, width=224, channel=3)
    train_mobilenet(g, BATCH_SIZE, EPOCH_TIMES, pb_file_path,train_x,train_y)

if __name__ == "__main__":
	main()	



