'''
name:test_cnn_mnist_tensorboard_argparse.py
create_date:9/12/2017
author:jimchen1218@sina.com
'''
			

import tensorflow as tf

from tensorflow.examples.tutorials.mnist import input_data
import argparse
import sys
import tempfile


print (__doc__)


IMAGE_SIZE = 28
HIDDEN_SIZE = 500
NUM_LABELS = 10
RAND_SEED = 42
EPOCH_SIZE = 2000
BATCH_SIZE = 100
LEARNING_RATE = 0.01

tf.logging.set_verbosity(tf.logging.INFO)

# Import data
path_mnist="/tmp/mnist_data"

def variable_summaries(var):
  """Attach a lot of summaries to a Tensor (for TensorBoard visualization)."""
  with tf.name_scope('summaries'):
    mean = tf.reduce_mean(var)
    tf.summary.scalar('mean', mean)
    with tf.name_scope('stddev'):
      stddev = tf.sqrt(tf.reduce_mean(tf.square(var - mean)))
    tf.summary.scalar('stddev', stddev)
    tf.summary.scalar('max', tf.reduce_max(var))
    tf.summary.scalar('min', tf.reduce_min(var))
    #tf.summary.histogram('histogram', var)

def weight_variable(shape):
    initial = tf.truncated_normal(shape, stddev=0.1, seed=RAND_SEED)
    return tf.Variable(initial)

def bias_variable(shape):
    initial = tf.constant(0.1, shape=shape)
    return tf.Variable(initial)

def feed_dict(train):
  if train:
    xs, ys = mnist.train.next_batch(BATCH_SIZE, fake_data=False)
    k = 0.5
  else:
    xs, ys = mnist.test.images, mnist.test.labels
    k = 1.0
  return {x: xs, y_: ys, keep_prob: k}

def input_layer(layer_name):
    with tf.name_scope(layer_name):
        x = tf.placeholder(tf.float32, [None, IMAGE_SIZE**2], name="x-input")
        y_ = tf.placeholder(tf.float32, [None, NUM_LABELS], name="y-input")
        keep_prob = tf.placeholder(tf.float32)
    return x,y_,keep_prob

def dropout_layer(layer_name,hidden_layer,keep_prob):
    with tf.name_scope(layer_name):
        tf.summary.scalar('dropout_keep_probability', keep_prob)
        dropped = tf.nn.dropout(hidden_layer, keep_prob)
    return dropped

def nn_layer(input_tensor, input_dim, output_dim, layer_name, act=tf.nn.relu):
  with tf.name_scope(layer_name):
    with tf.name_scope('weights'):
      weights = weight_variable([input_dim, output_dim])
      variable_summaries(weights)
    with tf.name_scope('biases'):
      biases = bias_variable([output_dim])
      variable_summaries(biases)
    with tf.name_scope('Wx_plus_b'):
      preactivate = tf.matmul(input_tensor, weights) + biases
      #tf.summary.histogram('pre_activations', preactivate)
    activations = act(preactivate, name='activation')
    #tf.summary.histogram('activations', activations)
    return activations

def fc_layer(act):
    y = tf.nn.softmax(act)
    return y

def count_cross_entropy(x,y):
    with tf.name_scope('cross_entropy'):
    #diff = tf.nn.softmax_cross_entropy_with_logits(labels=y_, logits=y)
        diff = -(x * tf.log(y))
        with tf.name_scope('total'):
            cross_entropy = tf.reduce_mean(diff)
    tf.summary.scalar('cross_entropy', cross_entropy)
    return cross_entropy

def train_optimizer(cross_entropy):
    with tf.name_scope('train'):
        train_opt = tf.train.AdamOptimizer(LEARNING_RATE).minimize(cross_entropy)
    return train_opt

def correct_prediction(x,y):
    with tf.name_scope('accuracy'):
        with tf.name_scope('correct_prediction'):
            correct_prediction = tf.equal(tf.argmax(x, 1), tf.argmax(y, 1))
    with tf.name_scope('accuracy'):
        accuracy = tf.reduce_mean(tf.cast(correct_prediction, tf.float32))
    tf.summary.scalar('accuracy', accuracy)
    return accuracy

def cnn_model(input_x,input_y,input_size,output_size,keep_prob):
    hidden_layer1 = nn_layer(input_x, input_size, HIDDEN_SIZE, "hidden_layer1")
    dropped =dropout_layer("dropout",hidden_layer1,keep_prob)
    hidden_layer2 = nn_layer(dropped, HIDDEN_SIZE, output_size, 'hidden_layer2', act=tf.identity)
    y = fc_layer(hidden_layer2)
    cross_entropy = count_cross_entropy(input_y,y)
    train_opt = train_optimizer(cross_entropy)
    accuracy = correct_prediction(y,input_y)
    return accuracy

def main(_):
    sess = tf.InteractiveSession()
    tempdir = tempfile.mkdtemp()
    x,y_,keep_prob = input_layer("input_layer")
    mnist = input_data.read_data_sets(path_mnist,one_hot=True,fake_data=False)
    accuracy = cnn_model(x,y_,IMAGE_SIZE**2,NUM_LABELS,keep_prob)

    merged = tf.summary.merge_all()
    print("tempdir path is :%s"%(tempdir))
    train_writer = tf.summary.FileWriter(tempdir + '/train',sess.graph)
    test_writer = tf.summary.FileWriter(tempdir + '/test')

    tf.global_variables_initializer().run()
    for i in range(FLAGS.max_steps):
        if i % BATCH_SIZE == 0:    
            summary, acc = sess.run([merged, accuracy], feed_dict=feed_dict(False))
            test_writer.add_summary(summary, i)
            print('Accuracy at step %s: %s' % (i, acc))
        else:
            summary, _ = sess.run([merged, train_opt], feed_dict=feed_dict(True))
            train_writer.add_summary(summary, i)


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


