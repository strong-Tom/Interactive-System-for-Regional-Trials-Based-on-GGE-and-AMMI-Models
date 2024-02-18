import pandas as pd
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def draw_3d_scatter(Data_path,x_tz,y_tz,z_tz,target_name):
    '''
    画3维散点图
    target:分类标签名称
    target_list:分类标签列表（无重复）
    x_tz,y_tz,z_tz:三维散点图的3个坐标轴名称
    '''

    # data = pd.read_csv(Data_path, encoding='utf-8')
    data = pd.read_excel(Data_path,sheet_name='综合')
    target_index = data.columns.to_list().index(target_name)
    target_list = list(set(data.iloc[:, target_index].to_list()))  # 里面保存不重复的标签
    print(target_list)
    # data1=data.loc[data['地点']==1]的循环,给属于不同标签的数据分为不同类
    for i in target_list:
        m = f'data{i}'
        exec(m + '= data.loc[data[target_name]==i]')

    # target_list=[1,2]
    for i in target_list:  # range()包前不包后
        '''
        每一次循环相当于以下过程
        x1=data1['苗高,cm']
        y1=data1['地径,mm']
        z1=data1['无性系']
        '''
        x = f'x{i}'
        y = f'y{i}'
        z = f'z{i}'
        m = f'data{i}'
        exec(x + '=' + m + '[x_tz]')
        exec(y + '=' + m + '[y_tz]')
        exec(z + '=' + m + '[z_tz]')

    fig = plt.figure()
    ax = Axes3D(fig)
    ax.set_xlabel(x_tz)
    ax.set_ylabel(y_tz)
    ax.set_zlabel(z_tz)

    # target_list = [1, 2,3]
    for i in target_list:
        exec('ax.scatter(x' + str(i) + ', y' + str(i) + ', z' + str(i) + ')')
    plt.show()

def draw_2d_scatter(Data_path,x_tz,y_tz,target_name):
    '''画二维散点图'''

    # data = pd.read_csv(Data_path, encoding='utf-8')
    data=pd.read_excel(Data_path,sheet_name='综合')


    plt.xlabel(x_tz)
    plt.ylabel(y_tz)

    target_index=data.columns.to_list().index(target_name)
    target_list = list(set(data.iloc[:, target_index].to_list()))  # 里面保存不重复的标签


    for i in target_list:
        m = f'data{i}'
        exec(m + '= data.loc[data[target_name]==i]')

    for i in target_list:  # range()包前不包后
        '''
        每一次循环相当于以下过程
        x1=data1['苗高,cm']
        y1=data1['地径,mm']
        '''
        x = f'x{i}'
        y = f'y{i}'
        m = f'data{i}'
        exec(x + '=' + m + '[x_tz]')
        exec(y + '=' + m + '[y_tz]')



    target_list=[2,3]

    for i in target_list:
        label = f'label{i}'
        label=target_name+str(i)
        exec('plt.scatter(x'+str(i)+',y'+str(i)+',label=label)')

    label1='地点1'
    exec("plt.scatter(x1,y1,label=label1)")
    # exec ('print(x1,y1)')




    plt.legend()
    plt.show()

def draw_2d_scatter_for_web():

    return 0


