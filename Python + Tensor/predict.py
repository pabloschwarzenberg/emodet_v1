import numpy as np
from keras.preprocessing.image import load_img, img_to_array
from keras.models import load_model


longitud = 150
altura = 150
modelo = "./modelo/models.h5"
peso_modelo = "./modelo/weight.h5"
cnn = load_model(modelo)
cnn.load_weights(peso_modelo)

def predict(file):
    x = load_img(file, target_size=(longitud, altura))
    x = img_to_array(x)
    x = np.expand_dims(x, axis=0)
    array = cnn.predict(x)
    result = array[0]
    answer = np.argmax(result)
    if answer == 0:
        print("pred: Asco")
    elif answer == 1:
        print("pred: Desprecio")
    elif answer == 2:
        print("pred: Feliz")
    elif answer == 3:
        print("pred: Ira-enojo")
    elif answer == 4:
        print("pred: neutro-aburrimiento")
    elif answer == 5:
        print("pred: sorpresa")
    elif answer == 6:
        print("pred: temor")
    elif answer == 7:
        print("pred: trsiteza")
    
    return answer

predict("D://Proyectos//Tesis//caras//entrenamiento//ira-enojo//1L10SDRHWX.jpg")