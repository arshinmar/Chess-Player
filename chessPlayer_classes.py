#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 17:11:57 2019

@author: Admin
"""

class tree:
        def __init__(self,x):
                self.value=x
                self.store=[self.value,[]]
        def AddSuccessor(self,x):
                self.store[1]+=[x]
                return True
        def GetSuccessors(self):
                return self.store[1]
        def Print_DepthFirst(self):
                self.TruePrint("")
                return True
        def TruePrint(self,prefix):
                print(prefix+str(self.store[0]))
                for i in self.store[1]:
                        i.TruePrint(prefix+"   ")
                return True
        def GetLevelOrder(self):
                x=queue()
                x.push(self.store)
                accum=[]
                while True:
                        blah=x.pop()
                        if blah==False:
                                break
                        accum+=[blah[0]]
                        for ex in blah[1]:
                                x.push(ex.store)
                return accum

class queue:
        def __init__(self):
                self.store=[]
        def push(self,values):
                self.store+=[values]
                return True
        def pop(self):
                if len(self.store)==0:
                        return False
                else:
                        r=self.store[0]
                        self.store=self.store[1:len(self.store)]
                        return r
        def empty(self):
                if len(self.store)==0:
                        return True
                return False