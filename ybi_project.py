# -*- coding: utf-8 -*-
"""YBI-Project-Placement- Raef Abdul Nazir

Automatically generated by Colaboratory.
# **Project Title:**  Placement prediction
---

**Project by:** Raef Abdul Nazir
(Mar Baselios College of Engineering and Technology, Thiruvananthapuram, Kerala, India)


##### **Dataset Source:** from YBI Foundation (GitHub)

## **Objective:** To predict the Placement of a student based on given parameters

## **Importing Libraries**
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sklearn 
from sklearn import linear_model

"""## **Importing Dataset**"""

d=pd.read_csv('placements.csv',sep=',')
d.shape

dataset=pd.DataFrame(d)

"""## **Exploring Data**"""

dataset.info() #to confirm there are no null or missing values in dataset

"""## **Visulaizing Data using Matplotlib**"""

dataset.plot(kind='scatter',x='Placement',y='CGPA')
plt.show()

dataset.plot(kind='scatter',x='Placement',y='IQ',color='green')
plt.show()

"""## **Importing Libraries**"""

dataset.head(10)

dataset['Placement'].value_counts() #to check whether there is equal distribution of values

dataset.groupby('Placement').mean()

"""## **Define Target Variable y and Feature variables x**"""

x=dataset.drop(['Student_ID','Placement'], axis = 1)
y=dataset['Placement']

"""## **Standardize x values**"""

#this is done, since there are various ranges of data and scaling is required for correct predictions
from sklearn.preprocessing import StandardScaler
ssc=StandardScaler() #used to scale data of different ranges
x=ssc.fit_transform(x)
x

"""## **Train Test Split the Data**"""

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y,stratify=y, test_size = 0.3,random_state=192529)
'''
stratify: preserves proportion of target variable
random_state: used for initializing the internal random number generator, 
              which will decide the splitting of data into train and test indices
'''

"""## **Create the Prediction Model and finding its accuracy**"""

from sklearn.linear_model import LogisticRegression
Model = linear_model.LogisticRegression()
Model.fit(x_train, y_train) 
accuracy = Model.score(x_test, y_test)
print("Model is at",accuracy*100,"% Accuracy")

"""## **Predicted values vs. Actual Values**"""

predictions = Model.predict(x_test)
print('y_test:\n',y_test)
print('predictions: ',predictions)

#y_test is a series... so in order to get the predicted values we use seriesname.values
for i in range(len(predictions)):
  print("Model Predicted :",predictions[i],"  Actual value : ",y_test.values[i])

"""## **Model Evaluation**"""

from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(y_test,predictions))

print(classification_report(y_test,predictions))

"""## **Future Predictions**

here a random value is selected from the dataset as a new value so that we can make prediction.



Steps followed here are:
1.   extracted x and y, using random.randrange() to generate an index to select a random row from dataframe, then we use sample()
2.   separated x and y
3.   standardize x
4.   make prediction
"""

x_new=dataset.sample(1) #sample(1) generates 1 random row
x_new

x_new=x_new.drop(['Student_ID','Placement'], axis = 1)
x_new

#scaling x_new
x_new=ssc.fit_transform(x_new)
x_new

new_prediction=Model.predict(x_new)
new_prediction

"""## **Explanation**

---
####This is a project aimed to predict the placement of a student with given parameters.It was implemented using **Logistic Regression**. Through the project I have learnt how to visualize data, create a model by splitting data using sklearn and create its confusion matrix and classification report, and to generate future predictions using the created model. Many new functions were also introduced in this project.

"""
