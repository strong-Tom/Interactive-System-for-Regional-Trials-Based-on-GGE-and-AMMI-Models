import random

from django.db.models import Q
from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView

from backend import settings
from . import models
from .models import Blog, treeTmp, SaveFile, lineChart, pieChart, rule_table, decisionTree_img
from .models import forset
from .models import poplar
from .models import regional_sample
from .models import video,Qx
from .serializers import BlogSerializer, QxSerializer
from .serializers import forsetSerializer
from .serializers import poplarSerializer
from .serializers import regional_sampleSerializer, treeTmpSerializer, userSerializer, SaveFileSerializer, \
    lineChartSerializer, pieChartSerializer, rule_tableSerializer, decisionTree_imgSerializer
from .serializers import videoSerializer


# Create your views here.


class MyPagination(PageNumberPagination):
    page_size = 10

    page_query_param = "page"

    page_size_query_param = "size"

    max_page_size = 100


class BlogViewSet(viewsets.ModelViewSet):
    pagination_class = MyPagination
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class QxViewSet(viewsets.ModelViewSet):
    # pagination_class = MyPagination
    queryset = Qx.objects.all()
    serializer_class = QxSerializer




class regional_sampleViewSet(viewsets.ModelViewSet):
    pagination_class = MyPagination
    queryset = regional_sample.objects.all()
    serializer_class = regional_sampleSerializer


class forsetViewSet(viewsets.ModelViewSet):
    pagination_class = MyPagination
    queryset = forset.objects.all()
    serializer_class = forsetSerializer


class poplarViewSet(viewsets.ModelViewSet):
    pagination_class = MyPagination
    queryset = poplar.objects.all()
    serializer_class = poplarSerializer


class tree1ViewSet(viewsets.ModelViewSet):
    # pagination_class = MyPagination
    queryset = poplar.objects.all()
    serializer_class = poplarSerializer


class videoViewSet(viewsets.ModelViewSet):
    # pagination_class = MyPagination
    queryset = video.objects.all()
    serializer_class = videoSerializer


class treeTmpViewSet(viewsets.ModelViewSet):
    pagination_class = MyPagination
    queryset = treeTmp.objects.all()
    serializer_class = treeTmpSerializer


class SaveFileViewSet(viewsets.ModelViewSet):
    queryset = SaveFile.objects.all()
    serializer_class = SaveFileSerializer


class lineChartViewSet(viewsets.ModelViewSet):
    queryset = lineChart.objects.all()
    serializer_class = lineChartSerializer


class pieChartViewSet(viewsets.ModelViewSet):
    queryset = pieChart.objects.all()
    serializer_class = pieChartSerializer


class rule_tableViewSet(viewsets.ModelViewSet):
    queryset = rule_table.objects.all()
    serializer_class = rule_tableSerializer


class decisionTree_imgViewSet(viewsets.ModelViewSet):
    queryset = decisionTree_img.objects.all()
    serializer_class = decisionTree_imgSerializer


class EvaluateFileUploadView(APIView):
    def save_file(self, file):
        print(type(file))
        filename = file.name
        temp = settings.MEDIA_ROOT + '\\video\\'
        filepath = os.path.join(temp, filename)

        with open(filepath, 'wb') as fp:
            for chunk in file.chunks():
                fp.write(chunk)
        return self.request.build_absolute_uri(settings.MEDIA_URL + 'video/' + filename)

    def post(self, request):
        file = request.data.get('file')
        file_url = self.save_file(file)

        models.video.objects.create(
            video='video/' + file.name,
            name=file.name
        )
        return Response({"file": file_url})


class videoSearch(APIView):

    def get(self, request):
        work = request.GET.get('work', None)

        goodslist = video.objects.filter(Q(name__icontains=work))

        # ser = GoodsSer(goodslist, many=True)
        ser = videoSerializer(goodslist, many=True, context={'request': request})

        return Response(ser.data)


class login(APIView):

    def post(self, request):

        email = json.loads(request.body).get('email')
        password = json.loads(request.body).get('password')

        user = models.user.objects.filter(email__exact=email, password__exact=password)
        ser = userSerializer(user, many=True, context={'request': request})
        if user:
            return Response({'code': 0, 'user': ser.data})
        else:
            return Response({'code': -1, })


class register(APIView):

    def post(self, request):
        e = json.loads(request.body).get('email')
        p = json.loads(request.body).get('password')
        u = json.loads(request.body).get('username')

        user = models.user.objects.filter(email__exact=e)
        if user:
            return Response(-1)
        else:
            models.user.objects.create(
                username=u,
                email=e,
                password=p,
            )
            return Response(0)


class modifyUser(APIView):

    def post(self, request):
        # ����json���ݵķ�ʽ
        formData = json.loads(request.body).get('formData')
        email = formData.get('email')
        phone = formData.get('phone')
        sex = formData.get('sex')
        username = formData.get('username')
        u = models.user.objects.get(email=email)
        u.phone = phone
        u.username = username
        u.sex = sex
        u.save()
        return Response({'code': 0})


class modifyPassword(APIView):

    def post(self, request):
        formData = json.loads(request.body).get('formData')
        password = formData.get('pass')
        # checkPass = formData.get('checkPass')
        email = formData.get('email')
        u = models.user.objects.get(email=email)
        u.password = password
        u.save()
        return Response({'code': 0})


class uploadExcel(APIView):
    def save_file(self, file):
        filename = file.name
        temp = settings.MEDIA_ROOT + '\\excel\\'
        filepath = os.path.join(temp, filename)

        with open(filepath, 'wb') as fp:
            for chunk in file.chunks():
                fp.write(chunk)
        return self.request.build_absolute_uri(settings.MEDIA_URL + 'excel/' + filename)

    def post(self, request):

        file = request.data.get('file')
        # print(file,f'./media/excel/{file}')
        if os.path.isfile(f'./media/excel/{file}'):
            return Response({'code': -2})
        file_url = self.save_file(file)
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

        models.SaveFile.objects.create(
            name=file.name,
            create_time=create_time,
            file_url='excel/' + file.name,
        )
        return Response({"code": 0})


import os, time
import numpy as np
import pandas as pd
import warnings

warnings.filterwarnings('ignore')
from .extract_feature import extract_feature_for_acc
from .extract_feature import give_data_path


class extract_feature(APIView):

    def post(self, request):
        formData = json.loads(request.body)

        # for i in formData:
        #     # print(i)
        #     (shotname, extension) = os.path.splitext(i.get('name'))
        #     if (extension == '.csv'):
        #         Data_path = os.path.join(f'media/excel/{shotname}.csv')
        #         data = pd.read_csv(Data_path, encoding='utf-8').iloc[:, 1:].T.values
        #     if (extension == '.npy'):
        #         Label_path = os.path.join(f'media/excel/{shotname}.npy')
        #         label = np.load(Label_path)
        #     if extension != '.csv' and extension != '.npy':
        #         return Response({'code': -1})
        # print(data, label)
        # print(type(data), type(label))
        for i in formData:
            # print(i)
            (shotname, extension) = os.path.splitext(i.get('name'))
            if (extension == '.csv'):
                Data_path = os.path.join(f'media/excel/{shotname}.csv')
                x = pd.read_csv(Data_path, encoding='utf-8').iloc[:, :-1].values
                y = pd.read_csv(Data_path, encoding='utf-8').iloc[:, -1].values
                df = pd.read_csv(Data_path)
                length = len(df.columns) - 1
                break;
            elif (extension == '.xlsx'):
                Data_path = os.path.join(f'media/excel/{shotname}.xlsx')
                target_name = '区组'  # 后续添加功能，能够在网页选择标签
                data = pd.read_excel(Data_path, sheet_name='综合')
                target_index = data.columns.to_list().index(target_name)
                untarget_index = []
                for i in range(len(data.columns)):
                    if i != target_index:
                        untarget_index.append(i)

                x = pd.read_excel(Data_path).iloc[:, untarget_index].values
                y = pd.read_excel(Data_path).iloc[:, target_index].values
                df = pd.read_excel(Data_path, sheet_name='综合')
                length = len(df.columns) - 1

                break;
            # elif (extension == '.xls'):
            #     Data_path = os.path.join(f'media/excel/{shotname}.xls')
            #     data = pd.read_excel(Data_path, encoding='utf-8', sheet_name='�ۺ�').iloc[:, :-1].values
            #     label = pd.read_csv(Data_path, encoding='utf-8').iloc[:, -1].values
            #     df = pd.read_csv(Data_path)
            #     length = len(df.columns) - 1
            #     # print('length is',length)
            #     print(data, label)
            #     # print(type(data),type(label))
            #     break;
            else:
                return Response({'code': -1})
        # return Response({'code': 0})
        vimps_save_dir = os.path.join('./media/vimps_for_feature')
        if not os.path.exists(vimps_save_dir):
            os.makedirs(vimps_save_dir)

        # vimps_json = extract_feature_for_acc(x, y, Data_path, n_features=length, times=10, save_dir=vimps_save_dir)

        try:

            vimps_json = extract_feature_for_acc(x, y, Data_path, n_features=length, times=1, save_dir=vimps_save_dir)
        except:
            return Response({"code": -2})
        give_data_path(Data_path)
        return Response({'code': 0, 'vimps_json': vimps_json})


from zyq.utils.excel_to_csv import read_excel, xlsx_to_csv, get_excel_header


