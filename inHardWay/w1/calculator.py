#coding=utf-8
#!/usr/bin/env python3
import sys

def calculator(salary):
    insurance=calInsurance(salary)
    taxBase=salary-insurance-3500
    rate,baseTax,stageBase=switchStage(taxBase)
    totalTax = (taxBase-stageBase)*rate+baseTax
    income =salary-insurance-totalTax
    return income

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



try:
    salary = int(sys.argv[1])
    tax = calculator(salary)
    print(format(tax,".2f"))
except IndexError:
    # print("Please Input Salary")
    print("Parameter Error")
except ValueError:
    # print("Bad Salary Value:",sys.argv[1])
    print("Parameter Error")