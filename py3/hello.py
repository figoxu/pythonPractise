#!/usr/bin/env python3

def whileSample():
    n=0
    while n<11:
        print(n)
        n+=1

whileSample()

def handleNumber():
    x=int(input("Enter An Integer:"))
    if x <= 100:
        print("Your Number Is Smaller Than Equeal To 100")
    else:
        print("Your Number Is Greater Than 100")
    if x<0:
        x=0
        print('Negative Change to zeor')
    elif x==0:
        print("Zero")
    elif x==1:
        print("Single")
    else:
        print("More")

handleNumber()

def aveage():
    count=int(input("Enter Count Of Number Which You Will Inputs:"))
    sum=0
    for i in range(0,count):
        sum=sum+int(input("Enter The {} Number:".format(i)))
    return sum/count

avg = aveage()
print(avg)
print("Average = {:.2f}".format(avg))

data = {"Figo","JianHui","Xu"}
nick,name,firstName = data
print nick
print name
print firstName