class excel_to_csv(APIView):

    def post(self, request):
        data = json.loads(request.body)
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        for i in data:
            # print(i)
            (shotname, extension) = os.path.splitext(i.get('name'))
            if extension == '.xlsx':
                if os.path.isfile(f'./media/excel/{shotname}_convert.csv'):
                    return Response({'code': -2})
                xlsx_to_csv(f'./media/excel/{shotname}_convert.csv', get_excel_header(f'media/excel/{shotname}.xlsx'))
                for row_value in read_excel(f'media/excel/{shotname}.xlsx'):
                    xlsx_to_csv(f'./media/excel/{shotname}_convert.csv', row_value)
                models.SaveFile.objects.create(
                    name=f'{shotname}_convert.csv',
                    create_time=create_time,
                    file_url='excel/' + f'{shotname}_convert.csv',
                )
            if extension == '.xls':
                if os.path.isfile(f'./media/excel/{shotname}_convert.csv'):
                    return Response({'code': -2})
                xlsx_to_csv(f'./media/excel/{shotname}_convert.csv', get_excel_header(f'media/excel/{shotname}.xls'))
                for row_value in read_excel(f'media/excel/{shotname}.xls'):
                    xlsx_to_csv(f'./media/excel/{shotname}_convert.csv', row_value)
                models.SaveFile.objects.create(
                    name=f'{shotname}_convert.csv',
                    create_time=create_time,
                    file_url='excel/' + f'{shotname}_convert.csv',
                )
            if extension != '.xlsx' and extension != '.xls':
                return Response({'code': -1})

        return Response({'code': 0})


class excel_to_npy(APIView):

    def post(self, request):
        data = json.loads(request.body)
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        for i in data:
            # print(i)
            (shotname, extension) = os.path.splitext(i.get('name'))
            if extension == '.xlsx':
                if os.path.isfile(f'./media/excel/{shotname}_convert.npy'):
                    return Response({'code': -2})

                xlsx_to_csv(f'./media/excel/{shotname}.csv', get_excel_header(f'media/excel/{shotname}.xlsx'))

                for row_value in read_excel(f'media/excel/{shotname}.xlsx'):
                    xlsx_to_csv(f'./media/excel/{shotname}.csv', row_value)

                data = pd.read_csv(f'./media/excel/{shotname}.csv')

                np.save(f'./media/excel/{shotname}.npy', data)

                data1 = np.load(f'./media/excel/{shotname}.npy')
                data2 = list(np.array(data1).flatten())

                np.save(f'./media/excel/{shotname}_convert.npy', data2)

                os.remove(f'./media/excel/{shotname}.npy')

                os.remove(f'./media/excel/{shotname}.csv')
                models.SaveFile.objects.create(
                    name=f'{shotname}_convert.npy',
                    create_time=create_time,
                    file_url='excel/' + f'{shotname}_convert.npy',
                )

            if extension == '.xls':
                if os.path.isfile(f'./media/excel/{shotname}_convert.npy'):
                    return Response({'code': -2})

                xlsx_to_csv(f'./media/excel/{shotname}.csv', get_excel_header(f'media/excel/{shotname}.xls'))

                for row_value in read_excel(f'media/excel/{shotname}.xls'):
                    xlsx_to_csv(f'./media/excel/{shotname}.csv', row_value)

                data = pd.read_csv(f'./media/excel/{shotname}.csv')

                np.save(f'./media/excel/{shotname}.npy', data)

                data1 = np.load(f'./media/excel/{shotname}.npy')

                data2 = list(np.array(data1).flatten())

                if os.path.isfile(f'./media/excel/{shotname}_convert.npy'):
                    return Response({'code': -2})

                np.save(f'./media/excel/{shotname}_convert.npy', data2)

                os.remove(f'./media/excel/{shotname}.npy')

                os.remove(f'./media/excel/{shotname}.csv')

                models.SaveFile.objects.create(
                    name=f'{shotname}_convert.npy',
                    create_time=create_time,
                    file_url='excel/' + f'{shotname}_convert.npy',
                )
        return Response({'code': 0})


class batch_deletion(APIView):

    def post(self, request):
        data = json.loads(request.body)

        for i in data:
            id = i.get('id')

            SaveFile.objects.get(id=id).delete()
            path = settings.MEDIA_ROOT + '/excel/' + i.get('name')

            os.remove(path)

        return Response({'code': 0})

