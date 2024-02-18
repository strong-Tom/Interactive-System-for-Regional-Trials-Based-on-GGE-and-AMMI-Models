import seaborn as sns
import matplotlib.pyplot as plt

# 读取数据集
df = sns.load_dataset('iris')

# 绘制箱形图
sns.boxplot(x='species', y='petal_length', data=df)

# 设置图形参数
plt.title('Petal Length by Species')
plt.xlabel('Species')
plt.ylabel('Petal Length')

# 显示图形
plt.show()
