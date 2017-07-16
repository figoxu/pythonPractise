# -*- coding: utf-8 -*-
#2. 矩阵计算
# (1 2 ) * (2 5)
# (3 4 )   (1 3)
import numpy as np
x = np.array([[1, 2], [3 ,4]])
y = np.array([[2, 5], [1, 3]])
print x
print y
#矩阵相乘
print x.dot(y)  # 等价于np.dot(x, y)