def Colourlist_Generator(n):
    Rangelist = ['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    n = int(n)
    Colours = []   #空列表，用于插入n个表示颜色的字符串
    j = 1
    while j <= n:            #循环n次，每次在0到14间随机生成6个数，在加“#”符号，次次插入列表
        colour = ""    #空字符串，用于插入字符组成一个7位的表示颜色的字符串（第一位为#，可最后添加）
        for i in range(6):
            colour += Rangelist[random.randint(0,14)]    #用randint生成0到14的随机整数作为索引
        colour = "#"+colour               #最后加上不变的部分“#”
        Colours.append(colour)
        j = j+1
    return Colours


class select_for_scatter(APIView):

    def post(self, request):

        file_name = json.loads(request.body)[0].get('name')

        (shotname, extension) = os.path.splitext(str(file_name))
        if shotname == 'gge_real_data' or shotname == 'gge_simulation_data':
            return Response({'code': -1})
        if extension == '.xlsx' or extension == '.xls':
            file = os.path.join(f'media/excel/{shotname}{extension}')
            data = pd.read_excel(file)
        if extension == '.csv':
            file = os.path.join(f'media/excel/{shotname}.csv')
            data = pd.read_csv(file)

        data.to_csv('scatter_temp_data.csv')
        label_list = []
        data_list = []  # 保存四种类别数据的三维矩阵


        place_list = list(set(data['place'].tolist()))  # [1,2,3]
        clone_list = list(set(data['clone'].tolist()))

        for i in place_list:
            place_data = data.loc[data['place'] == i]
            place_data = place_data[['height', 'diameter']].values.tolist()
            data_list.append(place_data)
            label_list.append('place' + str(i))

        count_place=len(place_list)
        count_clone=len(clone_list)

        color_list = Colourlist_Generator(count_place)

        # print(count_place,count_clone)

        return Response({'code': 0, 'data_list': data_list, "label_list": label_list,'place_list':place_list,'clone_list':clone_list,'count_place':count_place,'color_list':color_list})

class upload_for_scatter(APIView):

    def post(self, request):

        file = request.data.get('file')
        # print(file)
        (shotname, extension) = os.path.splitext(str(file))
        if extension == '.xlsx' or extension == '.xls':
            data = pd.read_excel(file)
        if extension == '.csv':
            data = pd.read_csv(file)
        data.to_csv('scatter_temp_data.csv')
        label_list = []
        data_list = []  # 保存四种类别数据的三维矩阵


        place_list = list(set(data['place'].tolist()))  # [1,2,3]
        clone_list = list(set(data['clone'].tolist()))

        for i in place_list:
            place_data = data.loc[data['place'] == i]
            place_data = place_data[['height', 'diameter']].values.tolist()
            data_list.append(place_data)
            label_list.append('place' + str(i))

        count_place=len(place_list)
        count_clone=len(clone_list)

        color_list = Colourlist_Generator(count_place)

        # print(count_place,count_clone)

        return Response({'code': 0, 'data_list': data_list, "label_list": label_list,'place_list':place_list,'clone_list':clone_list,'count_place':count_place,'color_list':color_list})


class draw_2d_scatter(APIView):

    def post(self, request):
        label_list = []
        data_list = []  # 保存四种类别数据的三维矩阵
        data = pd.read_csv('scatter_temp_data.csv')
        front_place = json.loads(request.body).get('place')
        front_clone = json.loads(request.body).get('clone')
        #接受上传数据时随机生成的颜色列表，在此基础上多增加一种颜色即可
        color_list = json.loads(request.body).get('cl_list')

        color_judge = json.loads(request.body).get('cl_judge')

        limit_place = data.loc[data['place'] == int(front_place)]
        limit_place_and_clone = limit_place.loc[limit_place['clone'] == int(front_clone)]
        # df3为去除数据集中选中的地点和无性系数据后的数据
        df3 = data.append(limit_place_and_clone).drop_duplicates(keep=False)
        # 去除重复值并按数据升序排列
        place_list = list(set(df3['place'].tolist()))  # [1,2,3]

        for i in place_list:
            place_data = data.loc[data['place'] == i]
            place_data = place_data[['height', 'diameter']].values.tolist()
            data_list.append(place_data)
            if i == int(front_place):
                label_list.append('place ' + str(i)+' other clone')
            else:
                label_list.append('place ' + str(i))

        limit_place_and_clone = limit_place_and_clone[['height', 'diameter']].values.tolist()
        data_list.append(limit_place_and_clone)
        label_list.append('place '+str(front_place)+' clone ' + str(front_clone))

        color_add_list= []

        # 如果不是第一次选择无性系就使用上次的数据
        if color_judge:
            color_add_list = color_judge
        else:
            # 第一次选择无性系给定红色
            for i in color_list:
                color_add_list.append(i)
            color_add_list.append('#D70C2E')#红色
        return Response({'code': 0, 'data_list': data_list, "label_list": label_list,'color_add_list':color_add_list})

class compute_date(APIView):
    def get(self, request):
        date = []
        for y in range(2012, 2021):
            for m in range(1, 13):
                k = str(y) + '-' + str(m)
                date.append(k)
        # date = []

        # for m in range(1, 14):
        #     k = str(2012) + '-' + str(m)
        #     date.append(k)
        return Response({'date': date})

class test(APIView):
    def get(self, request):
        # return render(request,'./table_2018.html')
        return Response({'code': 999})
