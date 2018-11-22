# -*- coding: utf-8 -*-
"""
认识shapefile功能
"""

import matplotlib
matplotlib.use("TkAgg")
from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
# 构建地图实例
m = Basemap(projection='merc',
            llcrnrlon=73,
            llcrnrlat=15,
            urcrnrlon=135,
            urcrnrlat=55,
            resolution='c',
            lat_0=38.5,
            lon_0=95)

# 中国省份数据
filename = '/Users/xujianhui/Downloads/CHN_adm_shp/CHN_adm1'
# 使用shapefile读取文件，必须指定两个参数：路径和名字
# 但是不要加扩展名！
m.readshapefile(filename, 'CHN_adm1')
m.drawmapboundary()
m.fillcontinents(color='#78D2F9', lake_color='#4AF2A1')
# m.drawcoastlines()

# shapfile读取的文件是这个样子的：
# 包含很多块数据
print(len(m.CHN_adm1_info))
# 每个省份一块
print(m.CHN_adm1_info[0])
# 每个省份区域由若干个点构成
print(m.CHN_adm1[0])


plt.show()
# time.sleep(8)
# plt.delaxes()