#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Load the CSV file into a dataframe and drop the extra unnamed index column
import pandas as pd

df = pd.read_csv('operation_data.csv', index_col=0)
df.head()


# In[6]:


# Standardize text columns
for col in ['Supplier Name', 'Warehouse Location', 'Order Fulfillment Status']:
    df[col] = df[col].str.strip()


# In[2]:


# Clean up text columns by remove extra whitespace and list unique values to spot typos and inconsistencies
text_cols = ['Supplier Name', 'Warehouse Location', 'Order Fulfillment Status']
for col in text_cols:
    df[col] = df[col].str.strip()

for col in text_cols:
    print(col, "->", df[col].unique())


# In[3]:


# Check numeric columns for negative values or that dont exist also to show any negatives
num_cols = ['Current Stock Level','Reorder Point','Lead Time','Daily Demand Rate','Shipping Cost']
print(df[num_cols].describe())
print((df[num_cols] < 0).sum())


# In[4]:


# Confirm SKU is a valid unique identifier (no repeated IDs)
print("Unique SKUs:", df['SKU'].nunique(), "vs rows:", len(df))


# In[9]:


# 1.Which SKUs are at risk of stockout right now?
df['At Risk'] = df['Current Stock Level'] < df['Reorder Point']
at_risk = df[df['At Risk']]
print(f"{df['At Risk'].sum()} out of {len(df)} SKUs")


# In[12]:


# Q2: Which SKUs are most urgent (fewest days of stock left)?
df['Days of Stock'] = df['Current Stock Level'] / df['Daily Demand Rate']
urgent = df.sort_values('Days of Stock').head(10)
print(urgent)


# In[18]:


# 3.Which warehouses have the worst fulfillment performance?
warehouse_status = pd.crosstab(df['Warehouse Location'], df['Order Fulfillment Status'], normalize='index')
print(warehouse_status)


# In[ ]:





# In[ ]:





# In[20]:


# 4.Which suppliers are least reliable?
supplier_status = pd.crosstab(df['Supplier Name'], df['Order Fulfillment Status'])
print(supplier_status)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




