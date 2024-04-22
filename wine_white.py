import pandas as pd
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

#Datensatz laden
df = pd.read_csv("winequality-white.csv", delimiter=";")

# Nichtnumerisch in numerische Werte
data_unknown = df
data_unknown = data_unknown.astype("category")
data_unknown = data_unknown.apply(lambda x: x.cat.codes)

# Kelbow verwenden um Anzahl der Gruppen zu erhalten
model = KMeans()

visualizer = KElbowVisualizer(model, k=(2,9), timings=False)
visualizer.fit(data_unknown)
visualizer.show()

kMeans = KMeans(n_clusters=4)