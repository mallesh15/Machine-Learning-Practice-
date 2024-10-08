# -*- coding: utf-8 -*-
"""Untitled16.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_kkZVr6cYXLJYh53v68U3YQUGg2M6yS9
"""

import numpy as np
import pandas as pd

missing_value = ['NAN', 'N/a','na', np.nan]
data = pd.read_csv("/content/healthcare_datasets.csv", na_values=missing_value)
data.head()

data.info()

data.isnull().sum()

duplicate = data.duplicated().sum()
print(duplicate)

data.drop_duplicates(inplace=True)

duplicate = data.duplicated().sum()
print(duplicate)

data.isnull().sum()

data.dropna(subset=['Patient_ID'], inplace=True)

data.isnull().sum()

data.dropna(subset=['Gender'], inplace=True)

data.isnull().sum()

data.info()

data.fillna(method='ffill', inplace=True)

data.isnull().sum()

data.head()

from matplotlib import pyplot as plt
import seaborn as sns

sns.boxplot(x=data['Age'])

sns.boxplot(x=data['Blood_Pressure'])

sns.boxplot(x=data['Cholesterol'])

data1 = data.copy()

from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
numarical_values = ['Age', 'Blood_Pressure', 'Cholesterol']
data1[numarical_values] = scaler.fit_transform(data1[numarical_values])

print('After Scaling')
data1.head()

categorical_values = ['Gender', 'Patient_ID', 'Condition']
label_encoder = LabelEncoder()
data1[categorical_values] = data1[categorical_values].apply(label_encoder.fit_transform)

print('After Encoding')
data1.head()