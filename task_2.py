# -*- coding: utf-8 -*-
"""Task_2.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1_Iepl1D8ibXi0taqOMaAM9qx7P78M1OR
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

from google.colab import files
uploaded = files.upload()

df = pd.read_csv('titanic_preprocessed.csv')
print(df.head())

# 1. Summary Statistics
print("\nDataset Info:")
print(df.info())

print("\nSummary Statistics:")
print(df.describe())

print("\nMedian Values:")
print(df.median(numeric_only=True))

# 4. identifing patterns,trends, or anomalies in the data

print("\nSkewness:")
print(df.skew(numeric_only=True))

print("\nMissing Values:")
print(df.isnull().sum())

# 2. Histograms
print("\n Histograms for Numeric Features")
df.hist(bins=20, figsize=(15, 10), edgecolor='black')
plt.suptitle("Histograms of Numeric Features")
plt.tight_layout()
plt.show()

# Boxplots for Age and Fare # 4. Boxplots to visualize anomalies and patterns in numerical features
plt.figure(figsize=(12, 6))
sns.boxplot(data=df[['Age', 'Fare']])
plt.title("Boxplots for Age and Fare")
plt.show()

# 3. Correlation Matrix
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Matrix")
plt.show()

#5. Feature Relationships (Pairplots replaced with scatter)
df_cleaned = df.dropna(subset=['Age'])
fig1 = px.scatter(df_cleaned, x='Age', y='Fare', color='Survived', title='Age vs Fare Colored by Survival')
fig1.show()

fig2 = px.scatter(df_cleaned, x='Pclass', y='Fare', color='Survived', title='Pclass vs Fare Colored by Survival')
fig2.show()

# Feature-Level Inference Visuals
plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Sex', hue='Survived')
plt.title("Survival by Gender")
plt.show()
# Inference: Females had higher survival rates.

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Pclass', hue='Survived')
plt.title("Survival by Passenger Class")
plt.show()
# Inference: 1st class passengers had higher survival.

plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='Age', hue='Survived', bins=30, kde=True)
plt.title("Age Distribution by Survival")
plt.show()
# Inference: Younger passengers survived more.

fig3 = px.histogram(df, x="Fare", color="Survived", nbins=50, title="Fare Distribution by Survival")
fig3.show()
# Inference: Higher fare passengers survived more.

plt.figure(figsize=(8, 5))
sns.countplot(data=df, x='Embarked_S', hue='Survived')
plt.title("Survival by Embarked Port (S=1 if Southampton)")
plt.show()
# Inference: Passengers from Southampton had lower survival.

#  Detect Anomalies using filters
print("\nHigh Fare Outliers (Fare > 2.5):")
print(df[df['Fare'] > 2.5][['Fare', 'Survived']])

print("\nElderly Passengers (Age > 2.0):")
print(df[df['Age'] > 2.0][['Age', 'Survived']])

# Multicollinearity Check
print("\nHigh Correlations (> 0.75):")
corr_matrix = df.corr(numeric_only=True)
high_corr = corr_matrix[(corr_matrix > 0.75) & (corr_matrix != 1.0)]
print(high_corr.dropna(how='all').dropna(axis=1, how='all'))