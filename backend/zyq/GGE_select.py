from zyq.GGE import *
class select_for_variety_yield_and_stability(APIView):
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

        file_name = json.loads(request.body)[0].get('name')

        (shotname, extension) = os.path.splitext(str(file_name))

        if shotname == 'scatter_simulation_data' or shotname == 'scatter_real_data':
            return Response({'code': -1})
        if extension == '.xlsx' or extension == '.xls':
            file = os.path.join(f'media/excel/{shotname}{extension}')
            data = pd.read_excel(file)
        if extension == '.csv':
            file = os.path.join(f'media/excel/{shotname}.csv')
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

class select_for_which_won_where(APIView):
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

        file_name = json.loads(request.body)[0].get('name')

        (shotname, extension) = os.path.splitext(str(file_name))
        if shotname == 'scatter_simulation_data' or shotname == 'scatter_real_data':
            return Response({'code': -1})

        if extension == '.xlsx' or extension == '.xls':
            file = os.path.join(f'media/excel/{shotname}{extension}')
            data = pd.read_excel(file)
        if extension == '.csv':
            file = os.path.join(f'media/excel/{shotname}.csv')
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