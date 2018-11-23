# -*- coding: utf-8 -*-
import cv2
import imageio

path='/Users/xujianhui/PycharmProjects/pythonPractise/common/opencv/gifface/'
img1=cv2.imread(path+'%s'%('lg.jpg'))
img2=cv2.imread(path+'%s'%('lp.jpg'))
buff=[]
k=31
for i in range(k):
    alpha=i*1/k
    img=cv2.addWeighted(img1,alpha,img2,(1-alpha),0)
    cv2.imshow('img',img)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    buff.append(img)
    cv2.waitKey(100)
gif=imageio.mimsave('gaox.gif', buff, 'GIF', duration = 0.1)
if cv2.waitKey(0)==ord('q'):cv2.destroyAllWindows()



