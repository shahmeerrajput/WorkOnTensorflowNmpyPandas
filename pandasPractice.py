#!/usr/bin/env python
# coding: utf-8

# In[137]:


import pandas as pd


# # SERIES

# In[138]:


#to make series


# In[139]:


s = pd.Series(["Ali","Hamza","Zeeshan","Faiz","Adnan","Sabir"])
s


# In[140]:


Products = pd.Series(["Rio","Prince","Sooper","Gala","Chocolato","Oreo","Rite"])
Products


# In[141]:


Subjects = pd.Series(["Urdu","Islamiat","Physics","Chemistry","Zoology","Botany"])
Subjects


# In[142]:


#lable/ indexing values from series


# In[143]:


Subjects[4]


# In[144]:


Products[3]


# In[145]:


s[5]


# In[146]:


#for multiple indexing


# In[147]:


Products[[0,3]]


# In[148]:


Subjects[[1,4,2,3]]


# In[149]:


s[[1,4]]


# In[150]:


#updating or inserting values in series


# In[151]:


s[6]="Imad" #Inserted.But"Multiple values cannot be inserteed"


# In[152]:


s


# In[153]:


s[5]="Ahsan" #Updated
s


# In[154]:


#to update Multiple values


# In[155]:


s[[3,0]]=["Ikram","Nawaz"]
s


# In[156]:


# to delete value from series


# In[157]:


del s[3]


# In[158]:


s


# In[159]:


#multiple values cannot be deleted


# In[160]:


#you can also give your index as you want.i.e


# In[161]:


s1 = pd.Series([100,200,400,500,300],index=["mango","banana","apple","orange","grapes"])
s1


# # lets create series by using dictionary

# In[162]:


Student = {"Name":"A.Muqeet","FatherName":"Nasir","roll.No":"15"} 
Student


# In[163]:


s2 = pd.Series(Student)
s2


# In[164]:


s3 = pd.Series(s1, index=["mango","banana","apple","orange","grapes","Blue Berry"]) #here you can see Blue Berry is not in 
                                                                                    #index of s1,
                                                                                    #but when we put it,the value its value
                                                                                    #is shown NAN,means it is empty or Null.
s3


# In[165]:


#you can update value of Blue  Berry in s3


# In[166]:


s3["Blue Berry"]="150"
s3


# In[167]:


s3.values #by default the values is shown in float.


# In[168]:


s3.index #for index


# In[169]:


#for Boolean indexing


# In[170]:


s3>200 


# In[171]:


s3[s3>200]


# In[172]:


#to find index which is available in your series or not.i.e


# In[173]:


"pine apple" in s3 


# In[174]:


"mango" in s3


# In[175]:


pd.notnull(s3) #to find non null values


# In[176]:


#to update index of seies


# In[177]:


s4 = pd.Series(s3.values,index=["a","b","c",33,"d","e"])
s4


# # DATA FRAME

# In[178]:


df = pd.DataFrame([123,234,345,456,567]) #to create data frame


# In[179]:


df


# In[180]:


#here also you can put your own index.i.e


# In[184]:


ab = pd.DataFrame(["red","green","blue","black","orange"],index=['c1','c2','c3','c4','c5'])
ab


# In[185]:


#you can also give the name of column


# In[186]:


ab = pd.DataFrame(["red","green","blue","black","orange"],index=['c1','c2','c3','c4','c5'],columns=["colors"])
ab


# # lets create data frame in dictionary

# In[187]:


marks = {"Maths":[77,65,55,45,67,48,36,70,58,61],
         "English":[64,66,58,41,71,45,65,59,68,44],
         "Physics":[65,65,75,46,55,64,64,38,66,57],
         "Chemistry":[46,76,57,46,65,81,35,45,56,65]}
marks


# In[188]:


d1 = pd.DataFrame(marks,index=["ALi","Nawaz","Hamza","Malik","Zain","Adil","Bilal","Faiz","Shakir","Ahsan"])


# In[189]:


d1


# In[190]:


#if you have excel file then the you can use this code
#data = pd.read_cvs("file name")


# In[191]:


#to find values from data frame


# In[192]:


d1.head()#it will show first five values


# In[193]:


d1.head(4)# or put no. of data you want


# In[194]:


d1.tail()  #it will show last five values


# In[195]:


d1.tail(4) # or put no. of data you want


# In[196]:


#for information about data frame


# In[197]:


d1.info()


# In[198]:


d1.describe()  #it will decribe your frame i.e.counting,mean,standard daviation,minimum value,maximum value,etc


# In[199]:


d1.Chemistry #for information of only one index 


# In[ ]:


#if there is space in the name of index,then use this code
#d1["name of index"]


# In[200]:


#for information of more then one index


# In[204]:


d1[["Chemistry","Maths"]]


# In[205]:


#for complete information of one student


# In[209]:


d1.loc[["Faiz"]]


# In[210]:


d1.loc["Faiz"]


# In[207]:


#for complete information if multi students


# In[208]:


d1.loc[["Adil","Bilal"]]


# In[ ]:


#for information of one subject of multi students


# In[213]:


d1.loc[["Adil","Bilal"]]["Maths"]


# In[218]:


d1.loc[["Adil","Bilal"]][["Maths"]]


# In[215]:


d1.loc["Hamza"]["English"]    #for info of one sub of one student


# In[216]:


d1.loc[["Hamza"]]["English"]  


# In[217]:


d1.loc[["Hamza"]][["English"]]


# In[219]:


#you can put more values in frame.i.e


# In[221]:


d1["Practicle"]=[12,14,9,15,11,13,8,10,12,14]


# In[222]:


d1


# In[224]:


#you can also delete index


# In[225]:


del d1["Practicle"]


# In[226]:


d1


# In[227]:


#to add the marks of students


# In[232]:


d1["total"]=d1["Maths"]+ d1["English"]+ d1["Physics"]+ d1["Chemistry"]


# In[233]:


d1


# In[235]:


d1["total"]


# In[236]:


d1[["total"]]


# In[237]:


#how to get which student is pass or fail..??
#lets try to find it


# In[238]:


d1["Status"] = d1["total"]>200


# In[239]:


d1


# In[240]:


#above it is showing true and false but you want to give status of pass and fail,so...


# In[242]:


import numpy as np  # becouse where is the key of numpy


# In[248]:


d1["Status"]=np.where((d1["total"]>=200),"Pass","Fail")


# In[249]:


d1


# In[250]:


#or you can also do like that


# In[251]:


d1["Status"]=["Pass"if marks>=200 else "Fail"for marks in d1["total"]]


# In[252]:


d1


# In[253]:


#but some students got less then 40 marks in some subjects,as they are fail,but they are shown passed. So...??


# In[255]:


d1["RevisedStatus"]=np.where(((d1["Maths"]>=40) & (d1["English"]>=40) & (d1["Physics"]>=40) & (d1["Chemistry"]>=40)),"Pass","Fail")


# In[256]:


d1


# In[257]:


#be careful using brackets and during writing code..
#now lets give them new status


# In[259]:


d1["NewStatus"]=["Pass" if (math>=40) & (eng>=40) & (phy>=40) & (chem>=40) else "Fail" for math,eng,phy,chem in zip(d1["Maths"],d1["English"],d1["Physics"],d1["Chemistry"])]


# In[260]:


d1


# In[ ]:




