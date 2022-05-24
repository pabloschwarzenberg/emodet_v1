import pandas as pd

"""
    Cabeceras de archivo:
        Timestamp
        Por favor ingresa tu rut (sin puntos y con guión)

        Conjunto Objetivos Claros
            Los objetivos del juego eran claros (ObjetivoJuego)
            Los objetivos de cada nivel del juego eran claros (ObjetivoNivel)
            Los objetivos de los puzles del juego eran claros (ObjetivoPuzzle)
        
        Retroalimentacion
            La retroalimentación de mi progreso en el juego era adecuada
            La retroalimentación de mis acciones para resolver los puzles era adecuada
            La retroalimentación del efecto de mis acciones en el juego era oportuna
            La retroalimentación recibida  me permitía saber mi progreso para lograr los objetivos del juego
        
        Desafio
            El nivel de desafío del juego se adaptaba a mi habilidad
            El nivel de desafío del juego variaba en la medida que progresaba en el juego
            El juego provee nuevos desafíos con una progresión adecuada
            El juego provee puzles con desafíos de diferentes niveles de dificultad
        
        Enjoyment
            He disfrutado la experiencia de jugar el juego
            Fue satisfactorio encontrar como resolver cada uno de los desafíos del juego
            Una de mis motivaciones para continuar jugando era resolver los nuevos desafíos que se me presentaban
            Una de mis motivaciones para continuar jugando era resolver los nuevos desafíos que se me presentaban
        
        Interaccion Social
            Siento que la estructura del juego favoreció la discusión e intercambio de ideas con mis compañeros
            La cooperación en el juego fue útil para resolver los desafíos del juego
            Siento que la estructura del juego me permitió interactuar con mis compañeros y contar con su ayuda
        
        Autonomia
            Siento que tengo el control sobre mis acciones y su impacto en el juego
            Siento que tengo el control sobre mi éxito y avance en el juego
            Siento que puedo decidir cómo avanzar en el juego
        
        
        Versión del Juego
"""

# Funcion para eliminar las filas que contengan datos del juego Multi Player Física-Matemática
def EliminarFilas(datos):
    datos.drop(datos[datos["Versión del Juego"] == "Multi Player Física-Matemática"].index, inplace = True)
    datos.drop(["Timestamp"], axis=1, inplace=True)
    
# Funcion en el cual se le quita el guion al rut Cuestionario
def EliminarGuionCuestionario(datos):
    for indice, fila in datos.iterrows():
        variable = datos["Por favor ingresa tu rut (sin puntos y con guión)"][indice]
        if isinstance(variable, str):
            limpio = datos["Por favor ingresa tu rut (sin puntos y con guión)"][indice].replace("-", "")
            datos["Por favor ingresa tu rut (sin puntos y con guión)"][indice] = limpio



"""
    Datos del csv
        id
        player
        session
        level
        action
        time
        timestamp
        "replace(state,char(13),' ')" (Este es el que contiene la emocion)
"""

# Funcion en el cual se le quita el guion al rut Cuestionario
def EliminarGuionGameplay(datos):
    for indice, fila in datos.iterrows():
        variable = datos["player"][indice]
        if isinstance(variable, str):
            limpio = datos["player"][indice].replace("-", "")
            datos["player"][indice] = limpio

# Funcion para tener dataframe solo con emociones
def MantenerEmociones(datos):
    datos.drop(datos[datos["action"] != 4].index, inplace = True)
    # Se cambia nombre de columna a emocion
    datos.rename(columns={
        "state": "emocion"
        }, inplace=True)


# Los nombre no son iguales ej: joy - Joy
"""
    Los Nombres quedaran finalmente:
        Anxiety Frustration
        Wonder
        Joy
        Neutral Bored
"""
def ArreglarNombreEmocion(datos):
    for indice, fila in datos.iterrows():
        emocion = datos['emocion'][indice]
        if emocion == "joy":
            datos['emocion'][indice] = "Joy"
        if emocion == "anxiety_frustration":
            datos['emocion'][indice] = "Anxiety Frustration"
        if emocion == "wonder":
            datos['emocion'][indice] = "Wonder"
        if emocion == "neutral_bored":
            datos['emocion'][indice] = "Neutral Bored"