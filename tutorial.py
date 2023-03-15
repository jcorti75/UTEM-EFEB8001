##### Declaracion de Variables #######

#-------Int y Float------------#

myInt=10  #Declaración de variable Int
myFloat=10.5  #Declaración de variable Float

print(type(myInt))   #Imprime tipo de la variable
print(type(myFloat))   #Imprime tipo de la variable

myValue=10
myNumber=float(myValue)    #Transformar de Int a Float
print(myNumber)

myValue=10.4
myNumber=int(myValue)    #Transformar de Float a Int (Parte entera)
print(myNumber)

x=10
y=3
z=x+y
print(z)    #Imprime suma de x e y
print(x-y)  #Imprime resta de x e y
print(x/y)  #Imprime división de x e y
print(x//y) #Imprime piso del cociente entre x e y
print(x%y) #Imprime resto del cociente entre x e y
print(x**y) #Imprime x^y

#-------Strings------------#

myString="Hola Mundo"   #Declaración variable string
myString='Hola Mundo'   #Declaración variable string
myString=str(10.5)      #Conversión a string

x="Hola"
y=" Mundo"
z=x+y            #Concatenación de Strings
print(z)
print(z*2)       #Duplica el string

#Slicing de Strings
myString="Hola Mundo"
print(myString[0:4]) 
print(myString[:4])   
print(myString[5:]) 
print(myString[-1]) 
print(myString[-5:])
len(myString)     #Largo en caracteres de 
print("Largo: "+str(len(myString))+" letras")

#-------Booleans------------#

myBool=True   #Declaración de variable Boolean
myBool=False  #Declaración de variable Boolean

x=True
y=False
print(x and y)   #x & y  
print(x or y)    #x | y  

x=5
y=3
z=x>y     #z es una variable Booleana con valor True
print(z) 

z="Hola" in "Hola Mundo"  #testea si el texto "Hola" se encuentra en "Hola Mundo"
print(z)   

z=x<=y
print(z)

z=x==y
print(z)

z=x!=y
print(z)

z=not x==y      #Negación de la condición lógica
print(z) 

#-------Listas------------#

myList=list()  #Lista vacía
myList=[]      #Lista vacía
myList=["hola",8,True]   #Pueden contener distintos tipos de variables

x=[]   #Crear lista vacía
x.append("Hola")   #Agregar string a la lista
print(x)                 
x.append(8) #Agregar int a la lista
print(x)             
x.append(True)     #Agregar boolean a la lista
print(x)             
x=x+[9]   #Agregar un elemento a la lista
print(x)    
x=x+["Mundo", 3]    #Agregar más de un elemento a la lista
print(x)
len(x)     #Largo de la lista (N° de elementos)
len(x[0])  #Largo del primer elemento de la lista (N° de caracteres del String)
del x[0:2] #Eliminar dos primeros valores de la lista
print(x)         
print(x*2)    #Duplicar elementos de la lista

#-------Diccionarios------------#     

edades={"Diego": 27, "Paula": 33, "Jorge":35}  #Declaración de diccionario
edades["Diego"]     
edades["Paula"]   

edades["Juan"]=45     #Crear nuevo registro
del edades["Diego"]   #Borrar un registro


#-------Listas 2D------------#

x=[[1,2,3],
   [4,5,6]]

len(x)    #Largo de la lista(N° de elementos)
len(x[0]) #Largo del primer elemento de la lista (Largo de la primera lista)
x[0]   #Primer elemento de la lista de listas
x[1]   #Segundo elemento de la lista de listas
x[0][0]  #Primer elemento de la primera lista
x[0][1]  #Segundo elemento de la primera lista
x[1][0]  #Primer elemento de la segunda lista

#-------Listas 3D------------#
x=[[[1,2],[4,5]],
   [[6,7],[8,9]]]

x[0]
x[0][0]  
x[0][0][0]   


##### Expresiones condicionales #######

x=4
if (x-int(x))==0:
    print("x es entero")   
    if x>=5:    
             print("x es mayor o igual a 5")    
    elif x<=3:    
             print("x es menor o igual a 3")    
    else:    
            print("x es 4")
else:
    print("x es decimal")
    
##### Loops #######    
 #-------Ciclos while------------#   
contador=0
x=[]
y=[]
while contador<5:
    x.append(contador)
    y.append(contador**2)
    contador+=1    #contador=contador+1

print(x)     #Números del 0 al 4
print(y)     #Números del 0 al 4 elevados al cuadrado

 #-------Ciclos For------------#  
myNumbers=[2,4,6]
for x in myNumbers:
        print(x**2)  #Imprimir cada número de la lista al cuadrado
        
        
        
for x in range(len(myNumbers)):
          myNumbers[x]=myNumbers[x]**2   #Guardar los números al cuadrado en la misma lista
print(myNumbers)     



contar=0
myWords=["Jorge","Diego","Paula", "Diego"]
for x in myWords:
        if x=="Diego":
                   contar+=1
print("Diego aparece "+str(contar)+" veces")   #Contar cuántas veces sale el nombre Diego en la lista

 #-------List Comprehension------------#  
 
myNumbers=[x for x in range(5)]  #lista con números del 0 al 4
print(myNumbers)
      
myNumbers=[x**2 if x%2==0 else x for x in range(5)]  #Números del 0 al 4 donde los pares están elevados al cuadrado
print(myNumbers)
 
##### Declaración de funciones #######     
        
import math     #Importa librería math, para cargar el número pi
def volumen_cilindro(r,h):    #Función que calcula el volumen de un cilindro de radio r y altura h
    base=math.pi*(r**2)       #Cálculo del área de la base
    return base*h             #Retorna el área de la base por la altura (Volumen)

volumen_cilindro(2,3)    #Llama la función y calcula el volumen


def sumar_pares(myList):            #Función que suma los números pares de una lista
       y=[x for x in myList if x%2==0 ]      #Se queda solo con los números pares de la lista
       suma=0
       for i in y:
             suma+=i     #Va sumando los números de la lista y (pares)
       return suma

values=[1,2,3,4,5,6]
sumar_pares(values)     #Llama la función y calcula la suma de los pares

##### Numpy #######  

import numpy as np
x=[1,2,3,4]
x=np.array(x)   #Convierte lista en un arreglo de Numpy
x

x=x+2    #Le suma 2 a cada elemento del arreglo
print(x) 

x=x*2    #Multiplica por 2 cada elemento del arreglo
print(x)   

np.mean(x)  #Calcula la media del arreglo
np.max(x)   #Calcula el máximo del arreglo

y=[1,2,1,1,2,3,2,1]
y=np.array(y)        
np.unique(y)    #Extrae los valores únicos de y
np.var(y)      #Calcula la varianza de los valores de la lista

##### Pandas #######

#lINK PARA DESCARGAR DATASET:
#https://gist.github.com/netj/8836201

import pandas as pd
df=pd.read_csv("C:/Users/Diego/Downloads/iris.csv")  #Carga de el archivo .csv a dataframe de pandas (Reemplazar dirección)
df

df["variety"]    # o df.variety

df.iloc[0:2,0:3] #dos primeras filas y tres primeras columnas
df.iloc[0:3,:]   #3 primeras filas y todas las columnas
df.loc[0:2,"variety"]  #3 primeras filas y la columna variety 
df.loc[0:2,["sepal.length","variety"]]  #Primeras 3 filas y columnas "sepal.length" y "variety"

df.describe()  #Calcula estadísticos para las variables numéricas
df.corr()   #Calcula la matriz de correlación de las variables numéricas

df["length_width_ratio"]=df["sepal.length"]/df["sepal.width"] #Crea nueva columna con la división de sepal.length y sepal.width

del df["length_width_ratio"]  #Eliminar columna

df.dropna(how="any")  #Elimina registros que tienen NA's
df.drop_duplicates()  #Borra duplicados

#df.to_csv("rut_del_archivo") #Guarda el dataframe en un archivo .csv

##### Matplotlib #######
 #-------Histogramas------------#  
 
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/Diego/Downloads/iris.csv")
plt.hist(df["sepal.width"], bins=25)  #Define el grafo del histograma
plt.title("Histograma Sepal Width")   #Agrega título al gráfico
plt.xlabel("Valor")   #Agrega etiqueta al eje x del gráfico
plt.ylabel("Frecuencia")  #Agrega etiqueta al eje y del gráfico
plt.show()   #Muestra el gráfico

 #-------Scatter plot------------#  
 
import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("C:/Users/Diego/Downloads/iris.csv")
plt.scatter(x="sepal.length", y="sepal.width", data=df)  #Genera un scatter plot de sepal.length y sepal.width
plt.title("Iris Dataset")   #Agrega título al gráfico
plt.xlabel("Sepal Length")  #Agrega etiqueta al eje x del gráfico
plt.ylabel("Sepal Width")  #Agrega etiqueta al eje y del gráfico
plt.show()  #Muestra el gráfico


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