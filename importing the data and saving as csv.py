#!/usr/bin/env python
# coding: utf-8

# In[3]:


# importing the request to import data as json
import requests


# In[4]:


# the link from github as raw from the file you generated from mockaroo
url ='https://raw.githubusercontent.com/JaysonJob/data/refs/heads/main/Operational%20data.json'


# In[5]:


operation_data = requests.get(url)


# In[6]:


operation_data.status_code


# In[7]:


content = operation_data.json()


# In[8]:


content


# In[9]:


type(content)


# In[12]:


operation = content[:50]


# In[13]:


len(operation)


# In[14]:


# importing the relevant library
import pandas as pd


# In[16]:


df = pd.DataFrame(operation)


# In[17]:


# checking the first 5 rows 
df.head()


# In[18]:


# saving the json file as csv to file explorer
df.to_csv('operation_data.csv')


# In[ ]:




