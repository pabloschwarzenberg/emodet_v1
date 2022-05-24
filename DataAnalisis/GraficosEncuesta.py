import matplotlib
import matplotlib.pyplot as plt
import numpy as np

def ObjetivosClaros(datos):
    """
        Conjunto Objetivos Claros
            Los objetivos del juego eran claros (ObjetivoJuego)
            Los objetivos de cada nivel del juego eran claros (ObjetivoNivel)
            Los objetivos de los puzles del juego eran claros (ObjetivoPuzzle)
    """
    ObjetivoJuego = datos["Los objetivos del juego eran claros"]
    MaxObjJuego = ObjetivoJuego.max() #MaxOJ
    MinObjJuego = ObjetivoJuego.min() #MinOJ
    MediaObjJuego = ObjetivoJuego.median() #MedOJ

    ObjetivoNivel = datos["Los objetivos de cada nivel del juego eran claros"]
    MaxObjNivel = ObjetivoNivel.max() #MaxON
    MinObjNivel = ObjetivoNivel.min() #MinON
    MediaObjNivel = ObjetivoNivel.median() #MedON

    ObjetivoPuzzle = datos["Los objetivos de los puzles del juego eran claros"]
    MaxObjPuzzle = ObjetivoPuzzle.max() #MaxOP
    MinObjPuzzle = ObjetivoPuzzle.min() #MinOP
    MediaObjPuzzle = ObjetivoPuzzle.median() #MedOP
    
    Etiquetas = ['MaxOJ', 'MinOJ', 'MedOJ', 'MaxON', 'MinON', 'MedON', 'MaxOP', 'MinOP', 'MedOP']
    calificacion = [MaxObjJuego, MinObjJuego, MediaObjJuego, MaxObjNivel, MinObjNivel, MediaObjNivel, MaxObjPuzzle, MinObjPuzzle, MediaObjPuzzle]

    y_pos = np.arange(len(Etiquetas))

    plt.barh(y_pos, calificacion, align="center", alpha=0.5, edgecolor='black')
    plt.yticks(y_pos, Etiquetas)
    plt.xlabel('Calificacion')
    plt.title('Datos Objetivos Claros')
    plt.savefig('./GraficosEncuesta/ObjetivosClaros.png')
    plt.clf()


def Retroalimentacion(datos):
    """
        Retroalimentacion
            La retroalimentación de mi progreso en el juego era adecuada (RetroProgJuego)
            La retroalimentación de mis acciones para resolver los puzles era adecuada (RetroAccionResolver)
            La retroalimentación del efecto de mis acciones en el juego era oportuna (RetroAccionJuego)
            La retroalimentación recibida  me permitía saber mi progreso para lograr los objetivos del juego (RetroPermiteLograrObj)
    """
    RetroProgJuego = datos["La retroalimentación de mi progreso en el juego era adecuada"]
    MaxRPJ = RetroProgJuego.max() #MaxRPJ
    MinRPJ = RetroProgJuego.min() #MinRPJ
    MediaRPJ = RetroProgJuego.median() ##MedRPJ
    
    RetroAccionResolver = datos["La retroalimentación de mis acciones para resolver los puzles era adecuada"]
    MaxRAR = RetroAccionResolver.max() #MaxRAR
    MinRAR = RetroAccionResolver.min() #MinRAR
    MediaRAR = RetroAccionResolver.median() #MedRAR
    
    RetroAccionJuego = datos["La retroalimentación del efecto de mis acciones en el juego era oportuna"]
    MaxRAJ = RetroAccionJuego.max() #MaxRAJ
    MinRAJ = RetroAccionJuego.min() #MinRAJ
    MediaRAJ = RetroAccionJuego.median() #MedRAJ
    
    RetroPermiteLograrObj = datos["La retroalimentación recibida  me permitía saber mi progreso para lograr los objetivos del juego"]
    MaxRPL = RetroPermiteLograrObj.max() #MaxRPL
    MinRPL = RetroPermiteLograrObj.min() #MinRPL
    MediaRPL = RetroPermiteLograrObj.median() #MedRPL
    
    Etiquetas = ['MaxRPJ', 'MinRPJ', 'MediaRPJ', 'MaxRAR', 'MinRAR', 'MediaRAR', 'MaxRAJ', 'MinRAJ', 'MediaRAJ', 'MaxRPL', 'MinRPL', 'MediaRPL']
    calificacion = [MaxRPJ, MinRPJ, MediaRPJ, MaxRAR, MinRAR, MediaRAR, MaxRAJ, MinRAJ, MediaRAJ, MaxRPL, MinRPL, MediaRPL]

    y_pos = np.arange(len(Etiquetas))

    plt.barh(y_pos, calificacion, align="center", alpha=0.5)
    plt.yticks(y_pos, Etiquetas)
    plt.xlabel('Calificacion')
    plt.title('Datos Retroalimentacion')
    plt.savefig('./GraficosEncuesta/Retroalimentacion.png')
    plt.clf()


