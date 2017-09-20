'''
run success in tensorflow 1.2.1

'''

import numpy as np
import tensorflow as tf

import matplotlib as mpl
import matplotlib.pyplot as plt

from tensorflow.contrib.learn.python.learn.estimators import estimator
from tensorflow.contrib.learn.python.learn.estimators import _sklearn
from tensorflow.contrib.metrics.python.ops import metric_ops

mpl.use('Agg')

learn=tf.contrib.learn

HIDDEN_SIZE=30
NUMBER_LAYERS=1

TIMESTEPS=10
TRAINING_STEPS=10000
BATCH_SIZE=32

TRAINING_EXAMPLES=10000
TESTING_EXAMPLES=1000
SAMPLE_GAP=0.01

tf.logging.set_verbosity(tf.logging.INFO)

import tempfile
tempdir = tempfile.mkdtemp()

graph=tf.Graph()

def generate_data(seq):
    X=[]
    y=[]
    for i in range(len(seq)-TIMESTEPS-1):
        X.append([seq[i:i+TIMESTEPS]])
        y.append([seq[i+TIMESTEPS]])
    return np.array(X,dtype=np.float32),np.array(y,dtype=np.float32)

def lstm_model(X,y):
    lstm_cell=tf.contrib.rnn.BasicLSTMCell(HIDDEN_SIZE)
    cell=tf.contrib.rnn.MultiRNNCell([lstm_cell]*NUMBER_LAYERS)
    x_=tf.unstack(X,axis=1)
    output,_=tf.nn.static_rnn(cell,x_,dtype=tf.float32,sequence_length=None,initial_state=None)
    output=output[-1]
    prediction,loss=learn.models.linear_regression(output,y)
    train_op=tf.contrib.layers.optimize_loss(loss,tf.contrib.framework.get_global_step(),optimizer="Adagrad",learning_rate=0.1)
    return prediction,loss,train_op



test_start=TRAINING_EXAMPLES*SAMPLE_GAP
test_end=(TRAINING_EXAMPLES+TESTING_EXAMPLES)*SAMPLE_GAP
train_X,train_y=generate_data(np.sin(np.linspace(0,test_start,TRAINING_EXAMPLES,dtype=np.float32)))
test_X,test_y=generate_data(np.sin(np.linspace(test_start,test_end,TESTING_EXAMPLES,dtype=np.float32)))

estimator=estimator.Estimator(model_fn=lstm_model)
estimator.fit(x=train_X,y=train_y,steps=TRAINING_STEPS)
scores = estimator.evaluate(x=test_X,y=test_y,metrics={'MSE': metric_ops.streaming_mean_squared_error})
predictions = np.array(list(estimator.predict(x=test_X)))

merged_summaries=tf.merge_all_summaries()


print("tempdir path is :%s"%(tempdir))
writer=tf.summary.FileWriter(tempdir,graph)
writer.close()

sess=tf.Session(graph=graph)
with graph.as_default():
    with tf.name_scope('MSE'):
        mse_score = _sklearn.mean_squared_error(predictions, test_y)
        tf.scaler_summary(b"mse",mse_score,name="mse score")

print("mean square error is :%s"%(mse_score))

fig=plt.figure()
plot_predicted=plt.plot(predictions,label='predicted')
plot_test=plt.plot(test_y,label="real_sin")
plt.legend([plot_predicted,plot_test],['predicted','real_sin'])
plt.show()
fig.savefig("sin.png")






#def main(unused_argv):


#if __name__ == "__main__":
#  tf.app.run()
