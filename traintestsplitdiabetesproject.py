# -*- coding: utf-8 -*-
"""TrainTestSplitDiabetesPROJECT.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1X146PwLW2YsyxK50tlNKZ_p6fXGEGSRY

Importing the Dependencies
"""

import numpy as np# used to make numpy array very helpful in processing
import pandas as pd# mainly useful for creating dataFrame (input data into a nice structure table)
from sklearn.preprocessing import StandardScaler#used to standardize the data
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score

"""Data Collection and Analysis"""

# loading the diabetes dataset to a pandas DataFrame
diabetes_dataset = pd.read_csv('/content/diabetes.csv')

# printing the first 5 rows of the dataFrame
 diabetes_dataset.head()

#number of rows and columns in this dataset
diabetes_dataset.shape

#getting the statistical measures of the data
diabetes_dataset.describe()

diabetes_dataset['Outcome'].value_counts()

"""0---->Non-Diabetic
1--->Diabetic
"""

diabetes_dataset.groupby('Outcome').mean()

#separating the data and labels
X = diabetes_dataset.drop(columns='Outcome',axis=1)  #droping columns(1 ), if droping row then 0
Y = diabetes_dataset['Outcome'] #storing in variable Y

print(X)

print(Y)

"""Data Standardization"""

scaler = StandardScaler()

scaler.fit(X)

standardized_data = scaler.transform(X)

print(standardized_data)

X = standardized_data
Y = diabetes_dataset['Outcome']

print(X)
print(Y)

#Train Test Split
X_train , X_test, Y_train ,Y_test = train_test_split(X,Y,test_size = 0.2,stratify=Y,random_state=2)#stratify so that similar case of diabates and non-diabtes, random_state splitting of the data

print(X.shape,X_train.shape,X_test.shape)

"""Training the Model"""

classifier = svm.SVC(kernel='linear')   #svm to load support vector machine  #SVC represent support vector classifier, linerar model

#training the support vector Machine Classifier
classifier.fit(X_train,Y_train)

"""Model Evalution

Accuracy Score
"""

#accuracy score on the training data
X_train_prediction = classifier.predict(X_train)
training_data_accuracy = accuracy_score(X_train_prediction,Y_train)

print('Accuracy score of the training data : ',training_data_accuracy)

#accuracy score on the text data
X_test_prediction = classifier.predict(X_test)
test_data_accuracy = accuracy_score(X_test_prediction,Y_test)

print('Accuracy score of the test data: ',test_data_accuracy)

"""Making  a Predictive System"""

import numpy as np

input_data = (4, 110, 92, 0, 0, 37.6, 0.191, 30)

# Changing the input_data to a numpy array
input_data_as_numpy_array = np.asarray(input_data)

# Reshape the array as we are predicting for one instance      #to see that only one array is reshaped
input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)

# Standardize the input data
std_data = scaler.transform(input_data_reshaped)

print(std_data)

# Predict using the classifier
prediction = classifier.predict(std_data)  # Fixed the typo (st_data → std_data)

print(prediction)

if prediction[0] == 0:
    print('The person is not diabetic')
else:
    print('The person is diabetic')

