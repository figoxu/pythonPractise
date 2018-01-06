#!/usr/bin/python3
# -*- coding:utf-8 -*-
import pandas as pd

def analysis(file, user_id):
    df = pd.read_json(file)
    v = df[df['user_id'] == user_id]['minutes']
    times = v.count()
    minutes = v.sum()
    return times,minutes
