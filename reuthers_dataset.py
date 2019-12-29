#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tensorflow


# In[2]:


from tensorflow.keras.datasets import reuters


# In[3]:


(train_data, train_labels), (test_data, test_labels) = reuters.load_data(
num_words=10000)


# In[5]:


import numpy as np
def vectorize_sequences(sequences, dimension=10000):
    results = np.zeros((len(sequences), dimension))
    for i, sequence in enumerate(sequences):
        results[i, sequence] = 1.
    return results
x_train = vectorize_sequences(train_data)
x_test = vectorize_sequences(test_data)


# In[6]:


def to_one_hot(labels, dimension=46):
    results = np.zeros((len(labels), dimension))
    for i, label in enumerate(labels):
        results[i, label] = 1.
    return results
one_hot_train_labels = to_one_hot(train_labels)
one_hot_test_labels = to_one_hot(test_labels)


# In[19]:


from tensorflow.keras import models
from tensorflow.keras import layers
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=(10000,))) # wahan pr one_hot encode ki ha isi liye 1000 ki list bano ha agar kio word nahi ha to wahan 0 aye ga
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(46, activation='softmax')) #sigmoid binary class, softmax multiclass


# In[20]:


model.compile(optimizer='rmsprop',
loss='categorical_crossentropy',
metrics=['accuracy']) # ye metric me accuray,precision,recall
#accuray = corrrt / total true me kitni accuracy ha or false me kitny accuray ha auuracy nhi kr pata 
# precision = TP / TP + FP , recall = TP / TP + FN 


# In[21]:


x_val = x_train[:1000]
partial_x_train = x_train[1000:]
y_val = one_hot_train_labels[:1000]
partial_y_train = one_hot_train_labels[1000:]


# In[22]:


history = model.fit(partial_x_train,
partial_y_train,
epochs=10,
batch_size=512, #sirf 10,000 me sy 512 ek epoch me
validation_data=(x_val, y_val))

# question   1.confusion matric() = TP(pridiction true thi or ans true),FP(pridiction true thi or ans false),NP(pridiction false thi or ans false),TN(pridiction false thi or ans true)
# precision = TP / TP + FP , recall = TP / TP + FN 


# In[24]:


import matplotlib.pyplot as plt
loss = history.history['loss']
val_loss = history.history['val_loss']
epochs = range(1, len(loss) + 1)
plt.plot(epochs, loss, 'bo', label='Training loss')
plt.plot(epochs, val_loss, 'b', label='Validation loss')
plt.title('Training and validation loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.show()


# In[ ]:




