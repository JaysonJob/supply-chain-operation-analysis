#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


# Load the CSV
df = pd.read_csv(r"C:\Users\Administrator\Desktop\operation_data.csv")


# In[6]:


# sumarry statistics
df.describe().transpose()


# In[20]:


# checking the data types
df.dtypes


# In[22]:


# checking the data i formation
df.info()


# In[19]:


#checking the shape
df.shape


# In[8]:


#category columns
df.describe(include = 'object').T


# In[12]:


# View all column names
print(df.columns.tolist())


# In[14]:


#checking for nulls
df.duplicated().sum()


# In[17]:


# checking for nulls
df.isnull().sum()


# In[ ]:




