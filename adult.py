import pandas as pd
from sklearn.cluster import KMeans
from yellowbrick.cluster import KElbowVisualizer
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

path = "/Users/student/Downloads/adult 2.csv"
data = pd.read_csv(path)

print(data.head(5))

conv_num = ['workclass', 'education', 'marital-status', 'occupation',
            'relationship', 'race', 'gender', 'native-country', 'income']
data[conv_num] = data[conv_num].astype('category')
data[conv_num] = data[conv_num].apply(lambda x: x.cat.codes)
print(data[conv_num])

model = KMeans()

visualizer = KElbowVisualizer(model, k=(2,9), timings=False)
visualizer.fit(data)
visualizer.show()

kmeans = KMeans(n_clusters=4)
pred = kmeans.fit_predict(data)

data_new = pd.concat([data, pd.DataFrame(pred, columns=['label'])], axis=1)
print(data_new)

data_new.to_csv('data_new.csv')




