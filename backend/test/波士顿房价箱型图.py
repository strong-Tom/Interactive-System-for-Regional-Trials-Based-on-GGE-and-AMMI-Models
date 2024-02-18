import seaborn as sns
import pandas as pd
from matplotlib import pyplot as plt
from sklearn.datasets import load_boston

boston = load_boston()
df = pd.DataFrame(boston.data, columns=boston.feature_names)
df['MEDV'] = boston.target

sns.boxplot(data=df, orient='h')
plt.show()