# -*- coding: utf-8 -*-
"""pokemon-transfer-learning.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1eKksoazP7N7TSP2vm4qzv9Ccl00kkmLA
"""

import matplotlib.pyplot as plt
import numpy as np
import PIL
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Dense, Flatten, Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

from google.colab import drive
drive.mount('/content/drive')

data_dir = '/content/drive/MyDrive/PokemonData'

"""Set variables to reformat img heights and width and set batch size."""

img_height,img_width=300,300
batch_size=32

"""Create a training dataset with 80% of the data"""

train_ds = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="training",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

"""Create a validation dataset with 20% of the data"""

val_ds = tf.keras.preprocessing.image_dataset_from_directory(
  data_dir,
  validation_split=0.2,
  subset="validation",
  seed=123,
  image_size=(img_height, img_width),
  batch_size=batch_size)

"""import pretrained model and output layer (where learning will take place)"""

resnet_model = Sequential()

pretrained_model= tf.keras.applications.ResNet50(include_top=False,
                   input_shape=(300,300,3),
                   pooling='avg',classes=150,
                   weights='imagenet')
for layer in pretrained_model.layers:
        layer.trainable=False

resnet_model.add(pretrained_model)

resnet_model.add(Flatten())
resnet_model.add(Dense(512, activation='relu'))
resnet_model.add(Dense(150, activation='softmax'))
resnet_model.summary()

resnet_model.compile(optimizer=Adam(lr=0.001),loss='sparse_categorical_crossentropy',metrics=['accuracy'])

history = resnet_model.fit(train_ds, validation_data=val_ds, epochs=10)
model.save(os.path.join('/results/models','pokemonclassifier.h5'))