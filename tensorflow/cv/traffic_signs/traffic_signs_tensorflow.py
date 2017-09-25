'''
Traffic Sign Recognition with Tensorflow
The goal is to build a model that can detect and classify traffic signs in a video stream taken from a moving car.
'''

import os
import random
import skimage.data
import skimage.transform
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf
import time

print (__doc__)


def load_datasets(data_dir):
    directories = [d for d in os.listdir(data_dir) if os.path.isdir(os.path.join(data_dir, d))]
    #print("load_datasets directories:%s"%(directories))
    images = []
    labels = []
    for d in directories:
        label_dir = os.path.join(data_dir, d)
        file_names = [os.path.join(label_dir, f) for f in os.listdir(label_dir) if f.endswith(".ppm")]
        for f in file_names:
            images.append(skimage.data.imread(f))
            labels.append(int(d))
    return images, labels

def display_images_and_labels(images, labels):
    unique_labels = set(labels)
    plt.figure(figsize=(15, 15))
    i = 1
    for label in unique_labels:
        image = images[labels.index(label)]
        plt.subplot(8, 8, i)
        plt.axis('off')
        plt.title("Label {0} ({1})".format(label, labels.count(label)))
        i += 1
        _ = plt.imshow(image)
    #plt.show()

#display_images_and_labels(images, labels)


def display_label_images(images, label):
    limit = 24  # show a max of 24 images
    plt.figure(figsize=(15, 5))
    i = 1
    start = labels.index(label)
    end = start + labels.count(label)
    for image in images[start:end][:limit]:
        plt.subplot(3, 8, i)  # 3 rows, 8 per row
        plt.axis('off')
        i += 1
        plt.imshow(image)
    #plt.show()


#main code start here
time_start=time.time()
# Load training and testing datasets.
ROOT_PATH = "traffic_signs"
train_data_dir = os.path.join(ROOT_PATH,"datasets/BelgiumTS/Training")
test_data_dir = os.path.join(ROOT_PATH,"datasets/BelgiumTS/Testing")
images, labels = load_datasets(train_data_dir)
print("number of images:%d"%(len(images)))
display_label_images(images, 32)

for image in images[:5]:
    print("shape: {0}, min: {1}, max: {2}".format(image.shape, image.min(), image.max()))
    images32 = [skimage.transform.resize(image, (32, 32)) for image in images]
    display_images_and_labels(images32, labels)
    for image in images32[:5]:
        print("shape: {0}, min: {1}, max: {2}".format(image.shape, image.min(), image.max()))


# Minimum Viable Model
labels_a = np.array(labels)
images_a = np.array(images32)
print("labels:", labels_a.shape,"\nimages:", images_a.shape)

# Create a graph to hold the model.
graph = tf.Graph()
with graph.as_default():
    images_ph = tf.placeholder(tf.float32, [None, 32, 32, 3])
    labels_ph = tf.placeholder(tf.int32, [None])
    images_flat = tf.contrib.layers.flatten(images_ph)
    logits = tf.contrib.layers.fully_connected(images_flat, 62, tf.nn.relu)
    predicted_labels = tf.argmax(logits, 1)
    loss = tf.reduce_mean(tf.nn.sparse_softmax_cross_entropy_with_logits(labels=labels_ph,logits=logits))
    train = tf.train.AdamOptimizer(learning_rate=0.001).minimize(loss)
    init = tf.global_variables_initializer()
    print("images_flat:", images_flat)
    print("logits:", logits)
    print("loss:", loss)
    print("predicted_labels:",predicted_labels)

session = tf.Session(graph=graph)
_ = session.run([init])
for i in range(201):
    _, loss_value = session.run([train, loss],feed_dict={images_ph: images_a, labels_ph: labels_a})
    if i % 10 == 0:
        print("Loss:", loss_value)
    
# Pick 10 random images
sample_indexes = random.sample(range(len(images32)), 10)
sample_images = [images32[i] for i in sample_indexes]
sample_labels = [labels[i] for i in sample_indexes]
predicted = session.run([predicted_labels],feed_dict={images_ph: sample_images})[0]
print(sample_labels)
print(predicted)

# Display the predictions and the ground truth visually.
fig = plt.figure(figsize=(10, 10))
for i in range(len(sample_images)):
    truth = sample_labels[i]
    prediction = predicted[i]
    plt.subplot(5, 2,1+i)
    plt.axis('off')
    color='green' if truth == prediction else 'red'
    plt.text(40, 10,"Truth:{0} Prediction: {1}".format(truth, prediction),fontsize=12, color=color)
    plt.imshow(sample_images[i])
plt.show()
    
# Load the test dataset.
test_images, test_labels = load_datasets(test_data_dir)
test_images32 = [skimage.transform.resize(image, (32, 32)) for image in test_images]
display_images_and_labels(test_images32, test_labels)


# Run predictions against the full test set.
predicted = session.run([predicted_labels],feed_dict={images_ph: test_images32})[0]
match_count = sum([int(y == y_) for y, y_ in zip(test_labels, predicted)])
test_len = len(test_labels)
accuracy = match_count / test_len


time_duration=time.time()-time_start

print("match_count: {:.3f}".format(match_count),"test_len: {:.3f}".format(test_len))
print("Accuracy: {:.3f}".format(accuracy))
print("time_duration: {:.5f}s".format(time_duration))
session.close()


















