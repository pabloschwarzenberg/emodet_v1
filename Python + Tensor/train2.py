# Librerias
# Librerias sistema
import sys
import os
# Libreria Tensorflow
import tensorflow as tf
# API Keras
from keras.layers import Dropout, Flatten, Dense, Activation, Convolution2D, MaxPooling2D
from keras.preprocessing.image import ImageDataGenerator
from keras.models import Sequential
from keras import backend as K
from keras import optimizers

# Limpiar sesion (memoria)
K.clear_session()

# Obtenemos imagenes
image_train = "../caras/entrenamiento"
image_validation = "../caras/validacion"

# Parametros globales
epoch = 10
height = 150
width = 150
batch_size = 25
steps_per_epoch = 500
validation_steps = 250
filter_conv1 = 32
filter_conv2 = 64
filter_conv3 = 128
size_filter1 = (4,4)
size_filter2 = (3,3)
size_filter3 = (2,2)
size_pool = (2,2)
class_model = 8
lr = 0.0001

# Preparar imagen para ser procesadas
train_data_generator = ImageDataGenerator(
    rescale = 1/255,
    shear_range = 0.1,
    zoom_range = 0.1,
    horizontal_flip = True
)

train_generator = train_data_generator.flow_from_directory(
    image_train,
    target_size = (height, width),
    batch_size = batch_size,
    class_mode = 'categorical'
)

test_data_generator = ImageDataGenerator(
    rescale = 1/255
)

validation_generator = test_data_generator.flow_from_directory(
    image_validation,
    target_size = (height, width),
    batch_size = batch_size,
    class_mode = 'categorical'
)

#Creacion de modelo
cnn = Sequential()

cnn.add(Convolution2D(
    filter_conv1,
    size_filter1,
    padding = 'same',
    input_shape = (height, width, 3),
    activation = 'relu'
))

cnn.add(MaxPooling2D(
    pool_size = size_pool,
    strides=None
))

cnn.add(Convolution2D(
    filter_conv2,
    size_filter2,
    padding = 'same'
))
cnn.add(MaxPooling2D(
    pool_size = size_pool,
    strides=None
))

cnn.add(Convolution2D(
    filter_conv3,
    size_filter3,
    padding = 'same'
))
cnn.add(MaxPooling2D(
    pool_size = size_pool,
    strides=None
))

cnn.add(Flatten())

cnn.add(Dense(
    128,
    activation = 'relu'
))

cnn.add(Dropout(
    0.4,
    noise_shape=None, 
    seed=None
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

target_dir = './modelos'
if not os.path.exists(target_dir):
    os.mkdir(target_dir)

cnn.save('./modelos/models.h5')
cnn.save_weights('./modelos/weight.h5')