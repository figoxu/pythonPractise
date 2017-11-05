#!/usr/bin/env python3

import sys
from collections import Counter

class Person(object):
    """
    返回具有给定名称的 Person 对象
    """

    def __init__(self, name):
        self.name = name

    def get_details(self):
        """
        返回包含人名的字符串
        """
        return self.name

    def get_grade(self):
        print("UnDefined")


class Student(Person):
    """
    返回 Student 对象，采用 name, branch, year 3 个参数
    """

    def __init__(self, name, branch, year,score):
        Person.__init__(self, name)
        self.branch = branch
        self.year = year
        self.score = score

    def get_details(self):
        """
        返回包含学生具体信息的字符串
        """
        return "{} studies {} and is in {} year.".format(self.name, self.branch, self.year)

    def get_grade(self):
        data={"Pass":0,"Fail":0}
        for k,v in Counter(self.score).items() :
            if k=="A" or k=="B" :
                data["Pass"] += v
            else:
                data["Fail"] += v
        printMap(data.items())

class Teacher(Person):
    """
    返回 Teacher 对象，采用字符串列表作为参数
    """
    def __init__(self, name, papers,score):
        Person.__init__(self, name)
        self.papers = papers
        self.score = score

    def get_details(self):
        return "{} teaches {}".format(self.name, ','.join(self.papers))

    def get_grade(self):
        printMap(Counter(self.score).items())
        
def printMap(items) :
    i=0
    for k,v in items :
        print("{}: {}".format(k,v),end=" ")
        if i<len(items)-1 :
            print(",",end="")
        i += 1

if len(sys.argv) >=3 :
   tp,score=sys.argv[1],sys.argv[2]
   if tp=="teacher" :
       Teacher('', [],score).get_grade()
   elif tp=="student":
       Student('', '', 0,score).get_grade()
