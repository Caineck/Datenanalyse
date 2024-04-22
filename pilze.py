import pandas as pd
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from sklearn.preprocessing import StandardScaler

data = pd.read_csv('mushrooms.csv')

data_unknown = data.drop(['class'], axis=1)
data_unknown = data_unknown.astype('category')
data_unknown = data_unknown.apply(lambda x: x.cat.codes)

print(data_unknown)

s_scaler = StandardScaler()
data_unknown = pd.DataFrame(s_scaler.fit_transform(data_unknown), columns = data_unknown.columns)

model = KMeans()

visualizer = KElbowVisualizer(model, k=(1,9), timings=False)
visualizer.fit(data_unknown)
visualizer.show()

kmeans = KMeans(n_clusters=5)
pred = kmeans.fit_predict(data_unknown)

data_new = pd.concat([data, pd.DataFrame(pred, columns=['label'])], axis=1)
print(data_new)
