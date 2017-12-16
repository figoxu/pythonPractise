#coding=utf-8
#!/usr/bin/env python3

import getopt
import sys

class Config(object):

    def __init__(self,path):
        self._config={}
        with open(path) as file:
            for line in file:
                vs=line.split("=")
                k,v=vs[0].strip(),vs[1].strip()
                self._config[k]=v

    def get_config(self,k):
            return float(self._config[k])

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

class Data(object):
    def __init__(self,path):
        self._data={}
        with open(path) as file:
            for line in file:
                vs = line.split(",")
                k,v=vs[0].strip(),vs[1].strip()
                self._data[k]=v
    def caculator(self,config):
        outdata=[]
        for (k,v) in self._data.items():
            salary=float(v)
            insuranceBase=salary
            if salary<=config.JiShuL:
                insuranceBase=config.JiShuL
            elif salary>=config.JiShuH:
                insuranceBase=config.JiShuH
            insurance = calInsurance(insuranceBase,config)
            tax =calTax(salary-insurance)
            income=salary-insurance-tax
            outdata.append(str(k)+","+str(v)+","+format(insurance,".2f")+","+format(tax,".2f")+","+format(income,".2f"))
        return outdata

    def dumptofile(self,output,cfg):
        outdata=self.caculator(cfg)
        with open(output,"w") as file:
            for v in outdata:
                file.write(v+"\n")
        file.close()

def parseOpt(argv):
        try:
                opts,args = getopt.getopt(argv,"c:d:o:",["c=","d=","o="])
        except getopt.GetoptError:
                print("args error")
                sys.exit(2)
        configure,dest,output="","",""
        for k,v in opts:
                if k in ("-c","--config"):
                        configure=v
                elif k in ("-d","--dest"):
                        dest=v
                elif k in ("-o","--output"):
                        output=v
        return configure,dest,output



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



if __name__=='__main__':
    try:
        configure,dest,output = parseOpt(sys.argv[1:])
        cfg=Config(configure)
        data=Data(dest)
        data.dumptofile(output,cfg)
    except BaseException as err:
        print(err)