def Desafios(datos):
    """
        Desafio
            El nivel de desafío del juego se adaptaba a mi habilidad (DesafioAdaptaHabilidad)
            El nivel de desafío del juego variaba en la medida que progresaba en el juego (DesafioVariaEnProgreso)
            El juego provee nuevos desafíos con una progresión adecuada (DesafioProgresoAdecuado)
            El juego provee puzles con desafíos de diferentes niveles de dificultad (DesafioDistintaDificultad)
    """
    DesafioAdaptaHabilidad = datos["El nivel de desafío del juego se adaptaba a mi habilidad"]
    MaxDAH = DesafioAdaptaHabilidad.max() #MaxDAH
    MinDAH = DesafioAdaptaHabilidad.min() #MinDAH
    MediaDAH = DesafioAdaptaHabilidad.median() ##MedDAH
    
    DesafioVariaEnProgreso = datos["El nivel de desafío del juego variaba en la medida que progresaba en el juego"]
    MaxDVP = DesafioVariaEnProgreso.max() #MaxDVP
    MinDVP = DesafioVariaEnProgreso.min() #MinDVP
    MediaDVP = DesafioVariaEnProgreso.median() #MedDVP
    
    DesafioProgresoAdecuado = datos["El juego provee nuevos desafíos con una progresión adecuada"]
    MaxDAP = DesafioProgresoAdecuado.max() #MaxDAP
    MinDAP = DesafioProgresoAdecuado.min() #MinDAP
    MediaDAP = DesafioProgresoAdecuado.median() #MedDAP
    
    DesafioDistintaDificultad = datos["El juego provee puzles con desafíos de diferentes niveles de dificultad"]
    MaxDDD = DesafioDistintaDificultad.max() #MaxDDD
    MinDDD = DesafioDistintaDificultad.min() #MinDDD
    MediaDDD = DesafioDistintaDificultad.median() #MedDDD
    
    Etiquetas = ['MaxDAH', 'MinDAH', 'MediaDAH', 'MaxDVP', 'MinDVP', 'MediaDVP', 'MaxDAP', 'MinDAP', 'MediaDAP', 'MaxDDD', 'MinDDD', 'MediaDDD']
    calificacion = [MaxDAH, MinDAH, MediaDAH, MaxDVP, MinDVP, MediaDVP, MaxDAP, MinDAP, MediaDAP, MaxDDD, MinDDD, MediaDDD]

    y_pos = np.arange(len(Etiquetas))

    plt.barh(y_pos, calificacion, align="center", alpha=0.5)
    plt.yticks(y_pos, Etiquetas)
    plt.xlabel('Calificacion')
    plt.title('Datos Desafio')
    plt.savefig('./GraficosEncuesta/Desafio.png')
    plt.clf()


