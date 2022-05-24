import pandas as pd
import numpy as np
import seaborn as snb
import matplotlib
import matplotlib.pyplot as plt

def CambiarEmocionANumero(datos):
    for indice, fila in datos.iterrows():
        emocion = datos['emocion'][indice]
        if emocion == "Joy":
            datos['emocion'][indice] = 1.0
        if emocion == "Anxiety Frustration":
            datos['emocion'][indice] = 2.0
        if emocion == "Wonder":
            datos['emocion'][indice] = 3.0
        if emocion == "Neutral Bored":
            datos['emocion'][indice] = 4.0
    
    datos['emocion'] = datos['emocion'].astype(str).astype(float)


def GraficoCalor(dato1, dato2):    
    #Eliminamos columnas de no interes
    del dato1['Por favor ingresa tu rut (sin puntos y con guión)']
    del dato1['Versión del Juego']
    del dato1['Una de mis motivaciones para continuar jugando era resolver los nuevos desafíos que se me presentaban']
    del dato2['player']
    del dato2['session']
    del dato2['level']
    del dato2['action']
    del dato2['time']
    del dato2['timestamp']
    

    dato1 = dato1.reset_index(drop=True)  #Se reinicia el index dado que viene desfasado
    dato2 = dato2.reset_index(drop=True)  #Se reinicia el index dado que viene desfasado
    CambiarEmocionANumero(dato2) #Se transaforma los string a numero
    
    Datos = pd.DataFrame()
    Datos = Datos.append(dato1)
    Datos['emocion'] = dato2
    Datos = Datos.dropna()
    Datos = Datos.reset_index(drop=True)  #Se reinicia el index dado que viene desfasado

    Datos = Datos.values.T
    dato2 = dato2.values.T
    _dato1 = np.corrcoef(dato1)
    _dato2 = np.corrcoef(dato2)
    
    _Datos = np.corrcoef(Datos)
    grafico = snb.heatmap(_Datos, annot=True)
    plt.show()
    plt.clf()


# Mapa Calor Preguntas Encuentas
def GraficoCalorEncuesta(dato1):    
    #Eliminamos columnas de no interes
    del dato1['Por favor ingresa tu rut (sin puntos y con guión)']
    del dato1['Versión del Juego']
    

    dato1 = dato1.reset_index(drop=True)  #Se reinicia el index dado que viene desfasado
    
    dato1 = dato1.reset_index(drop=True)  #Se reinicia el index dado que viene desfasado

    dato1 = dato1.values.T
    _dato1 = np.corrcoef(dato1)
    
    _dato1 = np.corrcoef(_dato1)
    grafico = snb.heatmap(_dato1)
    #plt.show()
    plt.savefig('./GraficosEncuesta/MapaCalorEncuesta.png')
    plt.clf()

# Mapa Calor Preguntas Encuentas
def GraficoCalorEncuestaEmocion(dato1):    
    #Eliminamos columnas de no interes
    """
    del dato1['Por favor ingresa tu rut (sin puntos y con guión)']
    del dato1['Versión del Juego']
    """
    print(dato1.columns)

    dato1 = dato1.reset_index(drop=True)  #Se reinicia el index dado que viene desfasado
    
    dato1 = dato1.reset_index(drop=True)  #Se reinicia el index dado que viene desfasado

    dato1 = dato1.values.T
    _dato1 = np.corrcoef(dato1)
    
    _dato1 = np.corrcoef(_dato1)
    grafico = snb.heatmap(_dato1)
    #plt.show()
    plt.savefig('./GraficosEncuesta/MapaCalorEncuestaEmocion.png')
    plt.clf()