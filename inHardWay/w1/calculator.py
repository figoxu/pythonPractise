#coding=utf-8
#!/usr/bin/env python3
import sys

def calculator(salary):
    taxBase = salary-3500
    if taxBase<0:
        return 0
    tax = taxRange(taxBase,0,1500,0.03)
    tax = tax + taxRange(taxBase,1500,4500,0.10)
    tax = tax + taxRange(taxBase,4500,9000,0.20)
    tax = tax + taxRange(taxBase,9000,35000,0.25)
    tax = tax + taxRange(taxBase,35000,55000,0.30)
    tax = tax + taxRange(taxBase,55000,80000,0.35)
    tax = tax + taxRange(taxBase,80000,2147483647,0.03)
    return tax

def taxRange(taxBase,lower,upper,rate):
    if taxBase<lower:
        return 0
    elif taxBase>upper:
        return (upper-lower)*rate
    else:
        return (taxBase-lower)*rate


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