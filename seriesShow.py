# -*- coding: utf-8 -*-
# @Author  : Hugo Wang
# @Time    : 2021/8/19 10:29
# @IDE     : PyCharm
# @Function: Show Time Series

from pandas import read_csv
from matplotlib import pyplot

# load dataset
dataset = read_csv('pollution.csv', header=0, index_col=0)
values = dataset.values
# specify columns to plot
groups = [0, 1, 2, 3, 5, 6, 7]
i = 1
# plot each column
pyplot.figure()
for group in groups:
    pyplot.subplot(len(groups), 1, i)
    pyplot.plot(values[:, group])
    pyplot.title(dataset.columns[group], y=0.5, loc='right')
    i += 1
pyplot.show()
