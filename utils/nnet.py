#!/usr/bin/env python
# coding: utf-8

import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers import Input, Add, Dense, Average, Activation, BatchNormalization, Flatten, Conv3D, AveragePooling3D, MaxPooling3D, GlobalMaxPooling3D, Dropout, Concatenate
from tensorflow.keras.models import Model, load_model
from tensorflow.keras.initializers import random_uniform, glorot_uniform, constant, identity
from tensorflow.python.keras.utils.vis_utils import plot_model
import numpy as np

#3d CNN
def cnn_model(x):
    
    inputs = x
    x = tf.keras.layers.Conv2D(16, kernel_size = (3, 3),activation = 'relu')(inputs)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.MaxPool2D(pool_size = (2, 2))(x)
    
    x = tf.keras.layers.Conv2D(32, kernel_size = (3, 3), activation = 'relu')(x)
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.MaxPool2D(pool_size = (2, 2))(x)
    
    x = tf.keras.layers.Conv2D(64, kernel_size = (6, 6), activation = 'relu')(x) 
    x = tf.keras.layers.BatchNormalization()(x)
    x = tf.keras.layers.MaxPool2D(pool_size = (2, 2))(x)

    return x

#input
input_samp = np.zeros([16, 224, 224, 3])

#input
input = Input(input_samp[0, :].shape, name = 'video')
out = cnn_model(input)
out = Flatten()(out)
out = Dropout(0.5)(out)
out = Dense(1024, activation = 'relu')(out)
out = Dense(128, activation = 'relu')(out)
output = Dense(1, activation = 'sigmoid', name = 'class')(out)

#create the model
video_cnn_model = Model(input, output)



