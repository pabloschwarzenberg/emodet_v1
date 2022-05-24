# Librerias
import sys
import os
import tensorflow as tf
from keras.preprocessing.image import ImageDataGenerator
from keras import optimizers
from keras.models import Sequential
from keras.layers import Dropout, Flatten, Dense, Activation, Convolution2D, MaxPooling2D
from keras import backend as K

#Limpiar sesion (memoria)
K.clear_session()

#Obtenemos imagenes
image_train = "../caras/entrenamiento"
image_validation = "../caras/validacion"

#Parametros globales
epoch = 20
height = 150
width = 150
batch_size = 50
steps_per_epoch = 1000
validation_steps = 300
filter_conv1 = 32
filter_conv2 = 64
size_filter1 = (3,3)
size_filter2 = (2,2)
size_pool = (2,2)
class_model = 4
lr = 0.0001

#Preparar imagen para ser procesadas
train_data_generator = ImageDataGenerator(
    rescale = 1./255,
    shear_range = 0.2,
    zoom_range = 0.2,
    horizontal_flip = True,
)

test_data_generator = ImageDataGenerator(
    rescale = 1./255
)

train_generator = train_data_generator.flow_from_directory(
    image_train,
    target_size = (height, width),
    batch_size = batch_size,
    class_mode = 'categorical',
    color_mode = 'grayscale'
)

validation_generator = test_data_generator.flow_from_directory(
    image_validation,
    target_size = (height, width),
    batch_size = batch_size,
    class_mode = 'categorical',
    color_mode = 'grayscale'
)

#Creacion de modelo
cnn = Sequential()

cnn.add(Convolution2D(
    filter_conv1,
    size_filter1,
    padding = 'same',
    input_shape = (height, width, 1),
    activation = 'relu'
))

cnn.add(MaxPooling2D(
    pool_size = size_pool
))

cnn.add(Convolution2D(
    filter_conv2,
    size_filter2,
    padding = 'same'
))
cnn.add(MaxPooling2D(
    pool_size = size_pool
))

cnn.add(Flatten())

cnn.add(Dense(
    256,
    activation = 'relu'
))

cnn.add(Dropout(
    0.5
))

cnn.add(Dense(
    class_model,
    activation = 'softmax'
))

cnn.compile(
    loss = "categorical_crossentropy",
    optimizer = optimizers.Adam(lr = lr),
    metrics = ['accuracy']
)

cnn.fit_generator(
    train_generator,
    steps_per_epoch= steps_per_epoch,
    epochs = epoch,
    validation_data = validation_generator,
    validation_steps = validation_steps
)

target_dir = './modelo'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

cnn.save('./modelo/models.h5')
cnn.save_weights('./modelo/weight.h5')