def draw_2d_scatter_batch(Data_path,x_tz,y_tz,target_name):
    '''画二维散点图'''

    # data = pd.read_csv(Data_path, encoding='utf-8')
    data=pd.read_excel(Data_path,sheet_name='综合')



    target_index=data.columns.to_list().index(target_name)
    target_list = list(set(data.iloc[:, target_index].to_list()))  # 里面保存不重复的标签


    for i in target_list:
        data1 = data.loc[data['地点'] == 1]
        data2 = data.loc[data['地点'] == 2]
        data3 = data.loc[data['地点'] == 3]

    for i in target_list:  # range()包前不包后

        x1=data1['苗高,cm']
        y1=data1['地径,mm']
        x2=data2['苗高,cm']
        y2=data2['地径,mm']
        x3=data3['苗高,cm']
        y3=data3['地径,mm']

    label_other='地点3其他无性系'
    label_special='地点3无性系'
    color_other='gray'
    color_special='red'


    for i in range(1,10):
        plt.subplot(3,3,i)

        plt.xlabel(x_tz)
        plt.ylabel(y_tz)
        plt.scatter(x1,y1,label='地点1')
        plt.scatter(x2,y2,label='地点2')
        data_youyanse = data3.loc[data3['无性系'] == i]
        data_wuyanse = data3.loc[data3['无性系'] != i]
        x_youyanse = data_youyanse['苗高,cm']
        y_youyanse = data_youyanse['地径,mm']
        x_wuyanse = data_wuyanse['苗高,cm']
        y_wuyanse = data_wuyanse['地径,mm']

        plt.scatter(x_wuyanse,y_wuyanse,label=label_other,c=color_other)
        plt.scatter(x_youyanse,y_youyanse,label=label_special+str(i),c=color_special)
        plt.legend()

        # plt.subplot(2,2,1)

    plt.show()
    plt.close()

    for i in range(10,19):
        plt.subplot(3,3,i-9)
        plt.xlabel(x_tz)
        plt.ylabel(y_tz)
        plt.scatter(x1,y1,label='地点1')
        plt.scatter(x2,y2,label='地点2')
        data_youyanse = data3.loc[data3['无性系'] == i]
        data_wuyanse = data3.loc[data3['无性系'] != i]
        x_youyanse = data_youyanse['苗高,cm']
        y_youyanse = data_youyanse['地径,mm']
        x_wuyanse = data_wuyanse['苗高,cm']
        y_wuyanse = data_wuyanse['地径,mm']

        plt.scatter(x_wuyanse,y_wuyanse,label=label_other,c=color_other)
        plt.scatter(x_youyanse,y_youyanse,label=label_special+str(i),c=color_special)
        plt.legend()

        # plt.subplot(2,2,1)

    plt.show()
    plt.close()

    for i in range(19,28):
        plt.subplot(3,3,i-18)
        plt.xlabel(x_tz)
        plt.ylabel(y_tz)
        plt.scatter(x1,y1,label='地点1')
        plt.scatter(x2,y2,label='地点2')
        data_youyanse = data3.loc[data3['无性系'] == i]
        data_wuyanse = data3.loc[data3['无性系'] != i]
        x_youyanse = data_youyanse['苗高,cm']
        y_youyanse = data_youyanse['地径,mm']
        x_wuyanse = data_wuyanse['苗高,cm']
        y_wuyanse = data_wuyanse['地径,mm']

        plt.scatter(x_wuyanse,y_wuyanse,label=label_other,c=color_other)
        plt.scatter(x_youyanse,y_youyanse,label=label_special+str(i),c=color_special)
        plt.legend()

        # plt.subplot(2,2,1)

    plt.show()
    plt.close()

    for i in range(28,37):
        plt.subplot(3,3,i-27)
        plt.xlabel(x_tz)
        plt.ylabel(y_tz)
        plt.scatter(x1,y1,label='地点1')
        plt.scatter(x2,y2,label='地点2')
        data_youyanse = data3.loc[data3['无性系'] == i]
        data_wuyanse = data3.loc[data3['无性系'] != i]
        x_youyanse = data_youyanse['苗高,cm']
        y_youyanse = data_youyanse['地径,mm']
        x_wuyanse = data_wuyanse['苗高,cm']
        y_wuyanse = data_wuyanse['地径,mm']

        plt.scatter(x_wuyanse,y_wuyanse,label=label_other,c=color_other)
        plt.scatter(x_youyanse,y_youyanse,label=label_special+str(i),c=color_special)
        plt.legend()

        # plt.subplot(2,2,1)

    plt.show()
    plt.close()

    for i in range(37,46):
        plt.subplot(3,3,i-36)
        plt.xlabel(x_tz)
        plt.ylabel(y_tz)
        plt.scatter(x1,y1,label='地点1')
        plt.scatter(x2,y2,label='地点2')
        data_youyanse = data3.loc[data3['无性系'] == i]
        data_wuyanse = data3.loc[data3['无性系'] != i]
        x_youyanse = data_youyanse['苗高,cm']
        y_youyanse = data_youyanse['地径,mm']
        x_wuyanse = data_wuyanse['苗高,cm']
        y_wuyanse = data_wuyanse['地径,mm']

        plt.scatter(x_wuyanse,y_wuyanse,label=label_other,c=color_other)
        plt.scatter(x_youyanse,y_youyanse,label=label_special+str(i),c=color_special)
        plt.legend()

        # plt.subplot(2,2,1)

    plt.show()
    plt.close()
