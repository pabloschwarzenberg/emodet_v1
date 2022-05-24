# Tesis Francisco Miranda

## Instalación
### Tensorflow con python 3.7 usando Conda
#### Activar ambiente para tensorflow 2.0 y ejecutar:
#### "conda install tensorflow-gpu==2.0"
#### "pip install keras"
#### Activar ambiente para tensorflow 1.15 y ejecutar:
#### "conda install tensorflow==1.15"
#### "pip install keras"
### Tensorflow libtensorflow 1.15 para C/C++
#### Descargar desde la pagina oficial "https://www.tensorflow.org/install/lang_c"
#### Para Linux y Mac utilizar guia de la pagina
### En Windows:
#### Descomprimir en la carpeta Tesis/Vision/Vision
#### Copiar archivo que esta en libtensorflow-cpu-windows-x86_64-1.15.0/lib "tensorflow.dll"
### Instalacion OpenCV
#### Descargar OpenCV desde la pagina oficial "https://sourceforge.net/projects/opencvlibrary/"
#### Descromprimir en la carpeta Tesis/Vision/Vision

### Python + Tensorflow. (Red neuronal se usa tensorflow 2.0 Se recomienda con gpu)
##### Uso de cnn para poder detectar emocion a travez de rasgos faciales, en los cuales se usan un conjunto de dataset clasificado por su estado emocional.
##### 1.- Se neceita la carpeta caras dentro de la carpeta Python + Tensor
##### 2.- Ejecutar codigo train.py, con esto se creara un archivo .h5 con el modelo y peso.

### Convertir archivo .h5 (se usa tensorflow 1.15)
##### 1.- Ejecutar archivo convert.py esto creara un carpeta con la cual se tendra un archivo .pb con toda su configuiración
##### 2.- Copiar carpeta ModeloPb en Vision/Vision

### Python + OpenCV
##### Uso de la libreria OpenCV para hacer la misma tarea anterior pero con un trabajos adicionales de tener que detectar primero el rostro y posteriormente clasificar.

### C++ + OpenCV
##### Ejecutar archivo con visual studio 15 o posterior
# emodet_v1
