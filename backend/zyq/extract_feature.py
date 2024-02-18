import base64
import random
import os, time
from io import BytesIO

import numpy as np
# 无省略显示np中所有数据
# np.set_printoptions(threshold=np.inf)
import pandas as pd

from sklearn.exceptions import NotFittedError
from sklearn.metrics import accuracy_score, roc_curve, auc
from sklearn.model_selection import train_test_split, StratifiedKFold
import warnings

from sklearn.preprocessing import StandardScaler
from sklearn.utils import check_random_state, shuffle
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.neural_network import MLPClassifier
import matplotlib.pyplot as plt

warnings.filterwarnings('ignore')
'''
    > 1. 计算基因的重要性，没有交叉验证
'''


# 常用路径：
# C:/Users/zyq/Desktop/我的网站/backend/GeneImportance/GeneImportance/Data/TCGA-KIRC/
def get_shuffled_data(data, dim, random_state=None):
    '''
    返回 打乱后的data
    '''
    myrandom = check_random_state(random_state)
    index = np.arange(data.shape[0])
    myrandom.shuffle(index)
    t_data = data.copy()
    t_data[:, dim] = data[:, dim][index]
    return t_data


class ClassifierMixin:
    def score(self, X, y, sample_weight=None):
        return accuracy_score(y, self.predict(X), sample_weight=sample_weight)