def Enjoyment(datos):
    """
        Enjoyment
            He disfrutado la experiencia de jugar el juego (ExpJugarJuego)
            Fue satisfactorio encontrar como resolver cada uno de los desafíos del juego (SatisfaccionResolverDesafio)
            Una de mis motivaciones para continuar jugando era resolver los nuevos desafíos que se me presentaban (MotivacionSigDesafio)
    """
    ExpJugarJuego = datos["He disfrutado la experiencia de jugar el juego"]
    MaxExpJuego = ExpJugarJuego.max() #MaxEJJ
    MinExpJuego = ExpJugarJuego.min() #MinEJJ
    MediaExpJuego = ExpJugarJuego.median() #MedEJJ

    SatisfaccionResolverDesafio = datos["Fue satisfactorio encontrar como resolver cada uno de los desafíos del juego"]
    MaxSatResDes = SatisfaccionResolverDesafio.max() #MaxSRD
    MinSatResDes = SatisfaccionResolverDesafio.min() #MinSRD
    MediaSatResDes = SatisfaccionResolverDesafio.median() #MinSRD

    MotivacionSigDesafio = datos["Una de mis motivaciones para continuar jugando era resolver los nuevos desafíos que se me presentaban"]
    MaxMotSigDes = MotivacionSigDesafio.max() #MaxMSD
    MinMotSigDes = MotivacionSigDesafio.min() #MinMSD
    MediaMotSigDes = MotivacionSigDesafio.median() #MedMSD
    
    Etiquetas = ['MaxEJJ', 'MinEJJ', 'MedEJJ', 'MaxSRD', 'MinSRD', 'MinSRD', 'MaxMSD', 'MinMSD', 'MedMSD']
    calificacion = [MaxExpJuego, MinExpJuego, MediaExpJuego, MaxSatResDes, MinSatResDes, MediaSatResDes, MaxMotSigDes, MinMotSigDes, MediaMotSigDes]

    y_pos = np.arange(len(Etiquetas))

    plt.barh(y_pos, calificacion, align="center", alpha=0.5)
    plt.yticks(y_pos, Etiquetas)
    plt.xlabel('Calificacion')
    plt.title('Datos Enjoyment')
    plt.savefig('./GraficosEncuesta/Enjoyment.png')
    plt.clf()


def InteraccionSocial(datos):
    """
        Interaccion Social
            Siento que la estructura del juego favoreció la discusión e intercambio de ideas con mis compañeros (JuegoAyudaIntercambioIdeas)
            La cooperación en el juego fue útil para resolver los desafíos del juego (CooperacionResolverProblema)
            Siento que la estructura del juego me permitió interactuar con mis compañeros y contar con su ayuda
    """
    JuegoAyudaIntercambioIdeas = datos["Siento que la estructura del juego favoreció la discusión e intercambio de ideas con mis compañeros"]
    MaxJAII = JuegoAyudaIntercambioIdeas.max() #MaxJAII
    MinJAII = JuegoAyudaIntercambioIdeas.min() #MinJAII
    MediaJAII = JuegoAyudaIntercambioIdeas.median() #MedJAII

    CooperacionResolverProblema = datos["La cooperación en el juego fue útil para resolver los desafíos del juego"]
    MaxCRP = CooperacionResolverProblema.max() #MaxCRP
    MinCRP = CooperacionResolverProblema.min() #MinCRP
    MediaCRP = CooperacionResolverProblema.median() #MinCRP

    JuegoAyudaInteractuar = datos["Una de mis motivaciones para continuar jugando era resolver los nuevos desafíos que se me presentaban"]
    MaxJAI = JuegoAyudaInteractuar.max() #MaxJAI
    MinJAI = JuegoAyudaInteractuar.min() #MinJAI
    MediaJAI = JuegoAyudaInteractuar.median() #MedJAI
    
    Etiquetas = ['MaxJAII', 'MinJAII', 'MedJAII', 'MaxCRP', 'MinCRP', 'MinCRP', 'MaxJAI', 'MinJAI', 'MedJAI']
    calificacion = [MaxJAII, MinJAII, MediaJAII, MaxCRP, MinCRP, MediaCRP, MaxJAI, MinJAI, MediaJAI]

    y_pos = np.arange(len(Etiquetas))

    plt.barh(y_pos, calificacion, align="center", alpha=0.5)
    plt.yticks(y_pos, Etiquetas)
    plt.xlabel('Calificacion')
    plt.title('Datos Interaccion Social')
    plt.savefig('./GraficosEncuesta/InteraccionSocial.png')
    plt.clf()


