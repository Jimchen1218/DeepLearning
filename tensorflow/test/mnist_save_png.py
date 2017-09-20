'''
name:mnist_save_png.py
create_date:9/19/2017
author:jimchen1218@sina.com
'''

from PIL import Image

import tflearn.datasets.mnist as mnist

print(__doc__)

X, Y, testX, testY = mnist.load_data(one_hot=True)
X = X.reshape([-1, 28, 28, 1])

testX = testX.reshape([-1, 28, 28, 1])
test_x_0 = testX[1].reshape([28, 28])

img = Image.new('L', (28, 28))
for i in range(28):
    for j in range(28):
        img.putpixel((i, j), 255 - int(test_x_0[j][i] * 255.0))

img.save('test_save.png')