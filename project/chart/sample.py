# -- coding:utf-8 --
import matplotlib.pyplot as plt
import matplotlib
from matplotlib.font_manager import FontProperties

#指定特殊字体的办法
#myfont = FontProperties(fname="/usr/local/lib/python3.6/site-packages/matplotlib/mpl-data/fonts/ttf/simhei.ttf")
# plt.title("绘制折线图",fontproperties=myfont)
# plt.ylabel("y轴",fontproperties=myfont)
# plt.xlabel("x轴",fontproperties=myfont)

plt.rcParams['font.family']=['SimHei']
print(matplotlib.matplotlib_fname())
x = [5, 4, 66, 1]
y = [7, 8, 9, 10]

plt.plot(x, y, 'b', label='XXX1', linewidth=2)

plt.title("绘制折线图")
plt.ylabel("y轴")
plt.xlabel("x轴")
plt.savefig('折线图', dpi=72)


# 把字体文件放入 matplotlib 的font目录下，在清除下列目录的缓存
# print(matplotlib.get_cachedir())
# 新安装的字体会出现在下列列表
for i in sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist]):
    print(i)

plt.show()
