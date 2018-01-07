#!/usr/bin/python3
# -*- coding:utf-8 -*-

import pandas as pd
import matplotlib.pyplot as plt


def quarter_volume():
    data = pd.read_csv('apple.csv', header=0)
    s = data.Volume
    s.index = pd.to_datetime(data.Date)
    second_volumn = s.resample('Q').sum().sort_values()[-2]
    return second_volumn
