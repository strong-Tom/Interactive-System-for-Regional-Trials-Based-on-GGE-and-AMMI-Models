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
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False


class draw_box_plot_dq(APIView):
    def get(self, request):
        data = [[16.4,
                 12.9,
                 11.5,
                 ],
                [16.8,
                 17.1,
                 15.9,
                 ],
                [21.3,
                 13.9,
                 15.8,
                 ],
                [18.9,
                 18.6,
                 17.5,
                 ]]

        # 绘制箱型图
        plt.boxplot(data)

        # 修改 x 轴上的类别
        plt.xticks([1, 2, 3, 4], ['小黑杨', '龙丰一号', '2111杨', '青山杨'])

        # 添加标题和轴标签
        plt.title('大庆样地杨树品种平均胸径')
        plt.xlabel('杨树品种')

        plt.ylabel('胸径（cm）')
        # 显示图表
        # plt.show()

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


class draw_box_plot_qq(APIView):
    def get(self, request):
        data = [[14.9,
                 12.85,
                 14.7,

                 ],
                [18.15,
                 20.5,
                 18.8,

                 ],
                ]

        # 绘制箱型图
        plt.boxplot(data)

        # 修改 x 轴上的类别
        plt.xticks([1, 2], ['小黑杨', '青山杨'])

        # 添加标题和轴标签
        plt.title('齐齐哈尔样地杨树品种平均胸径')
        plt.xlabel('杨树品种')

        plt.ylabel('胸径（cm）')

        # 显示图表
        # plt.show()

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
