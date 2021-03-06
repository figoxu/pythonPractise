#coding=utf-8
#!/usr/bin/env python3

import getopt
import sys
from multiprocessing import Process,Queue,Lock
from datetime import datetime
from configparser import ConfigParser

class Config(object):

    def __init__(self,path,city):
        self._city=city
        cfg=ConfigParser()
        cfg.read(path)
        self._config=cfg

    def get_config(self,k):
            return float(self._config[self._city][k])

    @property
    def JiShuL(self):
        return self.get_config("JiShuL")

    @property
    def JiShuH(self):
        return self.get_config("JiShuH")

    @property
    def YangLao(self):
        return self.get_config("YangLao")


    @property
    def YiLiao(self):
        return self.get_config("YiLiao")

    @property
    def ShiYe(self):
        return self.get_config("ShiYe")

    @property
    def GongShang(self):
        return self.get_config("GongShang")

    @property
    def ShengYu(self):
        return self.get_config("ShengYu")

    @property
    def GongJiJin(self):
        return self.get_config("GongJiJin")



def parseOpt(argv):
        try:
                opts,args = getopt.getopt(argv,"hC:c:d:o:",["help","C=","c=","d=","o="])
        except getopt.GetoptError:
                print("args error")
                sys.exit(2)
        city,configure,dest,output="DEFAULT","","",""
        for k,v in opts:
                if k in ("-h","--help"):
                    print("Usage: calculator.py -C cityname -c configfile -d userdata -o resultdata")
                    sys.exit()
                elif k in ("-C","--city"):
                        city=v
                elif k in ("-c","--config"):
                        configure=v
                elif k in ("-d","--dest"):
                        dest=v
                elif k in ("-o","--output"):
                        output=v
        return city,configure,dest,output



def calculator(salary,cfg):
    insurance=calInsurance(salary,cfg)
    totalTax = calTax(salary,insurance)
    income =salary-insurance-totalTax
    return income

def calTax(taxBase):
    taxBase = taxBase - 3500
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

def calInsurance(salary,cfg):
    return salary*(cfg.YangLao+cfg.YiLiao+cfg.ShiYe+cfg.GongShang+cfg.ShengYu+cfg.GongJiJin)


queue1 = Queue()
queue2 = Queue()

def readingInput(path,lock):
    with lock:
        with open(path) as file:
            data=[]
            for line in file:
                vs = line.split(",")
                k, v = vs[0].strip(), vs[1].strip()
                data.append({"k":k,"v":v})
            queue1.put(data)


def calculateInput(cfg,lock):
    with lock:
            dstr =  datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
            data=queue1.get()
            newdata=[]
            for obj in data:
                k,v=obj["k"],obj["v"]
                salary = float(v)
                insuranceBase = salary
                if salary <= cfg.JiShuL:
                    insuranceBase = cfg.JiShuL
                elif salary >= cfg.JiShuH:
                    insuranceBase = cfg.JiShuH
                insurance = calInsurance(insuranceBase, cfg)
                tax = calTax(salary - insurance)
                income = salary - insurance - tax
                data = str(k) + "," + str(v) + "," + format(insurance, ".2f") + "," + format(tax, ".2f") + "," + format(income,".2f")+","+dstr+"\n"
                newdata.append(data)
            queue2.put(newdata)

def processOuput(path,lock):
    with lock:
        with open(path, "w") as file:
            newdata = queue2.get()
            file.writelines(newdata)
        file.close()

if __name__=='__main__':
    try:
        city,configure,dest,output = parseOpt(sys.argv[1:])
        lock=Lock()
        cfg=Config(configure,city)
        Process(target=readingInput,args=(dest,lock)).start()
        Process(target=calculateInput,args=(cfg,lock)).start()
        Process(target=processOuput,args=(output,lock)).start()
    except BaseException as err:
        print(err)



