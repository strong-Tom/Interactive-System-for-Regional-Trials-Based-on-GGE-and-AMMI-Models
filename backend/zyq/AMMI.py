import base64

from io import BytesIO

import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#########################django框架###############################
import os
import time
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView


class upload_for_ammi(APIView):

    def post(self, request):

        # 标签
        clone_text_size = 9
        clone_text_color = 'black'

        place_text_size = 10
        place_text_color = 'g'
        # 线
        line_color = 'red'
        line_size = 1
        # 点
        clone_scatter_size = 30
        clone_scatter_color = 'orange'
        clone_scatter_mark = 'o'

        place_scatter_size = 50
        place_scatter_color = 'blue'
        place_scatter_mark = '^'

        file = request.data.get('file')
        print(file)
        (shotname, extension) = os.path.splitext(str(file))
        if extension == '.xlsx' or extension == '.xls':
            data = pd.read_excel(file)
        if extension == '.csv':
            data = pd.read_csv(file)

        data.to_csv('ammi_temp_data.csv', index=0)

        X = data.values
        pca = PCA(2)
        x_new = pca.fit_transform(X)
        # print(pca.components_[1:2, :])
        place_pc2 = pca.components_[1:2, :]
        place_height = X.mean(axis=0)

        clone_pc2 = x_new[:, 1]
        clone_height = X.mean(axis=1)

        ys = clone_pc2
        scaley = 1.0 / (ys.max() - ys.min())
        ys *= scaley

        # 无性系散点
        plt.scatter(clone_height, ys, c=clone_scatter_color, marker=clone_scatter_mark, s=clone_scatter_size)
        # 无性系标签
        for i in range(len(X)):
            plt.text(clone_height[i],
                     ys[i],
                     str(i + 1),
                     fontsize=clone_text_size,
                     color=clone_text_color,
                     verticalalignment="top",
                     horizontalalignment="right"
                     )
        # 地点散点
        plt.scatter(place_height, place_pc2, marker=place_scatter_mark, c=place_scatter_color, s=place_scatter_size)
        label = list(data.columns)
        n = data.shape[1]
        for i in range(n):
            # 地点标签
            plt.text(place_height[i] * 0.95, place_pc2[0][i] * 1.05, label[i], color=place_text_color, ha='center',
                     va='center', fontsize=place_text_size)
            # 线模块，plot函数含义是[(x1,x2),(y1,y2)]
            plt.plot([sum(place_height) / len(place_height), place_height[i]], [0, place_pc2[0][i]], c=line_color,
                     linewidth=line_size)

        plt.xlabel('Mean height')
        plt.ylabel('PC1')
        # plt.title("PC1 VS Means")
        # plt.show()

        # 将图片以二进制的格式传到前端
        sio = BytesIO()
        plt.savefig(sio, format='png')
        data = base64.encodebytes(sio.getvalue()).decode()
        # data=base64.b64encode(sio.getvalue())
        src = 'data:image/png;base64,' + str(data)

        # # 记得关闭，不然画出来的图是重复的
        plt.close()

        return Response({'src': src})


class draw_ammi(APIView):
    def post(self, request):

        form = request.data.get('file')
        # 标签
        clone_text_size = form.get('clone_text_size')
        clone_text_color = form.get('clone_text_color')

        place_text_size = form.get('place_text_size')
        place_text_color = form.get('place_text_color')
        # 线
        line_color = form.get('line_color')
        line_size = form.get('line_size')
        # 点
        clone_scatter_size = form.get('clone_scatter_size')
        clone_scatter_color = form.get('clone_scatter_color')
        clone_scatter_mark = form.get('clone_scatter_mark')

        place_scatter_size = form.get('place_scatter_size')
        place_scatter_color = form.get('place_scatter_color')
        place_scatter_mark = form.get('place_scatter_mark')

        # file = request.data.get('file')
        # print(file)
        data = pd.read_csv('ammi_temp_data.csv')

        X = data.values
        pca = PCA(2)
        x_new = pca.fit_transform(X)
        # print(pca.components_[1:2, :])
        place_pc2 = pca.components_[1:2, :]
        place_height = X.mean(axis=0)

        clone_pc2 = x_new[:, 1]
        clone_height = X.mean(axis=1)

        ys = clone_pc2
        scaley = 1.0 / (ys.max() - ys.min())
        ys *= scaley

        # 无性系散点
        plt.scatter(clone_height, ys, c=clone_scatter_color, marker=clone_scatter_mark, s=clone_scatter_size)
        # 无性系标签
        for i in range(len(X)):
            plt.text(clone_height[i],
                     ys[i],
                     str(i + 1),
                     fontsize=clone_text_size,
                     color=clone_text_color,
                     verticalalignment="top",
                     horizontalalignment="right"
                     )
        # 地点散点
        plt.scatter(place_height, place_pc2, marker=place_scatter_mark, c=place_scatter_color, s=place_scatter_size)
        label = list(data.columns)
        n = data.shape[1]
        for i in range(n):
            # 地点标签
            plt.text(place_height[i] * 0.95, place_pc2[0][i] * 1.05, label[i], color=place_text_color, ha='center',
                     va='center', fontsize=place_text_size)
            # 线模块
            plt.plot([sum(place_height) / len(place_height), place_height[i]], [0, place_pc2[0][i]], c=line_color,
                     linewidth=line_size)

        plt.xlabel('Mean height')
        plt.ylabel('PC1')
        # plt.title("PC1 VS Means")
        # plt.show()

        # 将图片以二进制的格式传到前端
        sio = BytesIO()
        plt.savefig(sio, format='png')
        data = base64.encodebytes(sio.getvalue()).decode()
        # data=base64.b64encode(sio.getvalue())
        src = 'data:image/png;base64,' + str(data)

        # # 记得关闭，不然画出来的图是重复的
        plt.close()

        return Response({'src': src})
