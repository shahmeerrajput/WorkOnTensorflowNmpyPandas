#!/usr/bin/env python
# coding: utf-8

# # Boolean Indexing

# In[2]:


import numpy as np


# In[3]:


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])


# In[4]:


data = np.random.randn(7, 4)


# In[5]:


names


# In[6]:


data


# In[7]:


names == 'Bob'


# In[8]:


data[names == 'Bob']


# In[9]:


data[names != 'Bob']


# In[12]:


data[names == 'Bob', 1:3]


# In[11]:


data


# In[13]:


data[3]


# In[14]:


data[[3,4,0,1]]


# In[15]:


cond = names == 'Bob'


# In[16]:


cond


# In[19]:


data[~(cond)]


# In[25]:


mask = (names == 'Bob') | (names == 'Will')


# In[21]:


mask


# In[22]:


names


# In[23]:


data[mask]


# In[26]:


data < 0


# In[27]:


data[data < 0]


# In[28]:


data[data < 0] = 0


# In[29]:


data


# # Fancy Indexing

# In[30]:


arr = np.empty((8, 4))


# In[31]:


for i in range(8):
    arr[i] = i


# In[32]:


arr


# In[36]:


arr[4]


# In[37]:


arr[[4,6]]


# In[41]:


arr[[4,6], 2:]


# In[42]:


arr = np.arange(32).reshape((8, 4))


# In[43]:


arr


# In[44]:


arr[[1, 5, 7, 2], [0, 3, 1, 2]]


# In[46]:


arr


# In[45]:


arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]]

#1[0,3,1,2], 5[0,3,1,2], 7[0,3,1,2], 2[0,3,1,2]
#[(1,0),(1,3),(1,1),(1,2)] and so on


# # Transposing Arrays and Swapping Axes

# In[47]:


arr = np.arange(15).reshape((3, 5))


# In[48]:


arr


# In[49]:


arr.T


# In[50]:


arr = np.random.randn(7) * 5


# In[51]:


arr


# In[52]:


remainder, whole_part = np.modf(arr)


# In[53]:


remainder


# In[54]:


whole_part


# # Array-Oriented Programming with Arrays

# In[55]:


names = ['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe']


# In[57]:


names


# In[58]:


names = set(names)


# In[59]:


names


# In[60]:


students = {'Ali','Nasir','Mohsin', 'Ali'}


# In[61]:


students


# In[67]:


arr = np.arange(24)


# In[71]:


arr.reshape((4, -1))


# In[88]:


arr = np.arange(15).reshape((5, 3))


# In[73]:


arr


# In[74]:


arr.ravel()


# In[75]:


arr.flatten()


# In[76]:


arr


# In[89]:


flat = arr.flatten()


# In[78]:


arr


# In[81]:


ravel = arr.ravel()


# In[80]:


arr


# In[83]:


ravel


# In[90]:


flat


# In[85]:


ravel[2:8] = 0


# In[86]:


ravel


# In[87]:


arr


# In[91]:


flat[2:8] = 0


# In[92]:


arr


# In[94]:


arr1 = np.array([[1, 2, 3], [4, 5, 6]])
arr1


# In[95]:



arr2 = np.array([[7, 8, 9], [10, 11, 12]])
arr2


# In[97]:


np.concatenate([arr1,arr2])


# In[98]:


np.concatenate([arr1,arr2],axis=0)


# In[99]:


np.concatenate([arr1,arr2],axis=1)


# In[100]:


splitt =np.arange(1,25).reshape(6,4)
splitt


# In[104]:


np.vsplit(splitt,2)


# In[106]:


np.hsplit(splitt,2)


# In[110]:


arr=np.array([1,2,3,4])
a=np.broadcast(arr,4)


# In[111]:


a


# In[3]:


def tof(n,a,b,c):
    if(n>0):
        tof(n-1,a,c,b)
        print(a , "-" ,c)
        tof(n-1,b,a,c)


# In[4]:


tof(3,1,2,3)


# In[ ]:




