#!/usr/bin/env python
# coding: utf-8

# In[7]:


import tensorflow 
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense 
from tensorflow.keras.optimizers import Adam, SGD

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# In[8]:


df=pd.read_csv('weight-height.csv')


# In[22]:


X=df[['Height']].values
y_true=df[['Weight']].values


# In[23]:


X


# In[11]:


model = Sequential()
model.add(Dense(1, input_shape=(1,)))


# In[12]:


model.summary()


# In[13]:


model.compile(Adam(lr=0.8), 'mean_squared_error')


# In[14]:


model.fit(X,y_true, epochs=40)


# In[15]:


y_pred=model.predict(X)


# In[16]:


df.plot(kind='scatter',
       x='Height',
       y='Weight', title='Weight and Height in adults')
plt.plot(X, y_pred, color='red', linewidth=3)


# In[17]:


w,b=model.get_weights()


# In[18]:


w


# In[19]:


b


# In[ ]:




