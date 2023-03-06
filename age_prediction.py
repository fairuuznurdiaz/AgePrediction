# -*- coding: utf-8 -*-
"""Age Prediction

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1us0t8zMijnkNueUBykyPdqTIl3CqPbud
"""

from google.colab import drive

drive.mount('/content/drive')

# Replace with your path!
!unzip -q /content/drive/MyDrive/DataDataBDC/DataBDC.zip -d data

# # 
# !mv data/DataBDC data/DataBDC

# To download checkpoints, Keras models, TFLite models
from google.colab import files

# Life is incomplete without this statement!
import tensorflow as tf

# And this as well!
import numpy as np

# To visualize results
import matplotlib.pyplot as plt

import os
import datetime

# Image size for our model.
MODEL_INPUT_IMAGE_SIZE = [ 200 , 200 ]

# Fraction of the dataset to be used for testing.
TRAIN_TEST_SPLIT = 0.3

# Number of samples to take from dataset
N = 20000

# This method will be mapped for each filename in `list_ds`. 
def parse_image(  ):

    # Read the image from the filename and resize it.
    image_raw = tf.io.read_file( filename )
    image = tf.image.decode_jpeg( image_raw , channels=3 ) 
    image = tf.image.resize( image , MODEL_INPUT_IMAGE_SIZE ) / 255

    # Split the filename to get the age and the gender. Convert the age ( str ) and the gender ( str ) to dtype float32.
    parts = tf.strings.split( tf.strings.split( filename , '/' )[ 2 ] , '_' )

    # Normalize
    age = tf.strings.to_number( parts[ 0 ] ) / 116

    return image , age

# List all the image files in the given directory.
list_ds = tf.data.Dataset.list_files( 'data/DataBDC/*' , shuffle=True )

# Map `parse_image` method to all filenames.
dataset = list_ds.map( parse_image , num_parallel_calls=tf.data.AUTOTUNE )
dataset = dataset.take( N )