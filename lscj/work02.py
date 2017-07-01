#-*- coding:utf-8 -*-

def fc(x,y):
    return x*x-y*y

print "平方差数值计算"
v1 = input("输入数值1:");
v2 = input("输入数值2:");
print fc(v1,v2)


def pf1to100():
    pf = lambda x: x*x;
    total = 0
    for i in range(1,101):
        total += pf(i)
    return total
print "计算1到100的平方和"
print pf1to100()

def chkNum(num):
    return num<=100
v3 = input("输入数值,判断数值是否小于100，请输入:");
print chkNum(v3)


def Encry(num):
    arr = []
    for i in str(num):
        arr.append(i)
    arr[0],arr[3]=arr[3],arr[0]
    arr[1],arr[2]=arr[2],arr[1]
    for i in range(0,len(arr)):
        arr[i]=(int(arr[i])+5)%10
    return ''.join(str(i) for i in arr)

def Dencry(num):
    arr = []
    for i in str(num):
        arr.append(i)
    arr[0],arr[3]=arr[3],arr[0]
    arr[1],arr[2]=arr[2],arr[1]
    for i in range(0,len(arr)):
        arr[i]=(int(arr[i])+5)%10
    return ''.join(str(i) for i in arr)

v4 = input("输入需要加密的数值，长度为5位，请输入:");
encryVal = Encry(v4)
print "加密后数值为："+encryVal
print "解密后数值为："+Dencry(encryVal)












