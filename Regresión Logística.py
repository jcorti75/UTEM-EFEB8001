import numpy as np
import pandas as pd
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, confusion_matrix

cancer=load_breast_cancer()  #Cargar data
X=cancer.data    #Extraer Features
Y=cancer.target  #Extraer target
print(cancer.DESCR)  #Imprimir descripción del dataset

X_train, X_test, y_train, y_test = train_test_split(X, Y, train_size=0.7, random_state=42) #Separar data en train y test


l_r=LogisticRegression()  #Genera el modelo de regresión logística
l_r.fit(X_train, y_train)  #Entrenamiento del modelo

predicciones=l_r.predict(X_test) #Predicciones sobre la data de testeo

accuracy=accuracy_score(y_test,predicciones) #Cálculo del accuracy
precision=precision_score(y_test,predicciones) #Cálculo del precision
recall=recall_score(y_test,predicciones) #Cálculo del recall
confusion=confusion_matrix(y_test, predicciones) #Cálculo de la matriz de confusión

print("Accuracy: "+str(accuracy*100)+"%")
print("Precision: "+str(precision*100)+"%")
print("Recall: "+str(recall*100)+"%")

confusion=pd.DataFrame(confusion, columns=["predicted.no","predicted.yes"], index=["real.no","real.yes"])
confusion #Imprimir la matriz de confusión

