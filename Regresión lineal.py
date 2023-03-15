import numpy as np
import pandas as pd
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
from math import sqrt


boston=load_boston()  #Cargar data
X=boston.data    #Extraer Features
Y=boston.target  #Extraer target
print(boston.DESCR)  #Imprimir descripción del dataset

X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size=0.7, random_state=42) #Separar data en train y test

reg=LinearRegression() #Generar el modelo de regresión lineal
reg.fit(X_train,y_train)  #Entrenamiento de la regresión lineal

predicciones=reg.predict(X_test)  #Genero predicciones sobre data de testeo


rmse = sqrt(mean_squared_error(y_test, predicciones)) #Calcular el RMSE

print("RMSE: "+str(rmse*1000)+" dólares")

