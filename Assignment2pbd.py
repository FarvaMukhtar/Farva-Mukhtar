#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

dfc = pd.read_csv("C:\\Users\\jsrt_metadata.txt")

dfc.head()
 


# In[36]:


# part 1
x = dfc['diagnosis'].value_counts()
plt.hist(x, color='blue', density=True)
plt.title('histogram of diagnosis')

plt.show()


# In[30]:


dfc['diagnosis']


# In[34]:


dfc.head(40)


# In[57]:


# part 2
y = dfc.groupby('diagnosis')['state'].value_counts()
a = pd.pivot_table(data=dfc, index=['diagnosis'], columns=['state'], values=['y'])
a.plot.pie( colors=['blue', 'pink', 'skyblue'], subplots=True, figsize=(12, 30))
plt.title('Diagnosis with respect to State')


plt.show()


# In[61]:



# part 3
x = dfc.groupby('diagnosis')['gender'].value_counts()

b = pd.pivot_table(data=dfc, index=['diagnosis'], columns=['gender'], values=['x'])
b.plot.pie( colors=['red', 'yellowgreen', 'darkcyan'], subplots=True, figsize=(12, 30))
plt.title('Diagnosis with respect to Gender')
plt.show()


# In[ ]:




