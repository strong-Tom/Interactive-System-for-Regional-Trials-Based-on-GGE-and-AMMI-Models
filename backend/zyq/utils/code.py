'''处理映射 方法1'''
import pandas as pd


def convert_shi_fou(txt):
    if '是' in txt:
        return 1
    else:
        return 0

#定义一个数据转换的函数，将中文数据转换为数值
def convert(dt):
    if dt in ['青绿','蜷缩','浊响','清晰','凹陷','硬滑','是']:
        return 1
    elif dt in ['乌黑','稍蜷', '沉闷', '稍糊', '稍凹', '软粘','否']:
        return 2
    elif dt in ['浅白', '硬挺', '清脆', '模糊', '平坦']:
        return 3

df = pd.read_csv('test.csv')
# 按行或按列操作时用apply()
df['好瓜']=df['好瓜'].apply(convert_shi_fou)#将某一列数据处理
# 每一个数据进行操作时用applymap()
dt1=dt1.applymap(convert)

'''处理映射 方法2'''
d = {'UK': 0, 'USA': 1, 'N': 2}
df['Nationality'] = df['Nationality'].map(d)

features_remain = [u'最大生命', u'初始生命', u'最大法力', u'最高物攻', u'初始物攻', u'最大物防', u'初始物防', u'最大每5秒回血', u'最大每5秒回蓝', u'初始每5秒回蓝', u'最大攻速', u'攻击范围']
data = data_ori[features_remain]
data[u'最大攻速'] = data[u'最大攻速'].apply(lambda x: float(x.strip('%'))/100)

'''将文件中的？替换成空，并舍弃含有空的行'''
df = df.replace({'?':np.nan}).dropna()

'''解决Graphviz,pydotplus中文乱码的问题，手动修改树结构的字体类型'''
dot_data_val = dot_data.getvalue()
dot_data_val = dot_data_val.replace('helvetica', 'MicrosoftYaHei')
graph = pydotplus.graph_from_dot_data(dot_data_val)
graph.write_png("zhuyiqi.png")

'''让plt能输入中文'''
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False

'''修改df后保存'''
# index=False 不将索引序列保存到文本
# header=None  去除列名（不保存列名）
df.to_csv('test.csv', sep=',',index=False)

'''捕获异常方式'''
try:
    s
except Exception as e:
    print('捕获到的异常', e)

'''将文件以时间命名保存在指定目录下'''
from backend.settings import MEDIA_ROOT
import time
import os
dir = MEDIA_ROOT + '/rule_table'
if not os.path.exists(dir):
    os.makedirs(dir)
path = dir+'/{}.csv'.format(time.strftime('%Y-%m-%d %H_%M_%S',time.localtime(time.time())))

'''导入文件'''

Data_path = ''
data = pd.read_csv(Data_path, encoding='utf-8').iloc[:, :-1].values
label = pd.read_csv(Data_path, encoding='utf-8').iloc[:, -1].values

'''删除文件某一列数据'''
df = pd.read_csv('')
df= df.drop('column_name', 1)
df.to_csv('test.csv', sep=',',index=False)

'''打印赋值'''
"Activation(rule={}, facts={}, context={})".format(
            self.rule, self.facts, self.context)

'''numpy转化为dataframe'''
df=pd.DataFrame(numpy)

'''dataframe转化为numpy'''
nmp=df.to_numpy()

'''pands把字符串类型的列，变成分类数字编码I'''
for field in [ "Sex", "Cabin","Embarked" ] :
    df[field] = df [field].astype("category").cat.codes

'''将数据二进制化处理，此处和onehotencoder大概一致'''
y = label_binarize(y,classes=[0,1,2])

'''将列中最大的那列输出'''
np.argmax(pre,axis=1)

'''加入噪点'''
n_sample,n_featrues = X.shape
X = np.c_[X,np.random.RandomState(0).randn(n_sample,80*n_featrues)]