def Autonomia(datos):
    """
        Autonomia
            Siento que tengo el control sobre mis acciones y su impacto en el juego (ControlAccionImpacto)
            Siento que tengo el control sobre mi éxito y avance en el juego (ControlExitoAvance)
            Siento que puedo decidir cómo avanzar en el juego (DecidirComoAvanzar)
    """
    ControlAccionImpacto = datos["Siento que tengo el control sobre mis acciones y su impacto en el juego"]
    MaxCAI = ControlAccionImpacto.max() #MaxCAI
    MinCAI = ControlAccionImpacto.min() #MinCAI
    MediaCAI = ControlAccionImpacto.median() #MedCAI

    ControlExitoAvance = datos["Siento que tengo el control sobre mi éxito y avance en el juego"]
    MaxCEA = ControlExitoAvance.max() #MaxCEA
    MinCEA = ControlExitoAvance.min() #MinCEA
    MediaCEA = ControlExitoAvance.median() #MinCEA

    DecidirComoAvanzar = datos["Siento que puedo decidir cómo avanzar en el juego"]
    MaxDCA = DecidirComoAvanzar.max() #MaxDCA
    MinDCA = DecidirComoAvanzar.min() #MinDCA
    MediaDCA = DecidirComoAvanzar.median() #MedDCA
    
    Etiquetas = ['MaxCAI', 'MinCAI', 'MediaCAI', 'MaxCEA', 'MinCEA', 'MinCEA', 'MaxDCA', 'MinDCA', 'MedDCA']
    calificacion = [MaxCAI, MinCAI, MediaCAI, MaxCEA, MinCEA, MediaCEA, MaxDCA, MinDCA, MediaDCA]

    y_pos = np.arange(len(Etiquetas))

    plt.barh(y_pos, calificacion, align="center", alpha=0.5)
    plt.yticks(y_pos, Etiquetas)
    plt.xlabel('Calificacion')
    plt.title('Datos Autonomia')
    plt.savefig('./GraficosEncuesta/Autonomia.png')
    plt.clf()


