'''
Traffic Sign Recognition with Tensorflow
The goal is to build a model that can detect and classify traffic signs in a video stream taken from a moving car.
'''

import numpy as np
import tensorflow as tf

import matplotlib.pyplot as plt

import matplotlib as mpl

mpl.use('Agg')

print (__doc__)

learn=tf.contrib.learn

HIDDEN_SIZE=30
NUMBER_LAYERS=2

TIMESTEPS=10
TRAINING_STEPS=10000
BATCH_SIZE=32

TRAINING_EXAMPLES=10000
TESTING_EXAMPLES=1000
SAMPLE_GAP=0.01










print("match_count: {:.3f}".format(match_count),"test_len: {:.3f}".format(test_len))
print("Accuracy: {:.3f}".format(accuracy))
print("time_duration: {:.5f}s".format(time_duration))
session.close()


















