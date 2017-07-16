# -*- coding: utf-8 -*-
# 1. 读入ag0613.csv数据集，并计算数据的最大值、最小值、均值、标准差、中位数
import numpy as np
v=np.loadtxt('ag0613.csv', delimiter=',', usecols=(0,), unpack=True,skiprows=1)

print "highest =", np.max(v)
print "lowest =", np.min(v)
print "avg =", np.average(v)
print "std =", np.std(v)
print "median =", np.median(v)

