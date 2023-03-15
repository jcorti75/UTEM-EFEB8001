import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

df=pd.read_csv("C:/Users/Diego/Downloads/iris.csv") #Importo los datos
X=np.array(df.loc[:,df.columns[df.columns!="variety"]])  #Tomo solo los features y los paso a un arrego de numpy
X.shape  #Ver la forma de X
Y=np.array(df.loc[:,"variety"]) #Tomamos la columna variety y lo pasamos a un arreglo de numpy
Y.shape  #Ver la forma de Y
pca = PCA(n_components=2) #Creamos el modelo de componentes principales
pca.fit(X)  #Ajustamos el modelo
scores=pca.components_   #Ver los pesos de las componentes
varianza=pca.explained_variance_ratio_  #Porcentaje de varianza explicada por cada componente
np.sum(varianza)  #Si N° de componentes = N° de variables la suma es 1
X_pca=pca.transform(X)  #Aplica el modelo a los datos


grupos=pd.unique(df.variety) #Extrae los niveles de la variable variety (tipos de flores)
colores=["red", "green", "blue"] #Arreglo de colores

for i in range(len(grupos)):
             plt.scatter(x=[a[0] for a in X_pca[Y==grupos[i]]], y=[a[1] for a in X_pca[Y==grupos[i]]],  #Va graficando cada conjunto de puntos (tipos de flores) con distinto color
             c=colores[i], label=grupos[i])

plt.title("Iris Dataset")  #Agrega título al gráfico
plt.xlabel("Component 1") #Agrega etiqueta al eje x del gráfico
plt.ylabel("Component 2")  #Agrega etiqueta al eje y del gráfico
plt.legend()  #Agregar leyenda al gráfico
plt.show()  #Muestra el gráfico

