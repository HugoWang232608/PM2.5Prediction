# 基于LSTM模型预测PM2.5
数据集：UCI数据集 BeiJing PM2.5 Data Data Set
数据集详细说明请见：https://archive.ics.uci.edu/ml/datasets/Beijing+PM2.5+Data

## 环境说明
本程序在win10系统pycharm的以下环境中运行成功，不保证在其他环境能够运行

```
Python == 3.8
Tensorflow == 2.5.0
scikit-learn == 0.24.2
```

## 各程序说明
```dataPreprocessing.py```:  数据预处理，原始数据为 ```raw.csv```,预处理后的数据为 ```pollution.csv```;

```seriesShow.py```: 时间序列绘制程序

```main.py```: 主程序