def GraficoConjuntoPreguntas(datos):
    # Se obtiene promedio de conjuntos de preguntas Objetivos Claros
    auxData = datos.iloc[:, 1:4]
    Col1 = auxData["Los objetivos del juego eran claros"]
    Med1 = Col1.median()
    Col2 = datos["Los objetivos de cada nivel del juego eran claros"]
    Med2 = Col2.median()
    Col3 = datos["Los objetivos de los puzles del juego eran claros"]
    Med3 = Col3.median()
    PromedioObjetivosClaros = (Med1+Med2+Med3)/3 #Contiene el promedio del conjunto pregunta Objetivos Claros.

    del auxData
    del Col1
    del Med1
    del Col2
    del Med2
    del Col3
    del Med3
    
    # Se obtiene promedio de conjuntos de preguntas Retroalimentacion
    auxData = datos.iloc[:, 4:8]
    Col1 = datos["La retroalimentación de mi progreso en el juego era adecuada"]
    Med1 = Col1.median()    
    Col2 = datos["La retroalimentación de mis acciones para resolver los puzles era adecuada"]
    Med2 = Col2.median()    
    Col3 = datos["La retroalimentación del efecto de mis acciones en el juego era oportuna"]
    Med3 = Col3.median()    
    Col4 = datos["La retroalimentación recibida  me permitía saber mi progreso para lograr los objetivos del juego"]
    Med4 = Col4.median()
    PromedioRetroalimentacion = (Med1+Med2+Med3+Med4)/4 #Contiene el promedio del conjunto pregunta Retroalimentacion.
    
    del auxData
    del Col1
    del Med1
    del Col2
    del Med2
    del Col3
    del Med3
    del Col4
    del Med4

    # Se obtiene promedio de conjuntos de preguntas Desafio
    auxData = datos.iloc[:, 8:12]
    Col1 = datos["El nivel de desafío del juego se adaptaba a mi habilidad"]
    Med1 = Col1.median()    
    Col2 = datos["El nivel de desafío del juego variaba en la medida que progresaba en el juego"]
    Med2 = Col2.median()    
    Col3 = datos["El juego provee nuevos desafíos con una progresión adecuada"]
    Med3 = Col3.median()    
    Col4 = datos["El juego provee puzles con desafíos de diferentes niveles de dificultad"]
    Med4 = Col4.median()
    PromedioDesafio = (Med1+Med2+Med3+Med4)/4 #Contiene el promedio del conjunto pregunta Desafio.
    
    del auxData
    del Col1
    del Med1
    del Col2
    del Med2
    del Col3
    del Med3
    del Col4
    del Med4

    # Se obtiene promedio de conjuntos de preguntas Enjoyment
    auxData = datos.iloc[:, 12:15]
    Col1 = auxData["He disfrutado la experiencia de jugar el juego"]
    Med1 = Col1.median()
    Col2 = datos["Fue satisfactorio encontrar como resolver cada uno de los desafíos del juego"]
    Med2 = Col2.median()
    Col3 = datos["Una de mis motivaciones para continuar jugando era resolver los nuevos desafíos que se me presentaban"]
    Med3 = Col3.median()
    PromedioEnjoyment = (Med1+Med2+Med3)/3 #Contiene el promedio del conjunto pregunta Enjoyment.

    del auxData
    del Col1
    del Med1
    del Col2
    del Med2
    del Col3
    del Med3

    # Se obtiene promedio de conjuntos de preguntas Interaccion
    auxData = datos.iloc[:, 15:18]
    Col1 = auxData["Siento que la estructura del juego favoreció la discusión e intercambio de ideas con mis compañeros"]
    Med1 = Col1.median()
    Col2 = datos["La cooperación en el juego fue útil para resolver los desafíos del juego"]
    Med2 = Col2.median()
    Col3 = datos["Siento que la estructura del juego me permitió interactuar con mis compañeros y contar con su ayuda"]
    Med3 = Col3.median()
    PromedioInteraccion = (Med1+Med2+Med3)/3 #Contiene el promedio del conjunto pregunta Interaccion.

    del auxData
    del Col1
    del Med1
    del Col2
    del Med2
    del Col3
    del Med3

    # Se obtiene promedio de conjuntos de preguntas Autonomia
    auxData = datos.iloc[:, 18:21]
    Col1 = auxData["Siento que tengo el control sobre mis acciones y su impacto en el juego"]
    Med1 = Col1.median()
    Col2 = datos["Siento que tengo el control sobre mi éxito y avance en el juego"]
    Med2 = Col2.median()
    Col3 = datos["Siento que puedo decidir cómo avanzar en el juego"]
    Med3 = Col3.median()
    PromedioAutonomia = (Med1+Med2+Med3)/3 #Contiene el promedio del conjunto pregunta Autonomia.

    del auxData
    del Col1
    del Med1
    del Col2
    del Med2
    del Col3
    del Med3

    """
        Objetivos Claros --> OBJCL
        Retroalimentacion --> RETRO
        Desafio --> DESAF
        Enjoyment --> ENJOY
        Interaccion --> INTER
        Autonomia --> AUTON
    """
    Etiquetas = ['OBJCL', 'RETRO', 'DESAF', 'ENJOY', 'INTER', 'AUTON']
    calificacion = [PromedioObjetivosClaros, PromedioRetroalimentacion, PromedioDesafio, PromedioEnjoyment, PromedioInteraccion, PromedioAutonomia]

    y_pos = np.arange(len(Etiquetas))

    plt.barh(y_pos, calificacion, align="center", alpha=0.5)
    plt.yticks(y_pos, Etiquetas)
    plt.xlabel('Calificacion')
    plt.title('Promedio Conjunto Preguntas')
    plt.savefig('./GraficosEncuesta/ConjuntoPregunta.png')
    plt.clf()