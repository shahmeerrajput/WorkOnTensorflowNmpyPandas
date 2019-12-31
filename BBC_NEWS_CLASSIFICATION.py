#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


import os
# print(os.listdir("../input"))

# Any results you write to the current directory are saved as output.
import itertools
import os

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tensorflow as tf

from sklearn.preprocessing import LabelBinarizer, LabelEncoder
from sklearn.metrics import confusion_matrix

from tensorflow import keras
layers = keras.layers
models = keras.models


# In[4]:


data = pd.read_csv("bbc-text.csv")


# In[6]:


data 


# In[7]:


data.shape


# In[8]:


data.head(7)


# In[9]:


data['category'].value_counts()


# In[13]:


train_size = int(len(data) * .8)
print ("Train size: ",train_size)
print ("Test size: %d" % (len(data) - train_size))


# In[14]:


def train_test_split(data, train_size):
    train = data[:train_size]
    test = data[train_size:]
    return train, test


# In[15]:


train_cat, test_cat = train_test_split(data['category'], train_size)
train_text, test_text = train_test_split(data['text'], train_size)


# In[16]:


test_text


# In[17]:


max_words = 1000
tokenize = keras.preprocessing.text.Tokenizer(num_words=max_words,                                               char_level=False)


# In[18]:


tokenize.fit_on_texts(train_text) # fit tokenizer to our training text data
x_train = tokenize.texts_to_matrix(train_text)
x_test = tokenize.texts_to_matrix(test_text)


# In[ ]:





# In[19]:


encoder = LabelEncoder()
encoder.fit(train_cat)
y_train = encoder.transform(train_cat)
y_test = encoder.transform(test_cat)


# In[20]:


# Converts the labels to a one-hot representation
num_classes = np.max(y_train) + 1
y_train = keras.utils.to_categorical(y_train, num_classes)
y_test = keras.utils.to_categorical(y_test, num_classes)


# In[21]:


print('x_train shape:', x_train.shape)
print('x_test shape:', x_test.shape)
print('y_train shape:', y_train.shape)
print('y_test shape:', y_test.shape)


# In[22]:


batch_size = 32
epochs = 4
drop_ratio = 0.5


# In[23]:


model = models.Sequential()
model.add(layers.Dense(512, input_shape=(max_words,)))
model.add(layers.Dense(212 , activation = 'relu'))
model.add(layers.Activation('relu'))
model.add(layers.Dense(num_classes))
model.add(layers.Activation('softmax'))

model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])


# In[24]:


history = model.fit(x_train, y_train,batch_size=batch_size,epochs=epochs,verbose=1,validation_split=0.1)


# In[25]:


score = model.evaluate(x_test, y_test,                       batch_size=batch_size, verbose=1)


# In[26]:


print('Test loss:', score[0])
print('Test accuracy:', score[1])


# In[27]:


# model.predict(x_train[0])
x_train[0].shape


# # Hyperparameter tunning

# This is a good time to go back and tweak some parameters such as epoch, batch size, dropout ratio, network structure, activation function, and others, to see if you can improve the accuracy.
# 
# In this particular case, to make it more challenging, I recommend reducing the max words of the call to keras.preprocessing.text.Tokenizer. This will reduce the number of words for each input sample, thus making it more challenging to accurately predict the category. (Notice that not all hyperparameters are necessarily inside the model. This is one such example.)
# 
# The default was up to 1000 words per article. See what happens when you reduce that number to 200 words, or 50 words, or even fewer. As the evaluation accuracy drops, the effects of your hyperparameter tuning will be more pronounced, with successful adjustments making meaningful improvements to the model performance.
# 
# To make this process easier to manage, I've encapulated the model definition and training and evaluation calls into one function call. You can add additional parameters as needed.

# In[28]:


#by using hyperprameter tunning

def run_experiment(batch_size, epochs, drop_ratio):
  print('batch size: {}, epochs: {}, drop_ratio: {}'.format(
      batch_size, epochs, drop_ratio))
  model = models.Sequential()
  model.add(layers.Dense(512, input_shape=(max_words,)))
  model.add(layers.Activation('relu'))
  model.add(layers.Dropout(drop_ratio))
  model.add(layers.Dense(num_classes))
  model.add(layers.Activation('softmax'))

  model.compile(loss='categorical_crossentropy',
                optimizer='adam',
                metrics=['accuracy'])
  history = model.fit(x_train, y_train,
                    batch_size=batch_size,
                    epochs=epochs,
                    verbose=0,
                    validation_split=0.1)
  score = model.evaluate(x_test, y_test,
                       batch_size=batch_size, verbose=0)
  print('\tTest loss:', score[0])
  print('\tTest accuracy:', score[1])


# In[29]:


batch_size = 16
epochs = 4
drop_ratio = 0.4
run_experiment(batch_size, epochs, drop_ratio)


# In[30]:


text_labels = encoder.classes_

for i in range(10):
    prediction = model.predict(np.array([x_test[i]]))
    predicted_label = text_labels[np.argmax(prediction)]
    print(test_text.iloc[i][:50], "...")
    print('Actual label:' + test_cat.iloc[i])
    print("Predicted label: " + predicted_label + "\n")  


# In[31]:


test_text.iloc[3]


# In[32]:


prediction = model.predict(np.array([x_test[3]]))


# In[33]:


prediction


# In[34]:


predicted_label = text_labels[np.argmax(prediction)]
predicted_label


# In[35]:


#print(test_text.iloc[:50], "...")
print('Actual label:' + test_cat.iloc[3])
print("Predicted label: " + predicted_label + "\n") 

