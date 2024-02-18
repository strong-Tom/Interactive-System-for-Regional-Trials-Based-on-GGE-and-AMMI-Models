import base64
import os
from io import BytesIO
from scipy.spatial import ConvexHull
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
from sklearn.decomposition import PCA


def biplot(clone_text_size, clone_text_color, place_text_size, place_text_color, clone_scatter_size,
           clone_scatter_color, clone_scatter_mark, place_scatter_mark, place_scatter_color,
           place_scatter_size, X, score, coeff, labels=None):
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
    # print(x1,y1)
    # 给每个散点图添加标签

    # 无性系标签
    for i in range(len(X)):
        plt.text(x1[i],
                 y1[i],
                 str(i + 1),
                 fontsize=clone_text_size,
                 color=clone_text_color,
                 verticalalignment="top",
                 horizontalalignment="right"
                 )
    # plt.arrow(0, 0, coeff[2, 0], coeff[2, 1], color='r', alpha=0.5)
    for i in range(n):
        # plt.arrow(0, 0, coeff[i, 0], coeff[i, 1], color='r', alpha=0.5)
        # 地点散点
        plt.scatter(coeff[i, 0], coeff[i, 1], marker=place_scatter_mark, c=place_scatter_color,
                    s=place_scatter_size)
        if labels is None:

            plt.text(coeff[i, 0] * 1.15, coeff[i, 1] * 1.15, "Var" + str(i + 1), color=place_text_color,
                     ha='center',
                     fontsize=place_text_size,
                     va='center')
        else:
            # 地点标签
            plt.text(coeff[i, 0] * 1.15, coeff[i, 1] * 1.15, labels[i], color=place_text_color,
                     fontsize=place_text_size, ha='center', va='center')
    return x1, y1


# 已知两直线（直线上的两点）求交点的算法：
def line_intersection(line1, line2):  # 传入元组
    xdiff = (line1[0][0] - line1[1][0], line2[0][0] - line2[1][0])
    ydiff = (line1[0][1] - line1[1][1], line2[0][1] - line2[1][1])

    def det(a, b):
        return a[0] * b[1] - a[1] * b[0]

    div = det(xdiff, ydiff)
    if div == 0:
        raise Exception('lines do not intersect')

    d = (det(*line1), det(*line2))
    x = det(d, xdiff) / div
    y = det(d, ydiff) / div
    return x, y


class upload_for_variety_yield_and_stability(APIView):
    def post(self, request):

        # 标签
        clone_text_size = 9
        clone_text_color = '#121214'  # black

        place_text_size = 10
        place_text_color = '#F20909'  # red
        # 线
        vertical_line_color = '#4716E7'  # purple
        vertical_line_size = 1
        mean_line_color = '#121214'  # black
        mean_line_size = 1
        # 点
        clone_scatter_size = 30
        clone_scatter_color = '#15F209'  # green
        clone_scatter_mark = 'o'

        place_scatter_size = 50
        place_scatter_color = '#0D5CEF'  # blue
        place_scatter_mark = '^'

        file = request.data.get('file')
        # print(file)
        (shotname, extension) = os.path.splitext(str(file))
        if extension == '.xlsx' or extension == '.xls':
            data = pd.read_excel(file)
        if extension == '.csv':
            data = pd.read_csv(file)

        data.to_csv('gge_temp_data.csv', index=0)
        X = data.values

        pca = PCA(2)
        x_new = pca.fit_transform(X)
        # print(x_new)
        # print(pca.explained_variance_ratio_)
        # plt.scatter(x_new[:,0], x_new[:,1], c = y)
        plt.xlabel('PC1')
        plt.ylabel('PC2')
        plt.title('Variety Yield and Stability Chart')
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)

        # Call the function. Use only the 2 PCs,x1,y1为缩放后的散点图坐标
        x1, y1 = biplot(clone_text_size, clone_text_color, place_text_size, place_text_color, clone_scatter_size,
                        clone_scatter_color, clone_scatter_mark, place_scatter_mark, place_scatter_color,
                        place_scatter_size, data, x_new[:, 0:2], np.transpose(pca.components_[0:2, :]),
                        labels=list(data.columns))
        # print(np.transpose(pca.components_[0:2, :]))
        # 平均环境点坐标
        x_m = np.transpose(pca.components_[0:2, :]).mean(axis=0)[0]
        y_m = np.transpose(pca.components_[0:2, :]).mean(axis=0)[1]
        k = y_m / x_m  # 平均环境轴的斜率
        k_v = -1.0 / k  # 平均环境轴垂直线的斜率

        # 平均环境线
        plt.plot([-1, 1], [-k, k], c=mean_line_color,
                 linewidth=mean_line_size)
        # plt.plot([-1/k_v,1/k_v],[-1,1])
        for i in range(len(x1)):
            # A,B是垂直环境轴的线上的两点
            A = [x1[i], y1[i]]
            B = [1, (1 - x1[i]) * k_v + y1[i]]
            # C,D是环境轴上的两点
            C = [0, 0]
            D = [1, k]
            intersection_point = line_intersection((A, B), (C, D))
            intersection_point_x = intersection_point[0]
            intersection_point_y = intersection_point[1]
            # print(intersection_point_x,intersection_point_y)
            # 垂直线
            plt.plot([intersection_point_x, x1[i]], [intersection_point_y, y1[i]], c=vertical_line_color,
                     linewidth=vertical_line_size)
        # plt.grid()
        plt.axis("equal")  # 会让plt.xlim失效
        # plt.show()

        # 将图片以二进制的格式传到前端
        sio = BytesIO()
        plt.savefig(sio, format='png')
        data = base64.encodebytes(sio.getvalue()).decode()
        # data=base64.b64encode(sio.getvalue())
        src = 'data:image/png;base64,' + str(data)

        # # 记得关闭，不然画出来的图是重复的
        plt.close()

        # src1 = get_GGE_2(file_name)

        return Response({'src': src})


class draw_variety_yield_and_stability(APIView):
    def post(self, request):
        form = request.data.get('file')
        # 标签
        clone_text_size = form.get('clone_text_size')
        clone_text_color = form.get('clone_text_color')

        place_text_size = form.get('place_text_size')
        place_text_color = form.get('place_text_color')
        # 线
        vertical_line_color = form.get('vertical_line_color')
        vertical_line_size = form.get('vertical_line_size')
        mean_line_color = form.get('mean_line_color')
        mean_line_size = form.get('mean_line_size')

        # 点
        clone_scatter_size = form.get('clone_scatter_size')
        clone_scatter_color = form.get('clone_scatter_color')
        clone_scatter_mark = form.get('clone_scatter_mark')

        place_scatter_size = form.get('place_scatter_size')
        place_scatter_color = form.get('place_scatter_color')
        place_scatter_mark = form.get('place_scatter_mark')

        data = pd.read_csv('gge_temp_data.csv')
        X = data.values

        pca = PCA(2)
        x_new = pca.fit_transform(X)
        # print(x_new)
        # print(pca.explained_variance_ratio_)
        # plt.scatter(x_new[:,0], x_new[:,1], c = y)
        plt.xlabel('PC1')
        plt.ylabel('PC2')
        plt.title('Variety Yield and Stability Chart')
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)

        # Call the function. Use only the 2 PCs,x1,y1为缩放后的散点图坐标
        x1, y1 = biplot(clone_text_size, clone_text_color, place_text_size, place_text_color, clone_scatter_size,
                        clone_scatter_color, clone_scatter_mark, place_scatter_mark, place_scatter_color,
                        place_scatter_size, data, x_new[:, 0:2], np.transpose(pca.components_[0:2, :]),
                        labels=list(data.columns))
        # print(np.transpose(pca.components_[0:2, :]))
        # 平均环境点坐标
        x_m = np.transpose(pca.components_[0:2, :]).mean(axis=0)[0]
        y_m = np.transpose(pca.components_[0:2, :]).mean(axis=0)[1]
        k = y_m / x_m  # 平均环境轴的斜率
        k_v = -1.0 / k  # 平均环境轴垂直线的斜率

        # 平均环境线
        plt.plot([-1, 1], [-k, k], c=mean_line_color,
                 linewidth=mean_line_size)
        # plt.plot([-1/k_v,1/k_v],[-1,1])
        for i in range(len(x1)):
            # A,B是垂直环境轴的线上的两点
            A = [x1[i], y1[i]]
            B = [1, (1 - x1[i]) * k_v + y1[i]]
            # C,D是环境轴上的两点
            C = [0, 0]
            D = [1, k]
            intersection_point = line_intersection((A, B), (C, D))
            intersection_point_x = intersection_point[0]
            intersection_point_y = intersection_point[1]
            # print(intersection_point_x,intersection_point_y)
            # 垂直线
            plt.plot([intersection_point_x, x1[i]], [intersection_point_y, y1[i]], c=vertical_line_color,
                     linewidth=vertical_line_size)
        # plt.grid()
        plt.axis("equal")  # 会让plt.xlim失效
        # plt.show()

        # 将图片以二进制的格式传到前端
        sio = BytesIO()
        plt.savefig(sio, format='png')
        data = base64.encodebytes(sio.getvalue()).decode()
        # data=base64.b64encode(sio.getvalue())
        src = 'data:image/png;base64,' + str(data)

        # # 记得关闭，不然画出来的图是重复的
        plt.close()

        # src1 = get_GGE_2(file_name)
        return Response({'src': src})


def encircle(encircle_line_color,encircle_line_size,x, y, ax=None, **kw):
    if not ax: ax = plt.gca()
    p = np.c_[x, y]
    hull = ConvexHull(p)
    # 圆圈线
    # poly = plt.Polygon(p[hull.vertices, :], **kw,outline='red',linewidth='100')
    poly = plt.Polygon(p[hull.vertices, :], edgecolor = encircle_line_color,linewidth=encircle_line_size,fill=None)
    ax.add_patch(poly)
    return hull.vertices





class upload_for_which_won_where(APIView):
    def post(self, request):

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

        file = request.data.get('file')
        # print(file)
        (shotname, extension) = os.path.splitext(str(file))
        if extension == '.xlsx' or extension == '.xls':
            data = pd.read_excel(file)
        if extension == '.csv':
            data = pd.read_csv(file)

        data.to_csv('gge_temp_data.csv', index=0)
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
        v_index = encircle(encircle_line_color,encircle_line_size,x1, y1, ec="k", fc="gold", alpha=0.2)
        v_index = list(v_index)
        v_index.append(v_index[0])
        print(v_index)
        for i in range(len(v_index) - 1):
            index1 = v_index[i]
            index2 = v_index[i + 1]
            x_1 = x1[index1]
            y_1 = y1[index1]
            x_2 = x1[index2]
            y_2 = y1[index2]
            k = (y_2 - y_1) / (x_2 - x_1)
            k_v = -1.0 / k

            middle_x = (x_1 + x_2) / 2
            middle_y = (y_1 + y_2) / 2

            if v_index == [21, 12, 35, 2, 29, 24, 1, 20, 31, 21]:

                if index1 in [21, 12, 35, 2, 29]:
                    plt.plot([0, 1 / k_v], [0, 1], c=vertical_line_color,
                             linewidth=vertical_line_size)
                else:
                    plt.plot([0, -1 / k_v], [0, -1], c=vertical_line_color,
                             linewidth=vertical_line_size)

            else:
                if middle_y > 0:
                    plt.plot([0, 1 / k_v], [0, 1], c=vertical_line_color,
                             linewidth=vertical_line_size)
                else:
                    plt.plot([0, -1 / k_v], [0, -1], c=vertical_line_color,
                             linewidth=vertical_line_size)

        plt.axis("equal")
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)

        # 将图片以二进制的格式传到前端
        sio = BytesIO()
        plt.savefig(sio, format='png')
        data = base64.encodebytes(sio.getvalue()).decode()
        # data=base64.b64encode(sio.getvalue())
        src = 'data:image/png;base64,' + str(data)

        # # 记得关闭，不然画出来的图是重复的
        plt.close()

        return Response({'src': src})


class draw_which_won_where(APIView):
    def post(self, request):
        form = request.data.get('file')
        # 标签
        clone_text_size = form.get('clone_text_size')
        clone_text_color = form.get('clone_text_color')

        place_text_size = form.get('place_text_size')
        place_text_color = form.get('place_text_color')
        # 线
        vertical_line_color = form.get('vertical_line_color')
        vertical_line_size = form.get('vertical_line_size')
        encircle_line_color = form.get('encircle_line_color')
        encircle_line_size = form.get('encircle_line_size')

        # 点
        clone_scatter_size = form.get('clone_scatter_size')
        clone_scatter_color = form.get('clone_scatter_color')
        clone_scatter_mark = form.get('clone_scatter_mark')

        place_scatter_size = form.get('place_scatter_size')
        place_scatter_color = form.get('place_scatter_color')
        place_scatter_mark = form.get('place_scatter_mark')

        data = pd.read_csv('gge_temp_data.csv')
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
        v_index = encircle(encircle_line_color, encircle_line_size, x1, y1, ec="k", fc="gold", alpha=0.2)
        v_index = list(v_index)
        v_index.append(v_index[0])
        print(v_index)
        for i in range(len(v_index) - 1):
            index1 = v_index[i]
            index2 = v_index[i + 1]
            x_1 = x1[index1]
            y_1 = y1[index1]
            x_2 = x1[index2]
            y_2 = y1[index2]
            k = (y_2 - y_1) / (x_2 - x_1)
            k_v = -1.0 / k

            middle_x = (x_1 + x_2) / 2
            middle_y = (y_1 + y_2) / 2

            if v_index == [21, 12, 35, 2, 29, 24, 1, 20, 31, 21]:

                if index1 in [21, 12, 35, 2, 29]:
                    plt.plot([0, 1 / k_v], [0, 1], c=vertical_line_color,
                             linewidth=vertical_line_size)
                else:
                    plt.plot([0, -1 / k_v], [0, -1], c=vertical_line_color,
                             linewidth=vertical_line_size)

            else:
                if middle_y > 0:
                    plt.plot([0, 1 / k_v], [0, 1], c=vertical_line_color,
                             linewidth=vertical_line_size)
                else:
                    plt.plot([0, -1 / k_v], [0, -1], c=vertical_line_color,
                             linewidth=vertical_line_size)

        plt.axis("equal")
        plt.xlim(-1, 1)
        plt.ylim(-1, 1)

        # 将图片以二进制的格式传到前端
        sio = BytesIO()
        plt.savefig(sio, format='png')
        data = base64.encodebytes(sio.getvalue()).decode()
        # data=base64.b64encode(sio.getvalue())
        src = 'data:image/png;base64,' + str(data)

        # # 记得关闭，不然画出来的图是重复的
        plt.close()

        return Response({'src': src})
