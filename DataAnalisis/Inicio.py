# Importar Libreria Sistema.
import os
import pandas as pd

# Importar Funciones Propias.
# Funciones Encuesta.
from LimpiarArchivos import *
from GraficosEncuesta import *

# Funcion de graficar emociones
from GraficarEmociones import *

# Grafico de Mapa de Calor
from MapaCalor import *

# Revisa Existencia de Carpetas.
# Carpeta Para Grafico Encuesta.
try:
    os.stat("GraficosEncuesta")
except:
    os.mkdir("GraficosEncuesta")
# Carpeta Para Grafico Emociones Juego.
try:
    os.stat("GraficosEmociones")
except:
    os.mkdir("GraficosEmociones")
# Carpeta Para Grafico Emociones por Jugador.
try:
    os.stat("GraficosJugador")
except:
    os.mkdir("GraficosJugador")

# Se trabaja con excel de encuesta.
dfCuestionario = pd.read_excel('./FranciscoM/Cuestionario.xlsx') #Lectura de archivo.
dfCuestionarioEmocion = pd.read_excel('./FranciscoM/Cuestionario-Emocion.xlsx') #Lectura de archivo.

EliminarFilas(dfCuestionario) # Elimina filas de encuesta de otro juego.
EliminarGuionCuestionario(dfCuestionario) # Deja rut sin guion.

ObjetivosClaros(dfCuestionario) # Grafica resultado de encuesta para conjunto de preguntas.
GraficoConjuntoPreguntas(dfCuestionario) 
Retroalimentacion(dfCuestionario) # Grafica resultado de encuesta para conjunto de preguntas.
Desafios(dfCuestionario) # Grafica resultado de encuesta para conjunto de preguntas.
Enjoyment(dfCuestionario) # Grafica resultado de encuesta para conjunto de preguntas.
InteraccionSocial(dfCuestionario) # Grafica resultado de encuesta para conjunto de preguntas.
Autonomia(dfCuestionario) # Grafica resultado de encuesta para conjunto de preguntas.


# Se trabaja con excel generado en juego.
dfEmociones = pd.read_csv('./FranciscoM/dataset_juego2.csv', sep=",")

EliminarGuionGameplay(dfEmociones)
MantenerEmociones(dfEmociones) # Se deja el dataframe solo con datos de emociones del jugador.
ArreglarNombreEmocion(dfEmociones) # Arregla nombre de las emociones
GraficarEmociones(dfEmociones) # Grafica las repeticion de emociones en el juego
FotografiasNivel(dfEmociones) # Grafica la cantidad de fotografias por nivel
NivelFacilEmocion(dfEmociones) # Grafica emociones en el nivel Facil
NivelMedioEmocion(dfEmociones) # Grafica emociones en el nivel Medio
NivelDificilEmocion(dfEmociones) # Grafica emociones en el nivel Dificil
EmocionJugador(dfEmociones) # Grafica las emociones del jugador dentro del gameplay


# Se Grafica Mapa de Calor
#GraficoCalor(dfCuestionario, dfEmociones)
GraficoCalorEncuesta(dfCuestionario)

#EmocionJugador(dfEmociones)
GraficoCalorEncuestaEmocion(dfCuestionarioEmocion)
