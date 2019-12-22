#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


x = np.random.rand(10)
print(x)
y = np.random.rand(10)
print(y)


# In[3]:


x=np.arange(1,10).reshape(3,3)


# In[4]:


x


# In[5]:


m =np.arange(16).reshape(4,4)


# In[6]:


m


# In[7]:


d=np.arange(50).reshape(2,5,5)
d


# In[8]:


d[1][2][2]


# In[9]:


d[1,2:,2:]


# In[ ]:





# In[10]:


d<20


# In[11]:


d


# In[12]:


d>0


# In[18]:


bollarr = np.array([False,False,True,True,False,True],dtype="bool")


# In[19]:


d2=np.arange(36).reshape(6,6)


# In[20]:


d2


# In[21]:


d2[bollarr]


# In[22]:


d2.T


# In[23]:


d2


# In[24]:


import pandas as pd


# In[28]:


d1={"name":"athar","AIM":"AI","Institute":"PIAIC","timing":"5-10",}


# In[29]:


pd.Series(d1)


# In[31]:


l2=pd.Series([25000,30000,40000],index=["4th gen","5th gen","6th gen"])


# In[32]:


l2


# In[34]:


l2[2]=20000


# In[35]:


l2


# In[36]:


l2.values


# In[37]:


l2.index


# In[38]:


l2>30000


# In[41]:


l2[l2>20000]


# In[47]:


"5th gen" in l2


# In[55]:


s3=pd.DataFrame([11000,22000,33000,44000,55000])


# In[56]:


s3


# In[68]:


s3.column=["ATHAR","NASIR","ANEES","ALI","NOUMAN"]


# In[69]:


s3


# In[73]:


c=pd.DataFrame(["red","green","blue"],index=["C1","C2","C3"],columns=["Colors"])


# In[74]:


c


# In[91]:


data={"Qualification":["BSCS","BESE","ACCA","AI"],
      "Salary":[520000,40040,342000,432200],
      "Experience":["2 YEARS","5 YEARS","1 YEARS","4 YEARS"],
      "Address":["Hadeed","Hadeed","Korangi","DHA"],
     "Contact":["030220","034533","033445","030442",],
     "Promotion":["Next Month","After 2 Months","After A Year","Not Now"],}


# In[92]:


lis=pd.DataFrame(data,index=["Harry","Alex","Luqas","Billi"])


# In[90]:


lis


# In[97]:


st={"maths":[55,66,77,34],
    "chemistry":[88,33,54,23],
    "physics":[54,77,33,23],
    "english":[35,57,23,32],
}


# In[122]:


d2=pd.DataFrame(st,index=["Athar","Ashir","Asghar","Hamza"])


# In[123]:


d2


# In[124]:


d2.tail(2)


# In[125]:


d2["maths"]


# In[126]:


d2.loc[["Athar","Asghar"]]["english"]


# In[127]:


d2["Faltu"]=range(4)


# In[130]:


del d2["Faltu"]


# In[131]:


d2


# In[132]:


d2["Total"]=d2["maths"]+d2["chemistry"]+d2["physics"]+d2["english"]


# In[133]:


d2


# In[ ]:




