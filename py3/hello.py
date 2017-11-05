#coding=utf-8
#!/usr/bin/env python3

def ForElse():
    for i in range(0,10,2):
        print(i)
    else:
        print("Bye Bye")

print('-----ForElse-----')
ForElse()

def multiplication():
    print("-"*50)
    i=1
    while i<=9:
        j=1
        while j<=i:
            print( "{}X{}={:2d}".format(i,j,i*j) , end=' ')
            j+=1
        print()
        i +=1

print('---multiplication---')
multiplication()

def fibonacci():
    a,b = 0,1
    while b<100:
        print(b)
        a,b = b,a+b

print("---fibonacci---")
fibonacci()

def whileSample():
    n=0
    while n<11:
        print(n)
        n+=1


print("---while---")
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

print("---handleNumber---")
handleNumber()

def aveage():
    count=int(input("Enter Count Of Number Which You Will Inputs:"))
    sum=0
    for i in range(0,count):
        sum=sum+int(input("Enter The {} Number:".format(i)))
    return sum/count

print("---average---")
avg = aveage()
print(avg)
print("Average = {:.2f}".format(avg))

data = {"Figo","JianHui","Xu"}
nick,name,firstName = data
print(nick)
print(name)
print(firstName)





