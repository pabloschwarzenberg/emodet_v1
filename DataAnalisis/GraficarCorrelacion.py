import os
import numpy as np
import pandas as pd
from scipy import stats
import seaborn as sbn
import matplotlib
import matplotlib.pyplot as plt

# Carpeta para Correlacion de preguntas
try:
        os.stat("Correlaciones")
except:
        os.mkdir("Correlaciones")


dfCuestionarioEmocion = pd.read_excel('./FranciscoM/Cuestionario-Emocion.xlsx')

columnas = len(dfCuestionarioEmocion.columns)
j=1
for i in range(columnas-1):
    while j < columnas:
        slope, intercept, r, p, stderr = stats.linregress(dfCuestionarioEmocion.iloc[:, i], dfCuestionarioEmocion.iloc[:, j])
        line = f'Regresion line: y={intercept:.2f}+{slope:.2f}dfCuestionarioEmocion[i], r={r:.2f}'
        fig, ax = plt.subplots()
        ax.plot(dfCuestionarioEmocion.iloc[:, i], dfCuestionarioEmocion.iloc[:, j], linewidth=0, marker='s', label='Data Points')
        ax.plot(dfCuestionarioEmocion.iloc[:, i], intercept + slope * dfCuestionarioEmocion.iloc[:, i], label=line)
        ax.set_xlabel(dfCuestionarioEmocion.iloc[:,i].name)
        ax.set_ylabel(dfCuestionarioEmocion.iloc[:,j].name)
        ax.legend(facecolor='white')
        #plt.show()
        plt.savefig('./Correlaciones/'+dfCuestionarioEmocion.iloc[:,i].name+'pregunta'+str(j)+'.png')
        plt.clf()
        j+=1
    j=i+2
