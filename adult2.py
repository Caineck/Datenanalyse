import pandas as pd
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Aufgabe 1

# Daten einlesen
path = "/Users/student/Downloads/adult 2.csv"
data = pd.read_csv(path)

# Zeige die ersten 5 und die letzten 5 Zeilen der csv an
print(data.head(5), data.tail(5))

# Zusammenfassung des Datensatzes zu jeder Spalte
print(data.info())

# Aufgabe 2

# Wähle die Spalten age, occupation und income aus und zeige die ersten 10 Zeilen an
slct_clmn = data[['age', 'occupation', 'income']]
print(slct_clmn.head(10))

# Daten filtern und nur Zeilen anzeigen wo income '>50K' ist
filtered_data = data[data['income']=='>50K']
print(filtered_data)

# Alle Einträge finden bei denen das 'age' größer als 30 und die 'education 'Bachelors' ist
thirty_bachelor = data[(data['age']>30) & (data['education']=='Bachelors')]
print(thirty_bachelor)

# Aufgabe 3

# Neue Spalte hinzufügen: Berechen das Alter in Jahrzehnten und füge es in eine neue Spalte
data['age_decade'] = data['age'] / 10
print(data)

# Werte ändern: In 'income'-Spalte die Werte '>50K' und '<=50K' durch 'high' und 'low' ersetzen
changed_income = data['income'].replace({'>50K' : 'high', '<=50K' : 'low'})
print(changed_income)

# Zeilen löschen: Entferne 'occupation' die 'Unknown'
deleted_occupation = data[data['occupation']!='?']
print(deleted_occupation)

# Aufgabe 4

# Deskriptive Statistiken: Zeige die deskriptive Statistiken für die 'age' Spalte an
deskriptive_statistics = data['age'].describe()
print(deskriptive_statistics)

# Gruppierung und Aggregierung: Berechne den Durchschnitt von 'age' gruppiert nach 'income'
group_arregated = data[['age', 'income']]
group_arregated = data.groupby('income')['age'].mean()
print(group_arregated)

# Einzigartige Werte: finde diese in der 'education'-Spalte
unique_values = data['education'].unique()
print(unique_values)

# Aufgabe 5

# Boxplot für 'age' erstellen und nach 'income' gruppieren
#data.groupby('income').boxplot(column='age')
#plt.show()

# Scatterplot erstellen, farbkodiert nach 'income'
plt.scatter(data['age'], data['hours-per-week'], c=data['income'].map({'<=50K': 'blue', '>50K': 'red'}), alpha=0.5)

# Achsentitel hinzufügen
plt.xlabel('Age')
plt.ylabel('Hours-per-week')

# Legende hinzufügen
legend_labels = {'<=50K': 'Income <=50K', '>50K': 'Income >50K'}
plt.legend(handles=[plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=10),
                    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='red', markersize=10)],
           labels=[legend_labels['<=50K'], legend_labels['>50K']])

# Diagramm anzeigen
plt.show()