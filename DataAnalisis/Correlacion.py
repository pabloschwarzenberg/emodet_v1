import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sbn

#dfCuestionario = pd.read_excel('./FranciscoM/Cuestionario.xlsx')

dfCuestionarioEmocion = pd.read_excel('./FranciscoM/Cuestionario-Emocion.xlsx', skiprows=0) #Obtiene Dataset
dfCuestionario = dfCuestionarioEmocion.iloc[:,0:20] #Mantiene datos de Encuesta
dfEmociones = dfCuestionarioEmocion.iloc[:,20:24] #Mantiene datos de Emocion
"""
auxCuestionarioEmocion = dfCuestionarioEmocion.to_numpy()
auxCuestionario = dfCuestionario.to_numpy()
auxEmocion = dfEmociones.to_numpy()

# Coeficiente de correlacion Cuestionario con emocion
resCE = np.corrcoef(auxCuestionarioEmocion)
print("Imprime Correlacion Cuestionario con Emocion\n")
print(resCE)
print("\n\n\n")

# Coeficiente de correlacion Cuestionario
resC = np.corrcoef(auxCuestionario)
print("Imprime Correlacion Cuestionario\n")
print(resC)
print("\n\n\n")

# Coeficiente de correlacion Cuestionario
resE = np.corrcoef(auxEmocion)
print("Imprime Correlacion Emociones\n")
print(resE)
print("\n\n\n")
"""

MetodoPearson = dfCuestionarioEmocion.corr(method="pearson")
print("Imprime Metodo Pearson\n", MetodoPearson)

MetodoSpearman = dfCuestionarioEmocion.corr(method="spearman")
print("Imprime Metodo Spearman\n", MetodoSpearman)

MetodoKendall = dfCuestionarioEmocion.corr(method="kendall")
print("Imprime Metodo Kendall\n", MetodoKendall)

prueba2 = dfCuestionario.corr(dfCuestionario)
print("adasdasd\n", prueba2)
