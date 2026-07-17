#!/usr/bin/env python
# coding: utf-8

# In[5]:


#importing the required python libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[4]:


sns.set_style("whitegrid")

df = pd.read_csv('operation_data.csv')

for col in ['Supplier Name', 'Warehouse Location', 'Order Fulfillment Status']:
    df[col] = df[col].str.strip()

df['At Risk'] = df['Current Stock Level'] < df['Reorder Point']
df['Days of Stock'] = df['Current Stock Level'] / df['Daily Demand Rate']
df.head()


# In[6]:


# 1. Histogram: Current Stock Level vs Reorder Point
# Overlaying the two distributions shows whether stock levels across SKUs
# are generally sitting above or below the reorder threshold, and how much
# overlap (risk zone) exists between them.

plt.figure(figsize=(8, 5))
sns.histplot(df['Current Stock Level'], color='steelblue', label='Current Stock Level', kde=True, alpha=0.5)
sns.histplot(df['Reorder Point'], color='orange', label='Reorder Point', kde=True, alpha=0.5)
plt.title('Distribution: Current Stock Level vs Reorder Point')
plt.xlabel('Units')
plt.legend()
plt.tight_layout()
plt.show()


# In[7]:


# 2. Bar Chart: Top 10 Most Urgent SKUs
# Ranks the SKUs with the fewest remaining days of stock, making it
# immediately clear which items need reordering first.

urgent = df.sort_values('Days of Stock').head(10)

plt.figure(figsize=(8, 5))
sns.barplot(data=urgent, x='Days of Stock', y='SKU', hue='At Risk', dodge=False, orient='h')
plt.title('Top 10 Most Urgent SKUs (Fewest Days of Stock Left)')
plt.xlabel('Days of Stock Remaining')
plt.ylabel('SKU')
plt.tight_layout()
plt.show()


# In[8]:


# 3. Boxplot: Shipping Cost by Warehouse Location
# Compares the spread and median shipping cost across warehouses, helping
# spot which locations are consistently more expensive to ship from, or
# which have unusually wide cost variation.

plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='Warehouse Location', y='Shipping Cost', hue='Warehouse Location', palette='Set2', legend=False)
plt.title('Shipping Cost Distribution by Warehouse Location')
plt.tight_layout()
plt.show()


# In[9]:


# 4. Heatmap: Warehouse Location vs Order Fulfillment Status
# A normalized crosstab heatmap shows the proportion of each fulfillment
# outcome (On Time, Backordered, etc.) per warehouse, making it easy to
# spot underperforming locations at a glance.

warehouse_status = pd.crosstab(df['Warehouse Location'], df['Order Fulfillment Status'], normalize='index')

plt.figure(figsize=(8, 5))
sns.heatmap(warehouse_status, annot=True, fmt='.0%', cmap='YlOrRd')
plt.title('Fulfillment Status Rate by Warehouse')
plt.tight_layout()
plt.show()


# In[10]:


# 5. Scatterplot: Lead Time vs Daily Demand Rate (colored by At Risk)
# Plots each SKU by its supplier lead time against how fast it sells,
# colored by stockout risk. SKUs in the top-right (high demand, long lead
# time, marked "at risk") are the ones most likely to cause future shortages.

plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='Lead Time', y='Daily Demand Rate', hue='At Risk', style='At Risk', s=100, palette={True: 'red', False: 'green'})
plt.title('Lead Time vs Daily Demand Rate (Stockout Risk Highlighted)')
plt.tight_layout()
plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




