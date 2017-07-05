# -*- coding: utf-8 -*-
"""
Created on Tue Mar 21 17:09:58 2017

@author: iLenovo
"""

import numpy as np
import tensorflow as tf
import pandas as pt
import matplotlib.pyplot as plt

def readfile(string):
    file = open(string)
    lines = file.readlines()
    line = 1
    data2 = []
    for l in lines:
        inputdata = l.split(' ')
        inputdata = inputdata[0:len(inputdata)-1]
        data2.append( [float(x) for x in inputdata])
        line = line+1
    return data2

inputdata = readfile('SC_DJI_PHANTOM_SET_ONE')
x = []
y = []
for i in inputdata: 
    x.append(i[1:len(i)])
    y.append(i[0])

y = np.array(y)
#print (len(y) , len(x) , len(x[0]) , x[0]  , x.shape , y) 
print("input is read from the given file and assigned to x , y")

train_size = 100000
validation_size = 50000
test_size = 50000

sess = tf.InteractiveSession()
mean = tf.reduce_mean(x,0)
covariance = tf.placeholder('float', [90 ,90])
print(covariance)
plt.plot(x)
computed_x = x - mean
print(computed_x.eval())

sess.close()
