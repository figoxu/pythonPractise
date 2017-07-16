# -*- coding: utf-8 -*-
# 3. 随机生成100个标准正态的数据，并计算数据的均值与标准差
import numpy as np
from numpy.random import randn

d = np.random.randn(100)
print "avg =", np.average(d)
print "std =", np.std(d)