class Classifier(ClassifierMixin):
    def __init__(self, random_state=None):
        self.random_state = random_state
        self.best_clf = None
        self.ensembles = self._build_ensemble()

    def _build_ensemble(self):
        '''
            Create a ensemble classify.
            return: List[clf]
        '''
        # LDA用solver=svd，如果输入数据只有一个特征，会报错，可以换solver
        LDA = LinearDiscriminantAnalysis(solver='lsqr')
        KNN = KNeighborsClassifier()
        DTC = DecisionTreeClassifier()
        svc = SVC(probability=True)
        LR = LogisticRegression()
        MLP = MLPClassifier(max_iter=1000)
        MNB = GaussianNB()
        # 集成分类列表
        self.ensembles = [LDA, KNN, DTC, svc, MLP, LR, MNB]
        return self.ensembles

    def fit(self, x_train, y_train):
        '''
            fit every clf in ensembles
            return : List[clf(fitted)]
        '''
        self.ensembles = [clf.fit(x_train, y_train) for clf in self.ensembles]
        return self

    def find_best_ensembles(self, x_test, y_test, accuracy=False):
        '''
            训练所有的分类器:ensemble_fitted
            使用测试集合得出每个分类器的准确性
            param:
                accuracy: True/False: 根据什么来判断是否是最好的
                    True: 准确率， False: ErrorOOB
                # self.ensembles: 集成分类器（训练好的）
                 x_test, y_test: 训练集和测试集
            reutrn:
                idx, best_clf, best_score
                准确性最高的分类器的索引，训练好的分类器，最好分类器的准确性
        '''
        if accuracy == True:
            scores = [clf.score(x_test, y_test) for clf in self.ensembles]
        else:
            scores = [0 for _ in self.ensembles]
            for i, clf in enumerate(self.ensembles):
                try:
                    y_pred = clf.predict(x_test)
                    scores[i] = 1 - self.ErrOOB_score(y_true=y_test, y_pred=y_pred)
                except NotFittedError as e:
                    scores[i] = 0
            # scores = [1 - self.ErrOOB_score(y_true=y_test, y_pred=clf.predict(x_test)) for clf in self.ensembles]
        # x.argsort()返回从小到大排序的索引，x[x.argsort()[-1]] 表示取最大值
        idx = np.argsort(scores)[-1]  # 取最大得分值的索引
        self.best_clf = self.ensembles[idx]
        self.best_score = scores[idx]
        return idx, self.best_clf, self.best_score

    def _predict_by_voted(self, x_test):
        '''
            仅适用二分类情况(0,1)
            投票过半数计为1, 否则计为0
        '''
        y_preds = [clf.predict(x_test) for clf in self.ensembles]

        y_preds = np.array(y_preds).reshape(len(y_preds), -1)
        y_pred = np.mean(y_preds, axis=0) > 0.5
        return y_pred

    def _predict_by_best_clf(self, x_test):
        '''
        直接调用分类器自带的predict方法
        '''
        y_pred = self.best_clf.predict(x_test)
        return y_pred

    def predict(self, x_test, vote=False):
        '''
        两种预测方法
        一: 使用投票策略，使用所有的分类器进行预测，将所有的lable进行投票，投票结果为最终结果
        二:使用最好的分类器，进行预测，预测结果为最终结果
        '''
        if vote == True:
            y_pred = self._predict_by_voted(x_test)
        else:
            if self.best_clf == None:
                raise ValueError(
                    'The best_clf is not defined!\n U Should execute the function named "find_best_ensembles()"!')
            y_pred = self._predict_by_best_clf(x_test)
        return y_pred

    def predict_proba(self, x_test):
        '''
            使用单个最好的分类器，来预测数据属于某一类别的概率
            其结果可以用来画ROC曲线
            在二分类总可以用来计算auc值：
            auc = roc_auc_score(y_test, clf.predict_proba(x_test)[:, 1])
        '''
        if self.best_clf == None:
            raise AttributeError('No best_clf')
        y_pred_proba = self.best_clf.predict_proba(x_test)
        return y_pred_proba

    def get_best_score(self, x_test, y_test, vote=False, accuracy=True):
        """
            得到最好的score，也是有两种方式
            一:使用投票/最好分类器 来得到预测结果
            二:使用准确性(accuracy)还是文章中的ErrOOB来作为最后的结果
        """
        y_pred = self.predict(x_test, vote=vote)
        if accuracy == True:
            self.best_score = accuracy_score(y_test, y_pred)
        else:
            self.best_score = 1 - self.ErrOOB_score(y_test, y_pred)
        return self.best_score

    def ErrOOB_score(self, y_true, y_pred):
        '''
        对于二分类
        TP:真阳--原本是正例，预测为正例
        TF:真阴--原本是反例，预测为反例
        FP:假阳--原本是反例，预测为正例
        FN:假阴--原本是正例，预测为反例
        ERROR = [FN/(TP + FN) + FP/(TN + FP)] / 2
        '''
        TP, TN, FP, FN = self.get_mixture_matrix(y_true, y_pred)
        return (FN / (TP + FN) + FP / (TN + FP)) / 2

    def get_mixture_matrix(self, y_true, y_pred):
        '''
        对于二分类
        TP:真阳--原本是正例，预测为正例
        TF:真阴--原本是反例，预测为反例
        FP:假阳--原本是反例，预测为正例
        FN:假阴--原本是正例，预测为反例
        '''
        T = y_pred == 1
        F = y_pred != 1
        P = y_true == 1
        N = y_true != 1
        TP, TN, FP, FN = np.sum(T & P), np.sum(F & N), np.sum(T & N), np.sum(F & P)
        return TP, TN, FP, FN


class Vimps:
    '''
        计算特征重要性时，用来记录每次抽取的特征重要性

        一个简单的数据结构
    '''

    def __init__(self, num_of_features, save_dir=None):
        self.vimps = np.zeros(num_of_features, )
        self.count_feature = np.zeros(num_of_features, )
        self.save_dir = save_dir
        self.__check()

    def __check(self):
        if self.save_dir != None and not os.path.isdir(self.save_dir):
            raise f'This dir {self.save_dir} is not exist.'

    def update(self, n_feature_vimps, feature_count=None):
        if isinstance(n_feature_vimps, dict) and isinstance(feature_count, dict):
            for key, value in n_feature_vimps.items():
                self.vimps[key] += value
                self.count_feature[key] += feature_count[key]

        elif isinstance(n_feature_vimps, np.ndarray) and isinstance(feature_count, np.ndarray):
            self.vimps += n_feature_vimps
            self.count_feature += feature_count

    # 平均重要性
    def get_avg_vimps(self):
        not_nan_idx = np.where(self.count_feature != 0)
        return self.vimps[not_nan_idx] / self.count_feature[not_nan_idx]

    def save_vimps(self, save_path=None):
        if self.save_dir != None and save_path == None:
            save_path = os.path.join(self.save_dir, f'vimps_and_count_{time.time()}.csv')
        elif self.save_dir == None and save_path == None:
            save_path = f'vimps_and_count_{time.time()}.csv'
        elif self.save_dir != None and save_path != None:
            save_path = os.path.join(self.save_dir, save_path)
        # 指定为-1的时候，其行或列会随机分配一个数据,reshape(-1, 1)表示返回一个一列的数据
        # 保存数据到指定路径中
        # np.hstack表示在水平方向堆叠
        np.savetxt(save_path, np.hstack([self.vimps.reshape(-1, 1), self.count_feature.reshape(-1, 1)]))


