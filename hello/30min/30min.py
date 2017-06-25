#coding=utf-8
import os

#30min python in action
def main():
    print 'Hello World!'

    print "Figo\'s Hello World"
    foo(5,10)
    print '='*10
    print '当前路径：'+os.getcwd()
    counter= 0
    counter +=1

    food = ['苹果','杏子','李子','梨']
    for i in food:
        print '水果我喜欢：'+i

    for i in range(10):
        print i


'''
    多行注释
    这是一个函数
'''
def foo(param1,secondParam):
    res=param1+secondParam
    print '%s 加 %s 等于 %s'%(param1,secondParam,res)
    if res<50:
        print '小与50'
    elif res>=50 and  (param1==42 or secondParam==24):
        print '复杂运算'
    else:
        print "其它"




if __name__ == '__main__':
    main()