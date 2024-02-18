import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
data1 = pd.read_excel('../qsy.xlsx')
# 创建一个示例数据集，包括4个特征和1个目标变量
data = pd.DataFrame(data1)

# 计算各个变量之间的相关系数
corr = data.corr()
# sns.set(font_scale=1.25)#字符大小设定
# plt.figure(figsize=(10, 7))
# 绘制热力图，并显示相关系数大小和方向
# sns.heatmap(corr, annot=True, cmap='coolwarm')
sns.pairplot(data)
plt.title('大庆地区相关性分析热力图')

# plt.xlabel('x_label',fontsize=20, color='k') #x轴label的文本和字体大小
# plt.ylabel('y_label',fontsize=20, color='k') #y轴label的文本和字体大小
# plt.xticks() #x轴刻度的字体大小（文本包含在pd_data中了）
# plt.yticks(fontsize=20) #y轴刻度的字体大小（文本包含在pd_data中了）

# plt.rcParams['figure.figsize'] = (5.5, 5)
plt.show()

print(data)