def train_and_trainscore(X, y):
    # ans 将迭代num_iter次的结果都存储起来，到结束后一起保存，节省计算机读写文件时间。
    # ans = np.zeros([num_iter, X.shape[1]+1])
    # X是抽取到的特征相关数据，y是标签
    x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)
    classifier = Classifier()
    classifier = classifier.fit(x_train, y_train)
    _, best_clf, best_score = classifier.find_best_ensembles(x_test, y_test)

    # # 初始化每个特征的重要性， vimps[:-1] 记录每个特征重要性，vimps[-1]记录分类器的种类
    vimps = np.zeros((x_test.shape[1]))
    # if best_score < 0.75:
    #     return 0, vimps

    # # 遍历所有特征(这里是108维)，计算
    for n_dim in range(x_test.shape[1]):

        # 打乱一维特征，再使用最好的分类器来预测一下结果
        shuffle_one_feature_data = get_shuffled_data(x_test, n_dim)
        score_shuffled = classifier.get_best_score(shuffle_one_feature_data, y_test, vote=False, accuracy=False)
        # 定义：该维特征的重要性 = 未打乱这个维度之前的准确性 - 打乱这个维度之后的准确性
        one_feature_imptns = best_score - score_shuffled
        # 去掉负数
        if one_feature_imptns < 0:
            one_feature_imptns = 0
        #     print(n_dim)
        # 保存
        vimps[n_dim] = one_feature_imptns
    # # # vimps[-1] = idx
    return best_score, vimps


# X是data，y是标签，n_features是抽取多少个特征，times是抽取次数
def extract_feature_for_acc(X, y, Data_path, n_features, times, save_dir):
    # get n features from X randomly.
    sample = range(X.shape[1])
    vimps_ans = Vimps(X.shape[1], save_dir)
    # graph_vimps = GraphVimps(X.shape[1], save_dir)
    feature_dict = {}
    feature_count = {}

    best_score_total = 0  # 计算n次采样最高得分的平均数

    # 抽times次
    for _ in range(times):
        # sample为所有特征，从所有特征中抽取n_features个特征，返回被抽取的特征的索引
        extract_features = random.sample(sample, n_features)

        if os.path.splitext(Data_path)[-1] == '.xlsx':
            df = pd.read_excel(Data_path, sheet_name="综合")
            target_name = '区组'  # 后续添加功能，能够在网页选择标签，传入这里
            target_index = df.columns.to_list().index(target_name)
            untarget_index = []
            for i in range(len(df.columns)):
                if i != target_index:
                    untarget_index.append(i)
            feature_label = list(df.columns[untarget_index])
        if os.path.splitext(Data_path)[-1] == '.csv':
            df = pd.read_csv(Data_path)
            # 保存被抽到的特征的名称，后续显示在x轴的刻度上
            feature_label= list(df.columns[:-1])

        # print(feature_label)

        # best_score是每次采样集成分类器中的最高得分，vimps是每次采样的特征重要性
        best_score, vimps = train_and_trainscore(X[:, extract_features], y)

        best_score_total += best_score  # 每次最好得分累加，算平均得分

        # global get_best_clf
        # get_best_clf=best_clf#把最好分类器传给画roc的函数

        # print('best_score is ',best_score)
        # extract_features是被抽取到的样本的索引组成的列表，顺序是乱的
        for i, vimp in zip(extract_features, vimps):
            if i in feature_dict:
                feature_dict[i] += vimp
                feature_count[i] += 1
            else:
                feature_dict[i] = vimp
                feature_count[i] = 1
        print('第%d次重采样被抽到的特征索引是：' % int(_ + 1), extract_features, '每次特征重要性：', vimps,
              "每次最好得分是：", best_score)

    vimps_ans.update(feature_dict, feature_count)
    vimps_ans.save_vimps()  # 保存积累n轮采样积累的特征重要性和每个特征被抽到的总次数

    print(times, '次采样的平均特征重要性是：', vimps_ans.get_avg_vimps(), ';', times, '次采样的平均得分是：',
          best_score_total / times)

    # 将平均重要性和标签分别转化为数组并且转化为json数组
    vimps_json = json_list(list(np.array(vimps_ans.get_avg_vimps()).flatten()), list(np.array(feature_label).flatten()))

    return vimps_json


