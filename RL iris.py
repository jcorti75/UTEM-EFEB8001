import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

iris=load_iris()  #Cargar data
X=iris.data    #Extraer Features
Y=iris.target  #Extraer target

X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size=0.7, random_state=42) #Separar data en train y test


l_r=LogisticRegression()  #Genera el modelo de regresión logística
l_r.fit(X_train, y_train)  #Entrenamiento del modelo

predicciones=l_r.predict(X_test) #Predicciones sobre la data de testeo

accuracy=accuracy_score(y_test,predicciones) #Cálculo del accuracy
confusion=confusion_matrix(y_test, predicciones) #Cálculo de la matriz de confusión

with open('C:/Users/Diego/Downloads/modelo','wb') as f: #Código para guardar el modelo entrenado
                pickle.dump(l_r, f)
                
with open('C:/Users/Diego/Downloads/modelo','rb') as f: #Código para cargar el modelo entrenado
                lor = pickle.load(f)

print("Accuracy: "+str(accuracy*100)+"%")

confusion=pd.DataFrame(confusion, index=["Setosa", "Versicolor", "Virginica"], columns=["Setosa", "Versicolor", "Virginica"])
confusion #Imprimir la matriz de confusión


