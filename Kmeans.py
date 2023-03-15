import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans


df=pd.read_csv("C:/Users/Diego/Downloads/iris.csv") #Importo los datos
X=np.array(df.loc[:,df.columns[df.columns!="variety"]])  #Tomo solo los features y los paso a un arrego de numpy
X.shape  #Ver la forma de X
Y=np.array(df.loc[:,"variety"]) #Tomamos la columna variety y lo pasamos a un arreglo de numpy
Y.shape  #Ver la forma de Y

k_means=KMeans(n_clusters=3) #Creamos el modelo k-means
k_means.fit(X) #Ajustamos el modelo a los datos (entrenamiento)
centros=k_means.cluster_centers_ #Obtengo los centros de los clusters
labels=k_means.labels_   #Obtengo los labels de los registros (asignaciones a grupos)
labels=np.array(["Cluster "+str(i+1) for i in labels]) #Ponerle nombre a los clusters

pca = PCA(n_components=2) #Creamos el modelo de componentes principales
pca.fit(X)  #Ajustamos el modelo
X_pca=pca.transform(X)  #Aplica el modelo a los datos
centros_pca=pca.transform(centros) #Aplica el modelo a los centros

grupos=np.unique(labels)  #Obtengo los nombres únicos de los clusters
colores=["red", "green", "blue"] #Arreglo de colores

for i in range(len(grupos)):
             plt.scatter(x=[a[0] for a in X_pca[labels==grupos[i]]], y=[a[1] for a in X_pca[labels==grupos[i]]],  #Va graficando cada conjunto de puntos (clusters) con distinto color
             c=colores[i], label=grupos[i])
             plt.scatter(x=centros_pca[i][0], y=centros_pca[i][1], c='black', marker='x', s=200) #Graficar centros de los clusters

plt.title("Iris Dataset")  #Agrega título al gráfico
plt.xlabel("Component 1") #Agrega etiqueta al eje x del gráfico
plt.ylabel("Component 2")  #Agrega etiqueta al eje y del gráfico
plt.legend()  #Agregar leyenda al gráfico
plt.show()  #Muestra el gráfico



