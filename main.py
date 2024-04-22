import pandas as pd
from matplotlib import pyplot as plt

# Datensatz laden
df = pd.read_csv("iris.csv")

# Datensatz erkunden, ersten Zeilen anzeigen
print(df.head())
print(df.tail())

# Zusammenfassung des DataFrames mit Informationen zu jeder Spalte
print(df.info())

# 20 Mal '#' ausgeben
print("#" * 20)

# Spalten auswählen und die ersten 10 Zeilen anzeigen lassen
selected_columns = df[['sepal.length', 'sepal.width']]
print(selected_columns.head(10))

# Nur Zeilen mit 'setosa' anzeigen
setosa = df[df['species'] =='Setosa']
print(setosa)

# Alle Einträge 'petal.length'>1.5 und 'species' = 'Versicolor'
versicolor = df[(df['petal.length']>1.5) & (df['species']=='Versicolor')]
print(versicolor)

# Fläche berechnen und als neue Spalte hinzufügen
df['sepal.area'] = df['sepal.length'] * df['sepal.width']
print(df)

# Werte ändern, 'Setosa' zu 'S' usw...
changed_species = df['species'].replace({'Setosa' : 'S', 'Versicolor' : 'Ve', 'Virginica': 'Vi'})
print(changed_species)

# Löschen der Zeilen bei denen 'sepal.length'<4.5
deleted_lines = df[df['sepal.length']<4.5]
print(deleted_lines)

# Deskriptive Statistiken für numerische Spalten anzeigen (min, max)
numeric_stats = df.describe().loc[['min', 'max']]
print(numeric_stats)

# Durchschnitt von 'sepal.length' gruppiert nach 'species'
average_sepal_length = df.groupby('species')['sepal.length'].mean()
print(average_sepal_length)

# Einzigartige Werte der Spalte 'species' finden
unique_species = df['species'].unique()
print(unique_species)

# Scatter plot erstellen farbkodiert nach 'species'
plt.scatter(df['sepal.length'], df['sepal.width'])
plt.xlabel('sepal.length')
plt.ylabel('sepal.width')
plt.show()

setosa = df[df['species']=='Setosa']
versicolor = df[df['species']=='Versicolor']
virginica = df[df['species']=='Virginica']

plt.scatter(setosa['sepal.length'], setosa['sepal.width'], color = 'red', marker='s')
plt.scatter(versicolor['sepal.length'], versicolor['sepal.width'], color = 'blue', marker='o')
plt.scatter(virginica['sepal.length'], virginica['sepal.width'], color = 'green',marker='^')
plt.xlabel('sepal.length')
plt.ylabel('sepal.width')
plt.show()
