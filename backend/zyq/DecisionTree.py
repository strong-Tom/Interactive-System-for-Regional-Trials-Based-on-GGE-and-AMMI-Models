
"""
Created on Tue Jan 23 23:06:37 2018

@author: DAMI
"""

from rest_framework.response import Response
import os
import time

from django.contrib import admin, auth
from django.contrib.auth.models import User
from django.db.models import Q
from django.http import request, JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView
from backend import settings
from . import models
from .models import Blog, treeTmp, SaveFile, lineChart, pieChart
from .models import regional_sample
from .models import forset
from .models import poplar
from .models import video
from .models import user
from .serializers import regional_sampleSerializer, treeTmpSerializer, userSerializer, SaveFileSerializer, \
    lineChartSerializer, pieChartSerializer
from .serializers import forsetSerializer
from .serializers import BlogSerializer
from .serializers import poplarSerializer
from .serializers import videoSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from six import StringIO
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
import pydotplus

import time

from backend import settings
from backend.settings import MEDIA_ROOT
from zyq.utils.TreeToRule import *


class extract_rule(APIView):

    def post(self, request):
        formData = json.loads(request.body)
        for i in formData:

            (shotname, extension) = os.path.splitext(i.get('name'))
            if (extension == '.csv'):
                path = MEDIA_ROOT + '/excel/'+shotname+'.csv'

                break
            else:
                return Response({'code': -1})

        '''Reading the file and preperation of data '''
        # print('path is',path)
        df = pd.read_csv(path)

        df2 = df.replace({'?': np.nan}).dropna()

        # print("The Dataset before preprocessing: %s instances and %s attributes" % (df.shape[0], df.shape[1]))
        # print("The Dataset after preprocessing: %s instances and %s attributes" % (df2.shape[0], df2.shape[1]))

        '''Training the data and calculate the process time '''

        X = np.array(df2.iloc[:,:-1])
        y = np.array(df2.iloc[:,-1])
        # print(X,y)
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
        start_time = time.clock()
        clf_gini = DecisionTreeClassifier(max_depth=3, random_state=0).fit(X_train, y_train)

        # 生成规则
        feature_names = list(df2.columns[:-1])
        class_names = ['恶性', '良性']
        treeUtil = TreeUtil(
            clf=clf_gini,
            feature_names=feature_names,
            class_names=class_names
        )
        returndata = treeUtil.getRuleList(print_detail=True)
        # print(returndata)
        # print("done")

        '''Calculating the accuracy of trained sets'''

        # print('Accuracy of Decision Tree classifier on training set: {:.2f}'
        #       .format(clf_gini.score(X_train, y_train)))
        # print('Accuracy of Decision Tree classifier on test set: {:.2f}'
        #       .format(clf_gini.score(X_test, y_test)))

        '''画出决策树'''
        dot_data = StringIO()
        tree.export_graphviz(clf_gini, out_file=dot_data,
                             feature_names=feature_names, class_names=['恶性', '良性'],
                             filled=True, rounded=True, special_characters=True)
        '''解决Graphviz,pydotplus中文乱码的问题，手动修改树结构的字体类型'''
        dot_data_val = dot_data.getvalue()
        dot_data_val = dot_data_val.replace('helvetica', 'MicrosoftYaHei')
        graph = pydotplus.graph_from_dot_data(dot_data_val)
        dir = MEDIA_ROOT + '/decisionTree_img'
        if not os.path.exists(dir):
            os.makedirs(dir)
        path = dir + '/{}.png'.format(time.strftime('%Y-%m-%d %H_%M_%S', time.localtime(time.time())))
        graph.write_png(path)

        # 预测
        # p = clf_gini.predict(np.array([[4, 4, 4, 23, 23, 4, 4, 4, 4, 4]]))
        # print('p is', p)

        '''将生成的决策树图片转换为base64发送给前端'''
        import base64
        png = open(path, 'rb')
        res = png.read()
        s = base64.b64encode(res)
        png.close()
        img = s.decode('ascii')

        return Response({"code": 0,'img':img})