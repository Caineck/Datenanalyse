import pandas as pd
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt


# Datensatz laden
data = pd.read_csv("iris.csv")

# Datensatz aufteilen
setosa = data[data['species']=='Setosa']
versicolor = data[data['species']=='Versicolor']
virginica = data[data['species']=='Virginica']

# Alle drei Unterarten in einem Plot
plt.scatter(setosa['sepal.length'], setosa['sepal.width'], color='red', marker='s')
plt.scatter(versicolor['sepal.length'], versicolor['sepal.width'], color='blue', marker='o')
plt.scatter(virginica['sepal.length'], virginica['sepal.width'], color='green', marker='^')

plt.xlabel('sepal.length')
plt.ylabel('sepal.width')
plt.show()
