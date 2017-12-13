#coding=utf-8
#!/usr/bin/env python3

import sys

def calculator(salary):
    insurance=calInsurance(salary)
    totalTax = calTax(salary,insurance)
    income =salary-insurance-totalTax
    return income

def calTax(salary,insurance):
    taxBase = salary - insurance - 3500
    if taxBase<0 :
        taxBase=0
    rate, baseTax, stageBase = switchStage(taxBase)
    totalTax = (taxBase * rate) - baseTax
    return totalTax

def switchStage(income):
    if income<=1500:
        return 0.03,0,0
    elif income<=4500:
        return 0.10,105,1500
    elif income<=9000:
        return 0.20,555,4500
    elif income<=35000:
        return 0.25,1005,9000
    elif income<=55000:
        return 0.30,2755,35000
    elif income<=80000:
        return 0.35,5505,55000
    else:
        return 0.45,13505,80000


def calInsurance(salary):
    return salary*(0.08+0.02+0.005+0+0+0.06)


result=[]
try:
    for arg in sys.argv[1:]:
        vs=arg.split(':')
        salary=int(vs[1])
        income=calculator(salary)
        result.append(vs[0]+":"+format(income,".2f"))
except IndexError as e:
    print("Parameter Error")
except ValueError as e:
    print("Parameter Error")

if len(result)==len(sys.argv)-1:
    for v in result:
        print(v)