def json_list(list1, list2):
    '''
    将两个list转化为json形式，
    如[{"value":0.0,"name":"树木高"}
    {"value":0.0,"name":"树木宽"}]
    '''
    lst = []
    for index, item in enumerate(list1):
        for index1, item1 in enumerate(list2):
            if (index == index1):
                d = {}
                d['value'] = list1[index]
                d['name'] = list2[index]
                # print("every time is",d)
                lst.append(d)
    return json.dumps(lst, separators=(',', ':'), ensure_ascii=False)


def ROC_line_chart(pre_label, test_label):
    '''
    :param pre_label: 预测标签
    :param test_label: 真实标签
    :param result_path_dir: 输出路径
    :return:
    '''
    acc = accuracy_score(test_label, pre_label)  # 计算acc的值

    fpr, tpr, threshold = roc_curve(test_label, pre_label)  ###计算真正率和假正率
    roc_auc = auc(fpr, tpr)  ###计算auc的值
    print("roc_line_chart中accuracy准确率是：", acc, 'auc是', roc_auc, '\n')

    plt.figure()
    lw = 2
    plt.figure(figsize=(10, 10))
    plt.plot(fpr, tpr, color='darkorange',
             lw=lw, label='AUC (area = %0.2f)' % roc_auc)  ###假正率为横坐标，真正率为纵坐标做曲线
    plt.plot([0, 1], [0, 1], color='navy', lw=lw, linestyle='--')
    plt.xlim([0.0, 1.0])
    plt.ylim([0.0, 1.05])
    plt.xlabel('False Positive Ratde')
    plt.ylabel('True Positive Rate')
    plt.legend(loc="lower right")

    # 将图片以二进制的格式传到前端
    sio = BytesIO()
    plt.savefig(sio, format='png')
    data = base64.encodebytes(sio.getvalue()).decode()
    # data=base64.b64encode(sio.getvalue())
    src = 'data:image/png;base64,' + str(data)

    # # 记得关闭，不然画出来的图是重复的
    plt.close()
    return src


#########################django框架###############################
import os
import time
from rest_framework.response import Response
from rest_framework.utils import json
from rest_framework.views import APIView


def give_data_path(Data_path):
    '''把前端选中的数据在后端的路径传给画roc曲线的函数'''
    global get_Data_path
    get_Data_path = Data_path


class draw_roc(APIView):

    def post(self, request):
        Data_path = get_Data_path
        data = json.loads(request.body)
        selected_feature = []
        for i in data:
            selected_feature.append(i.get('name'))

        print(selected_feature)
        # 这里的readcsv要改成readexcel
        # df= pd.read_csv(get_Data_path, encoding='utf-8').iloc[:, :-1]
        df = df[selected_feature]
        X = df.to_numpy()
        # y = pd.read_csv(Data_path, encoding='utf-8').iloc[:, -1].values
        x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.3, stratify=y)
        best_clf = LinearDiscriminantAnalysis()  # 随便写的一个分类器，roc只能用于2分类，所以不用了
        # print('画roc曲线用的最好分类器是：',best_clf,'\n')
        best_clf.fit(X, y)  # 这里使用的最好分类器是最后一轮采样的最好分类器
        pre_label = best_clf.predict(x_test)
        src = ROC_line_chart(pre_label, y_test)
        return Response({'code': 0, 'src': src})
