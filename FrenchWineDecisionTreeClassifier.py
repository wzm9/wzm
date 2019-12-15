#coding:gbk
"""
����Ŀ�꣺���þ������㷨�Է�����Ʋ�ͬ����Ʒ�ֵ��Զ�����
���ߣ�����÷
���ڣ�2019/12/15
"""
import pandas as pd           # ������Ҫ�õĿ�
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import seaborn as sb
#%matplotlib inline
# ��������
df = pd.read_csv('frenchwine.csv')
df.columns = ['species','alcohol','malic_acid', 'ash','alcalinity ash','magnesium']
# �鿴ǰ5������
df.head()
print(df.head()) 
# �鿴����������ͳ����Ϣ
df.describe()
print(df.describe())

def scatter_plot_by_category(feat, x, y): #���ݵĿ��ӻ� 
    alpha = 0.5
    gs = df.groupby(feat)
    cs = cm.rainbow(np.linspace(0, 1, len(gs)))
    for g, c in zip(gs, cs):
        plt.scatter(g[1][x], g[1][y], color=c, alpha=alpha)

plt.figure(figsize=(20,6))
plt.subplot(131)
scatter_plot_by_category('species','alcalinity ash','magnesium')
plt.xlabel('alcalinity ash')
plt.ylabel('magnesium')
plt.title('species')
plt.show()

plt.figure(figsize=(20, 10)) #����seaborn���������Iris����ͬ����ͼ
for column_index, column in enumerate(df.columns):
    if column == 'species':
        continue
    plt.subplot(2,3, column_index + 1)
    sb.violinplot(x='species', y=column, data=df)
plt.show()

# ���ȶ����ݽ����з֣������ֳ�ѵ�����Ͳ��Լ�
from sklearn.model_selection import train_test_split #����sklearn���н�����飬����ѵ�����Ͳ��Լ�
all_inputs = df[['alcohol','malic_acid','ash','alcalinity ash','magnesium']].values
all_species = df['species'].values

(X_train,
 X_test,
 Y_train,
 Y_test) = train_test_split(all_inputs, all_species, train_size=0.85, random_state=4)#80%������ѡΪѵ����

# ʹ�þ������㷨����ѵ��
from sklearn.tree import DecisionTreeClassifier #����sklearn���е�DecisionTreeClassifier������������
# ����һ������������
decision_tree_classifier = DecisionTreeClassifier()
# ѵ��ģ��
model = decision_tree_classifier.fit(X_train, Y_train)
# ���ģ�͵�׼ȷ��
print(decision_tree_classifier.score(X_test, Y_test)) 
# ʹ��ѵ����ģ�ͽ���Ԥ�⣬Ϊ�˷��㣬
# ����ֱ�ӰѲ��Լ�����������ó�������
a = np.array(X_test)
b = a.tolist()
b[0],b[1],b[2] =b[1],b[15],b[14]
X_test = np.array(b)
print(X_test[0:3])#����3�����ݽ��в��ԣ���ȡ3��������Ϊģ�͵������

lise_name=[]#������һһ�����б�
model.predict(X_test[0:3])
for name in model.predict(X_test[0:3]):
	if name == 'Zinfandel':
		lise_name.insert(-1,'�ɷ���')#���б�Ԫ��������Ԫ��
	if name == 'Syrah':
		lise_name.insert(-1,'����')
	if name == 'Sauvignon':
		lise_name.insert(-1,'��ϼ��')
print(model.predict(X_test[0:3]))#������ԵĽ���������ģ��Ԥ��Ľ��
print(lise_name)
