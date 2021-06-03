import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# # 绘制简单的曲线
# plt.plot([1, 3, 5], [4, 8, 10])
# plt.show()


# # 1、x轴的定义域为 -3.14 ~ 3.14, 中间间隔100个元素
# x = np.linspace(-np.pi, np.pi, 100)
# plt.plot(x, np.sin(x))
# plt.show()


# # 1、绘制多条曲线,定义域：-2pi ~ 2pi
# x = np.linspace(-np.pi * 2, np.pi * 2, 100)
# # 2、创建图表
# plt.figure(1, dpi=50)
# # 3、画四条线
# for i in range(1, 5):
#     plt.plot(x, np.sin(x / i))
# plt.show()


# # 1、创建图表，dpi代表图片的精细度，dpi越大文件体积越大，杂志要300以上
# plt.figure(1, dpi=50)
# data = [1, 1, 1, 2, 2, 2, 3, 3, 4, 5, 5, 6, 4]
# # 2、只要传入数据，直方图就会统计数据出现的次数
# plt.hist(data)
# plt.show()


# # 1、绘制散点图
# x = np.arange(1, 10)
# y = x
# fig = plt.figure()
# # c = 'r' 表示散点的颜色为红色，marker表示指定三点多形状为圆形
# plt.scatter(x, y, c='r', marker='o')
# plt.show()


# # 1、读取文件数据并用指定方式绘制
# iris = pd.read_csv('./iris_training.csv')
# # 显示前五行的信息
# print(iris.head())

# # 绘制散点图，指定x、y轴采用的数据
# iris.plot(kind='scatter', x='120', y='4')
# plt.show()


import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# iris = pd.read_csv("./iris_training.csv")
# # 设置样式
# sns.set(style="white", color_codes=True)
# # 设置绘制格式为散点图
# sns.jointplot(x="120", y="4", data=iris, size=5)
# # distplot绘制曲线
# sns.displot(iris['120'])
# plt.show()


iris = pd.read_csv("./iris_training.csv")
# 设置样式
sns.set(style="white", color_codes=True)
# FaceGrid 一般绘制函数
# hue 彩色显示分类0/1/2
# plt.scatter绘制散点图
# add_legend()显示分类的描述信息
# sns.FacetGrid(iris, hue='virginica', size=5).map(plt.scatter, '120', '4').add_legend()
sns.FacetGrid(iris, hue='virginica', size=5).map(plt.scatter, 'setosa', 'versicolor').add_legend()
plt.show()