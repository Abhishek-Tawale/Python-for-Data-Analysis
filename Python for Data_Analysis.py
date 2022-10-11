#!/usr/bin/env python
# coding: utf-8

# In[8]:


import pandas as pd


# In[9]:


dir(pd)


# In[4]:


help(pd.NamedAgg)


# In[5]:


pip install streamlit


# In[6]:


import streamlit


# In[7]:


pip install scikit-learn


# In[5]:


df=pd.read_csv('https://raw.githubusercontent.com/slmsshk/DataSet/main/Salaries.csv')


# # Data Preview

# In[14]:


df.head(10)


# 
# 

# In[16]:


df.tail(10)


# 
# # Checking Data Types 
# 

# In[18]:


df.dtypes


# In[20]:


#Check Perticular Column Type
df["salary"].dtypes


# In[21]:


#Number Of dimension
df.ndim


# In[22]:


#Number Of Size (It will show No of datapoints)
df.size


# In[23]:


#return a tuple representing the dimensionally (it will show rows and columns)
df.shape


# In[24]:


#Nummpy representation of the data
df.values


# In[25]:


#Number of row lables and column names
df.axes


# In[26]:


#List the column names 
df.columns


# In[28]:


#Import Python Libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[29]:


#Find the summary for the numeric colums in the dataset
df.describe()


# In[38]:


#Calculate standard devision for all numeric columns
df.std()


# In[39]:


#What are the mean values of the first 50 records in the datasets
df.head(50).mean()


# In[32]:


#Find How many record this data frame has
df.size


# In[35]:


#Find how many columns are there
len(df.columns)


# In[36]:


#Find the column names
df.columns


# In[37]:


#What types of columns we have in this data frame
df.dtypes


# In[40]:


df.rank


# In[41]:


df["rank"]


# In[42]:


#type of rank
type(df.rank)


# In[45]:


type(df["rank"])


# In[6]:


#Group data using rank
df_rank=df.groupby(['rank'])


# In[11]:


#calculate mean value for each numeric column per each group 
df_rank.mean()


# In[18]:


#calculate mean only for salary
df.groupby('rank')[["salary"]].mean()


# In[19]:


#calculate mean both for salary and phd
df.groupby("rank")[["phd", "salary"]].mean()


# In[27]:


df.groupby(['rank'], sort=False).mean()


# # Data Frame Filtering

# In[32]:


#Calculate salary of professors greater than 20000
df[df["salary"]>20000]


# In[53]:


#select only those rows only belong to female professors 
df[df['sex']=='Female']


# # Data Frame: Slicing

# In[89]:


df1=df['salary']


# In[90]:


#first 50 rows of salary
df1.iloc[:50]


# In[70]:


#last 50 rows of salary
df1.iloc[-50:]


# In[95]:


df.iloc[ [0,5],[1,3] ]


# In[98]:


#first 7 rows
df.iloc[:7]


# In[83]:


#first and second rows and first 2 columns 
df.iloc[1:3, 0:2]


# # Aggregation Function in Pandas 

# In[100]:


df[["phd","salary"]].agg(["min", "mean", "max"])


# In[110]:


df[["rank"]].agg(["min", "max"])


# In[ ]:




