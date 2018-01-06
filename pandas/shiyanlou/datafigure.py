#!/usr/bin/python3
# -*- coding:utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_json('user_study.json')
df2 = df.groupby('user_id').sum()

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
ax.set_xlabel('User ID')
ax.set_ylabel('Study Time')
ax.set_title('StudyData')
ax.plot(df2)
fig.show()

