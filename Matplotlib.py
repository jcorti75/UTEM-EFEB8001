 #-------Scatter plot con series------------#  
 
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/Diego/Downloads/iris.csv")
grupos=pd.unique(df.variety) #Extrae los niveles de la variable variety (tipos de flores)
colores=["red", "green", "blue"] #Arreglo de colores

for i in range(len(grupos)):
             plt.scatter(x=df.loc[df.variety==grupos[i],"sepal.length"], y=df.loc[df.variety==grupos[i],"sepal.width"],  #Va graficando cada conjunto de puntos (tipos de flores) con distinto color
             c=colores[i], label=grupos[i])

plt.title("Iris Dataset")  #Agrega título al gráfico
plt.xlabel("Sepal Length") #Agrega etiqueta al eje x del gráfico
plt.ylabel("Sepal Width")  #Agrega etiqueta al eje y del gráfico
plt.legend()  #Agregar leyenda al gráfico
plt.show()  #Muestra el gráfico