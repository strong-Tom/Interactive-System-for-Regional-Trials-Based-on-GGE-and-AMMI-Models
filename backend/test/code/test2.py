import base64

from io import BytesIO

import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False






data = pd.read_csv('../../ammi_temp_data.csv')
X = data.values
# print(X)
pca = PCA(2)

x_new = pca.fit_transform(X)#3列降维为2列
print(x_new)
print(pca.components_)
place_pc2 = pca.components_[1, :]
#pca.components_ 属性返回一个矩阵，其中每一行表示一个主成分的特征向量。特征向量描述了数据在每个主成分上的贡献程度和方向
print(place_pc2)
place_height = X.mean(axis=0)#每个地点的平均树高
clone_pc2 = x_new[:, 1]
clone_height = X.mean(axis=1)#每个品种的无性系高