import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sb

# Grafica Contador de Emociones Totales.
def GraficarEmociones(datos):
    emociones = datos['emocion'].value_counts()
    Etiquetas = ['Anx_Frus', 'Joy', 'Neu_Bor', 'Wonder']
    EstadoJugador = [emociones["Anxiety Frustration"], emociones["Joy"], emociones["Neutral Bored"], emociones["Wonder"]]

    y_pos = np.arange(len(Etiquetas))

    plt.barh(y_pos, EstadoJugador, align="center", alpha=0.5)
    plt.yticks(y_pos, Etiquetas)
    plt.xlabel('Fotografias')
    plt.title('Datos Emocion Jugador')
    plt.savefig('./GraficosEmociones/Emocion.png')
    plt.clf()

# Grafica Contador De Fotografias Por Dificultad.
def FotografiasNivel(datos):
    nivel = datos['level'].value_counts()
    Etiquetas = ['N_Baj', 'N_Med', 'N_Alt']
    EstadoJugador = [nivel["N3D_2B"], nivel["N3D_2M"], nivel["N3D_2A"]]

    y_pos = np.arange(len(Etiquetas))

    plt.barh(y_pos, EstadoJugador, align="center", alpha=0.5)
    plt.yticks(y_pos, Etiquetas)
    plt.xlabel('Fotografias')
    plt.title('Datos Fotografias Nivel')
    plt.savefig('./GraficosEmociones/FotografiaNivel.png')
    plt.clf()

# Grafica Contador de Emociones en Nivel Facil
def NivelFacilEmocion(datos):
    Anx_Frus = 0
    Joy = 0
    Neu_Bor = 0
    Wonder = 0
    nivelFacil = datos.loc[:, 'level'] == 'N3D_2B'
    dfFacil = datos.loc[nivelFacil]

    emociones = dfFacil['emocion'].value_counts()

    for indice, fila in emociones.items():
        if indice == "Anxiety Frustration":
            Anx_Frus = fila
        if indice == "Joy":
            Joy = fila
        if indice == "Neutral Bored":
            Neu_Bor = fila
        if indice == "Wonder":
            Wonder = fila
    
    Etiquetas = ['Anx_Frus', 'Joy', 'Neu_Bor', 'Wonder']
    EstadoJugador = [Anx_Frus, Joy, Neu_Bor, Wonder]

    y_pos = np.arange(len(Etiquetas))

    plt.barh(y_pos, EstadoJugador, align="center", alpha=0.5)
    plt.yticks(y_pos, Etiquetas)
    plt.xlabel('Fotografias')
    plt.title('Emocion Jugador Nivel Facil')
    plt.savefig('./GraficosEmociones/EmocionNivelFacil.png')
    plt.clf()

# Grafica Contador de Emociones en Nivel Medio
def NivelMedioEmocion(datos):
    Anx_Frus = 0
    Joy = 0
    Neu_Bor = 0
    Wonder = 0
    nivelMedio = datos.loc[:, 'level'] == 'N3D_2M'
    dfMedio = datos.loc[nivelMedio]
    
    emociones = dfMedio['emocion'].value_counts()

    for indice, fila in emociones.items():
        if indice == "Anxiety Frustration":
            Anx_Frus = fila
        if indice == "Joy":
            Joy = fila
        if indice == "Neutral Bored":
            Neu_Bor = fila
        if indice == "Wonder":
            Wonder = fila

    Etiquetas = ['Anx_Frus', 'Joy', 'Neu_Bor', 'Wonder']
    EstadoJugador = [Anx_Frus, Joy, Neu_Bor, Wonder]

    y_pos = np.arange(len(Etiquetas))

    plt.barh(y_pos, EstadoJugador, align="center", alpha=0.5)
    plt.yticks(y_pos, Etiquetas)
    plt.xlabel('Fotografias')
    plt.title('Emocion Jugador Nivel Medio')
    plt.savefig('./GraficosEmociones/EmocionNivelMedio.png')
    plt.clf()

# Grafica Contador de Emociones en Nivel Dificil
def NivelDificilEmocion(datos):
    Anx_Frus = 0
    Joy = 0
    Neu_Bor = 0
    Wonder = 0
    nivelDificil = datos.loc[:, 'level'] == 'N3D_2A'
    dfDificil = datos.loc[nivelDificil]
    emociones = dfDificil['emocion'].value_counts()

    for indice, fila in emociones.items():
        if indice == "Anxiety Frustration":
            Anx_Frus = fila
        if indice == "Joy":
            Joy = fila
        if indice == "Neutral Bored":
            Neu_Bor = fila
        if indice == "Wonder":
            Wonder = fila
    
    Etiquetas = ['Anx_Frus', 'Joy', 'Neu_Bor', 'Wonder']
    EstadoJugador = [Anx_Frus, Joy, Neu_Bor, Wonder]

    y_pos = np.arange(len(Etiquetas))

    plt.barh(y_pos, EstadoJugador, align="center", alpha=0.5)
    plt.yticks(y_pos, Etiquetas)
    plt.xlabel('Fotografias')
    plt.title('Emocion Jugador Nivel Dificil')
    plt.savefig('./GraficosEmociones/EmocionNivelDificil.png')
    plt.clf()


# Grafica Emociones por Jugador
def EmocionJugador(datos):
    ListaJugadores = []
    Jugadores = datos['player'].value_counts()
    for indice, fila in Jugadores.items():
        ListaJugadores.append(indice)
    
    Anx_Frus = 0
    Joy = 0
    Neu_Bor = 0
    Wonder = 0
    for i in ListaJugadores:
        jugador = datos.loc[:, 'player'] == i
        EmocionJugador = datos.loc[jugador]
        
        emociones = EmocionJugador['emocion'].value_counts()

        for indice, fila in emociones.items():
            if indice == "Anxiety Frustration":
                Anx_Frus = fila
            if indice == "Joy":
                Joy = fila
            if indice == "Neutral Bored":
                Neu_Bor = fila
            if indice == "Wonder":
                Wonder = fila

        Etiquetas = ['Anx_Frus', 'Joy', 'Neu_Bor', 'Wonder']
        EstadoJugador = [Anx_Frus, Joy, Neu_Bor, Wonder]

        y_pos = np.arange(len(Etiquetas))

        plt.barh(y_pos, EstadoJugador, align="center", alpha=0.5)
        plt.yticks(y_pos, Etiquetas)
        plt.xlabel('Fotografias')
        plt.title('Emocion Gameplay Jugador')
        plt.savefig('./GraficosJugador/EmocionJugador '+i+'.png')
        plt.clf()