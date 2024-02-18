import base64

from io import BytesIO
import seaborn as sns
import pandas as pd
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

#########################djang框架###############################
import os
import time
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class draw_heat_dq(APIView):
    def get(self, request):
        data1 = pd.read_excel('dq.xlsx')
        # 创建一个示例数据集，包括4个特征和1个目标变量
        data = pd.DataFrame(data1)

        # 计算各个变量之间的相关系数
        corr = data.corr()
        plt.figure(figsize=(10, 6))
        # 绘制热力图，并显示相关系数大小和方向
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title('大庆地区相关性分析热力图')

        # 将图片以二进制的格式传到前端
        sio = BytesIO()
        plt.savefig(sio, format='png')
        data = base64.encodebytes(sio.getvalue()).decode()
        # data=base64.b64encode(sio.getvalue())
        src = 'data:image/png;base64,' + str(data)

        # # 记得关闭，不然画出来的图是重复的
        plt.close()
        # print("src----------------", src)
        return Response({'src': src})


class draw_heat_qq(APIView):
    def get(self, request):
        data1 = pd.read_excel('qq.xlsx')
        # 创建一个示例数据集，包括4个特征和1个目标变量
        data = pd.DataFrame(data1)

        # 计算各个变量之间的相关系数
        corr = data.corr()
        plt.figure(figsize=(10, 6))
        # 绘制热力图，并显示相关系数大小和方向
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title('齐齐哈尔地区相关性分析热力图')

        # 将图片以二进制的格式传到前端
        sio = BytesIO()
        plt.savefig(sio, format='png')
        data = base64.encodebytes(sio.getvalue()).decode()
        # data=base64.b64encode(sio.getvalue())
        src = 'data:image/png;base64,' + str(data)

        # # 记得关闭，不然画出来的图是重复的
        plt.close()
        # print("src----------------", src)
        return Response({'src': src})


class draw_heat_xhy(APIView):
    def get(self, request):
        data1 = pd.read_excel('xhy.xlsx')
        # 创建一个示例数据集，包括4个特征和1个目标变量
        data = pd.DataFrame(data1)

        # 计算各个变量之间的相关系数
        corr = data.corr()
        plt.figure(figsize=(10, 6))
        # 绘制热力图，并显示相关系数大小和方向
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title('小黑杨相关性分析热力图')

        # 将图片以二进制的格式传到前端
        sio = BytesIO()
        plt.savefig(sio, format='png')
        data = base64.encodebytes(sio.getvalue()).decode()
        # data=base64.b64encode(sio.getvalue())
        src = 'data:image/png;base64,' + str(data)

        # # 记得关闭，不然画出来的图是重复的
        plt.close()
        # print("src----------------", src)
        return Response({'src': src})

class draw_heat_hqy(APIView):
    def get(self, request):
        data1 = pd.read_excel('hqy.xlsx')
        # 创建一个示例数据集，包括4个特征和1个目标变量
        data = pd.DataFrame(data1)

        # 计算各个变量之间的相关系数
        corr = data.corr()
        plt.figure(figsize=(10, 6))
        # 绘制热力图，并显示相关系数大小和方向
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title('黑青杨相关性分析热力图')

        # 将图片以二进制的格式传到前端
        sio = BytesIO()
        plt.savefig(sio, format='png')
        data = base64.encodebytes(sio.getvalue()).decode()
        # data=base64.b64encode(sio.getvalue())
        src = 'data:image/png;base64,' + str(data)

        # # 记得关闭，不然画出来的图是重复的
        plt.close()
        # print("src----------------", src)
        return Response({'src': src})

class draw_heat_yzy(APIView):
    def get(self, request):
        data1 = pd.read_excel('yzy.xlsx')
        # 创建一个示例数据集，包括4个特征和1个目标变量
        data = pd.DataFrame(data1)

        # 计算各个变量之间的相关系数
        corr = data.corr()
        plt.figure(figsize=(10, 6))
        # 绘制热力图，并显示相关系数大小和方向
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title('银中杨相关性分析热力图')

        # 将图片以二进制的格式传到前端
        sio = BytesIO()
        plt.savefig(sio, format='png')
        data = base64.encodebytes(sio.getvalue()).decode()
        # data=base64.b64encode(sio.getvalue())
        src = 'data:image/png;base64,' + str(data)

        # # 记得关闭，不然画出来的图是重复的
        plt.close()
        # print("src----------------", src)
        return Response({'src': src})

class draw_heat_qsy(APIView):
    def get(self, request):
        data1 = pd.read_excel('qsy.xlsx')
        # 创建一个示例数据集，包括4个特征和1个目标变量
        data = pd.DataFrame(data1)

        # 计算各个变量之间的相关系数
        corr = data.corr()
        plt.figure(figsize=(10, 6))
        # 绘制热力图，并显示相关系数大小和方向
        sns.heatmap(corr, annot=True, cmap='coolwarm')
        plt.title('青山杨相关性分析热力图')

        # 将图片以二进制的格式传到前端
        sio = BytesIO()
        plt.savefig(sio, format='png')
        data = base64.encodebytes(sio.getvalue()).decode()
        # data=base64.b64encode(sio.getvalue())
        src = 'data:image/png;base64,' + str(data)

        # # 记得关闭，不然画出来的图是重复的
        plt.close()
        # print("src----------------", src)
        return Response({'src': src})