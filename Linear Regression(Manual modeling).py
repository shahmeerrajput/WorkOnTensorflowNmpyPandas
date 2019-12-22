#!/usr/bin/env python
# coding: utf-8

# In[3]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[6]:


df=pd.read_csv('weight-height.csv')


# In[7]:


df.head()


# In[8]:


df.describe()


# In[9]:


df.plot(kind='scatter', x='Height', y='Weight', 
       title='Weight and Height in adults')


# In[19]:


df.plot(kind='scatter', x='Height', y='Weight', 
       title='Weight and Height in adults')
plt.plot([55,78], [75,250], color='yellow', linewidth=5)


# # Our MOdel

# In[11]:


def line(x, w=0, b=0):
    y=w*x+b  #y=mx+c
    return  y


# # Cost Function

# In[12]:


def mean_squared_error(y_true, y_pred):
    s=(y_true-y_pred)**2
    return s.mean()


# In[13]:


X=df[['Height']].values
y_true=df[['Weight']].values


# In[45]:


y_pred=line(X,7.720096,-350.8536)  #y=mx+c


df.plot(kind='scatter', x='Height', y='Weight', 
       title='Weight and Height in adults')

plt.plot([55,78], [75,250], color='yellow', linewidth=3)

plt.plot(X,y_pred, color='red', linewidth=3)


# In[15]:


mean_squared_error(y_true,y_pred)


# In[ ]:





# In[ ]:





# In[ ]:




