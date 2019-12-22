#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import math as mt
from IPython.display import Markdown, display
def printmd(string):
    display(Markdown(string))


# In[2]:


def DectoBin(num):
    x = np.absolute(num)
    Bin = ""
    for i in range(1,33):
        if x > 1:
            Bin = (str)(x%2) + Bin
            x = (int)(x/2)
        elif x <= 1: 
            Bin = (str)(x%2) + Bin
            x = 0
        else:
            Bin = (str)(0) + Bin
            
    compActive = 0
    if(num < 0):
        for i in range(31,-1,-1):
            if compActive == 0 and Bin[i] == '1':
                compActive = 1
            elif compActive == 1:
                twoscomp = ((int)(Bin[i]) - 1)**2
                lst = list(Bin)
                lst[i] = str(twoscomp)
                Bin = "".join(lst)          
    return (str)(Bin)

def BintoDec(num):
    sum = 0
    if(num[0] == "0"):
        for i in range(1,33):
            sum = sum + (int((num[len(num)-i]))*(2**(i-1)))
        return sum
    else:
        for i in range(1,32):
            sum = sum + (int((num[len(num)-i]))*(2**(i-1)))
        sum = sum - (int((num[0]))*(2**(31)))
        return sum



class MyJaggedArray:
    def __init__(self,JALen):
        self.mem = [None]*(JALen*40)
        self.JALen = JALen
        self.inArrLenArr = [0]*JALen
        i = 0
        while (i < self.JALen):
            inArrLen = int(input(f"Enter {i+1} Array Length :"))
            if(inArrLen <= 10 and inArrLen > 0):
                self.inArrLenArr[i] = inArrLen
                for j in range(0,inArrLen):
                    data = int(input(f"Enter {i+1}, {j+1} Values : "))
                    data = DectoBin(data)
                    self.setValuestoMem(data,((i*40)+(j*4)))
            else:
                print("Lenght must be between 1 to 10")
                i = i -1
            i = i+1
                
    def setValuestoMem(self,data,index):
        count = 0
        for i in range(0,4):
            self.mem[index+i] = data[count:count+8]
            count = count + 8
            
    def getAllValues(self):
        printmd("<span style='color:green; font-size:22px'><b>My Jagged Array Values</b></span>")
        for i in range(0,self.JALen):
            print(f"Base Address is :",(i*40))
            for j in range(0,self.inArrLenArr[i]):
                val = self.mem[((i*40)+(j*4))]
                val = val + self.mem[((i*40)+(j*4))+1]
                val = val + self.mem[((i*40)+(j*4))+2]
                val = val + self.mem[((i*40)+(j*4))+3]
                print(BintoDec(val) , end =" ")
            print("")
        
    def printMem(self):
        printmd("<span style='color:green; font-size:22px'><b>Memory</b></span>")
        for i in range(0,len(self.mem)):
            print(self.mem[i])
            
    


# In[3]:


while True:
    JALen = int(input("Enter Jaggaed Array Length : "))
    if JALen <= 0 or JALen > 10:
        print("Jagged Array Length must be Between 1 to 10")
    else:
        break
        
obj = MyJaggedArray(JALen)
obj.getAllValues()


# In[4]:


obj.printMem()


# In[ ]:




