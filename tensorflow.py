#!/usr/bin/env python
# coding: utf-8

# # Deep Learning using tensorflow

# In[1]:


import tensorflow as tf  #tensor(matrix),differentiation,gradient,descent 


# In[2]:


from tensorflow.keras.datasets import mnist 


# In[3]:


(train_images, train_labels), (test_images, test_labels) = mnist.load_data()


# In[4]:


train_images.shape


# In[5]:


len(train_labels)


# In[6]:


test_images.shape


# In[7]:


len(test_labels)


# In[8]:


from tensorflow.keras import models  # activation function convert linearity of a function into non-linearity line ko khatam kr ky curve kr de ga
from tensorflow.keras import layers #lecture 12a # relu -ve vlue ko 0 kr det h  


# In[9]:


network = models.Sequential()# accuracy is eqaul to num of ans to actual ans (10/9)  
network.add(layers.Dense(612, activation='relu', input_shape=(28 * 28,)))#dense layer node apas me connceted ha
network.add(layers.Dense(10, activation='softmax'))# ye jo output jo ha woo hr class ki probibilityh ho gi % of probablity ko measure krta ha


# In[10]:


network.compile(optimizer='rmsprop',
loss='categorical_crossentropy',
metrics=['accuracy'])
#optimizar ka kaam weight ko measure krna
# # binary jb use krty ha jb 2 layer hoo
#using ann artifical nuetral network


# In[11]:


train_images = train_images.reshape((60000, 28 * 28))
train_images = train_images.astype('float32') / 255
test_images = test_images.reshape((10000, 28 * 28))
test_images = test_images.astype('float32') / 255


# In[12]:


from tensorflow.keras.utils import to_categorical
train_labels = to_categorical(train_labels)
test_labels = to_categorical(test_labels)


# In[13]:


network.fit(train_images, train_labels, epochs=2, batch_size=128)


# In[14]:


test_loss, test_acc = network.evaluate(test_images, test_labels)


# In[16]:


print('test_acc:', test_acc) #overfitting training and testing difference


# In[ ]:


#weight jo hota ha na woo line ka sclope hota ha


# In[ ]:




