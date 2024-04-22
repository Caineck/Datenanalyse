import pandas as pd
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Datensatz laden
df = pd.read_csv("winequality-white.csv", delimiter=";")

# Ersten 5 und letzten 5 Zeilen ausgeben
print(df.head(5))
print(df.tail(5))

# Überprüfen der Anzahl und Datentypen
print(df.info())

# Überprüfen auf fehlende Werte und ggf. Entfernen oder Ersetzen
print(df.isnull().any())

# Duplikate entfernen
print(df.duplicated())
df = df.drop_duplicates()
print(df.duplicated())

# Dekriptive Statistiken
desk_data = df.describe()
print(desk_data)

# Korrelation
corr = df.corr()
print(corr['quality'].sort_values())

# Histogramm
df['alcohol'].hist()
plt.title('Verteilung des Alkoholgehalts')
plt.show()

# Scatter
plt.scatter(df['alcohol'], df['quality'])
plt.title("Alkohol vs Quali des Weins")
plt.show()

# Boxplot
df.boxplot(column='alcohol', by='quality')
plt.title("Alkoholgehalt nach Weinquali")
plt.show()