import pandas as pd
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("diamonds.csv")

data_unknown = data.drop(['cut', 'Unnamed: 0'], axis = 1)
conv_num = ['color', 'clarity']
data_unknown[conv_num] = data_unknown[conv_num].astype('category')
data_unknown[conv_num] = data_unknown[conv_num].apply(lambda x: x.cat.codes)

print(data_unknown.head())

s_scaler = StandardScaler()
data_unknown = pd.DataFrame(s_scaler.fit_transform(data_unknown), columns = data_unknown.columns)

model = KMeans()

visualizer = KElbowVisualizer(model, k=(2,9), timings=False)
visualizer.fit(data_unknown)
visualizer.show()

kmeans = KMeans(n_clusters=4)
pred = kmeans.fit_predict(data_unknown)

data_new = pd.concat([data, pd.DataFrame(pred, columns=['label'])], axis=1)
print(data_new)

#data_new.to_csv('data_new.csv')