'''生成numpy随机二维数组，i表示行，j表示列'''
a = [[random.randint(1, 6) for j in range(1, 6)] for i in range(1, 5)]
data=np.array(a)


'''画混淆矩阵'''
import seaborn as sns

sns.set()
f, ax = plt.subplots()
y_true = y_test
y_pred = best_clf.predict(x_test)

label_get=[1,2,3]
# for i in range(1,44):
#     label_get.append(i)
# print(label_get)


C2 = confusion_matrix(y_true, y_pred,labels=label_get)  # 数据中标签是什么就填什么
print(C2)  # 打印出来看看

sns.heatmap(C2, annot=True, ax=ax,annot_kws={"size": 10},fmt="d")  # 画热力图

ax.set_title('confusion matrix')  # 标题
ax.set_xlabel('predict')  # x轴
ax.set_ylabel('true')  # y轴

plt.show()





'''画各种混淆矩阵'''
import seaborn as sns
from matplotlib import pyplot as plt
from scipy.special import softmax
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score

sns.set_theme(color_codes=True)

# 横坐标是真实类别数，纵坐标是预测类别数
y_true = y_test
y_pred = best_clf.predict(x_test)
cf_matrix = confusion_matrix(y_true, y_pred)

figure, axes = plt.subplots(2, 2, figsize=(16 * 1.25, 16))

# 混淆矩阵
ax = sns.heatmap(cf_matrix, annot=True, fmt='g', ax=axes[0][0], cmap='Blues')
ax.title.set_text("Confusion Matrix")
ax.set_xlabel("y_pred")
ax.set_ylabel("y_true")
# plt.savefig(csv_path.replace(".csv", "_cf_matrix.png"))
# plt.show()


# 混淆矩阵 - 百分比
cf_matrix = confusion_matrix(y_true, y_pred)
ax = sns.heatmap(cf_matrix / np.sum(cf_matrix), annot=True, ax=axes[0][1], fmt='.2%', cmap='Blues')
ax.title.set_text("Confusion Matrix (percent)")
ax.set_xlabel("y_pred")
ax.set_ylabel("y_true")
# plt.savefig(csv_path.replace(".csv", "_cf_matrix_p.png"))
# plt.show()

# 召回矩阵，行和为1
sum_true = np.expand_dims(np.sum(cf_matrix, axis=1), axis=1)
precision_matrix = cf_matrix / sum_true
ax = sns.heatmap(precision_matrix, annot=True, fmt='.2%', ax=axes[1][0], cmap='Blues')
ax.title.set_text("Precision Matrix")
ax.set_xlabel("y_pred")
ax.set_ylabel("y_true")
# plt.savefig(csv_path.replace(".csv", "_recall.png"))
# plt.show()

# 精准矩阵，列和为1
sum_pred = np.expand_dims(np.sum(cf_matrix, axis=0), axis=0)
recall_matrix = cf_matrix / sum_pred
ax = sns.heatmap(recall_matrix, annot=True, fmt='.2%', ax=axes[1][1], cmap='Blues')
ax.title.set_text("Recall Matrix")
ax.set_xlabel("y_pred")
ax.set_ylabel("y_true")
# plt.savefig(csv_path.replace(".csv", "_precision.png"))
# plt.show()

# 绘制4张图
plt.autoscale(enable=False)
# plt.savefig(csv_path.replace(".csv", "_all.png"), bbox_inches='tight', pad_inches=0.2)
plt.show()

# F1矩阵
a = 2 * precision_matrix * recall_matrix
b = precision_matrix + recall_matrix
f1_matrix = np.divide(a, b, out=np.zeros_like(a), where=(b != 0))
ax = sns.heatmap(f1_matrix, annot=True, fmt='.2%', cmap='Blues')
ax.title.set_text("F1 Matrix")
ax.set_xlabel("y_pred")
ax.set_ylabel("y_true")
# plt.savefig(csv_path.replace(".csv", "_f1.png"))
plt.show()

