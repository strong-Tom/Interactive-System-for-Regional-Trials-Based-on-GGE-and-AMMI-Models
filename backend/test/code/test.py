
import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
from sklearn.decomposition import PCA


def biplot(clone_text_size, clone_text_color, place_text_size, place_text_color, clone_scatter_size,
           clone_scatter_color, clone_scatter_mark, place_scatter_mark, place_scatter_color,
           place_scatter_size, X, score, coeff, labels=None):
    #score是pca降维后的数据，coeff是
    xs = score[:, 0]
    ys = score[:, 1]
    n = coeff.shape[0]
    # print(xs,ys)
    scalex = 1.0 / (xs.max() - xs.min())
    scaley = 1.0 / (ys.max() - ys.min())
    # 无性系散点
    plt.scatter(xs * scalex, ys * scaley, c=clone_scatter_color, marker=clone_scatter_mark,
                s=clone_scatter_size)
    x1 = xs * scalex
    y1 = ys * scaley

    for i in range(n):
        # plt.arrow(0, 0, coeff[i, 0], coeff[i, 1], color='r', alpha=0.5)
        # 地点散点
        plt.scatter(coeff[i, 0], coeff[i, 1], marker=place_scatter_mark, c=place_scatter_color,
                    s=place_scatter_size)

    return x1, y1
# 标签
clone_text_size = 9
clone_text_color = '#121214'  # black

place_text_size = 10
place_text_color = '#F20909'  # red
# 线
vertical_line_color = '#4716E7'  # purple
vertical_line_size = 1
encircle_line_color = '#121214'  # black
encircle_line_size = 1
# 点
clone_scatter_size = 30
clone_scatter_color = '#15F209'  # green
clone_scatter_mark = 'o'

place_scatter_size = 50
place_scatter_color = '#0D5CEF'  # blue
place_scatter_mark = '^'

data = pd.read_csv('../../gge_temp_data.csv')
X = data.values

pca = PCA(2)
x_new = pca.fit_transform(X)

plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('Which won Where')
# Call the function. Use only the 2 PCs,x1,y1为缩放后的散点图坐标
x1, y1 = biplot(clone_text_size, clone_text_color, place_text_size, place_text_color, clone_scatter_size,
                clone_scatter_color, clone_scatter_mark, place_scatter_mark, place_scatter_color,
                place_scatter_size, data, x_new[:, 0:2], np.transpose(pca.components_[0:2, :]),
                labels=list(data.columns))


plt.axis("equal")
plt.xlim(-1, 1)
plt.ylim(-1, 1)
plt.show()

#查看数据
# print("x_new is",x_new)
# print("x_new[:, 0:2] is",x_new[:, 0:2])
# print(np.transpose(pca.components_[0:2, :]))
# print(pca.components_[0:2,:])
print(pca.components_)