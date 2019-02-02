#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[4]:


df = pd.read_csv(r'C:\Users\Nazanin\Downloads\drugsCom_raw\drugsComTest_raw.csv', sep="\t")
df1 = pd.read_csv(r'C:\Users\Nazanin\Downloads\drugsCom_raw\drugsComTrain_raw.csv', sep="\t")
display(df, df1)


# In[5]:


df2 = df.append(df1)
list(df2)


# In[6]:


display(df2)


# In[7]:


df2.reset_index(drop=True)


# In[8]:


df2.columns


# In[9]:


df.dtypes


# In[10]:


df1.dtypes


# In[11]:


df2.dtypes


# In[12]:


df2.drugName.value_counts()


# In[13]:


df2.condition.value_counts()


# In[14]:


import seaborn as sns


# In[15]:


df2.columns


# In[16]:


df2['rating'].plot(kind = 'hist')


# In[17]:


df2['usefulCount'].plot(kind = 'hist') #'number of users who found review useful' This hist deosn't show anything. 
                                       #We need to plot graph of rating vs usefulcount to see any correlation 


# In[18]:


plt.scatter('rating', 'usefulCount',  data= df2) 
plt.xlabel('Rating')
plt.ylabel('Users found Reviews Useful')
plt.show()


# In[20]:


df2['drugName'].value_counts()[:50]


# In[21]:


df2['drugName'].value_counts()[:40].plot(kind='barh')


# In[22]:


df2['drugName'].value_counts()[:10].plot(kind='barh')


# In[23]:


df2['drugName'].value_counts()[10:20].plot(kind='barh')


# In[24]:


df2['drugName'].value_counts()[20:30].plot(kind='barh')


# In[25]:


df2['drugName'].value_counts()[30:40].plot(kind='barh')


# In[26]:


df2['drugName'].value_counts()[40:50].plot(kind='barh')


# In[27]:


#sns.catplot(y='drugName',  kind='count', palette='pastel', edgecolor='.6', data=df2) #hue="class"


# In[30]:


df2['condition'].value_counts()[:40]


# In[38]:


df2['condition'].value_counts()[:20].plot(kind='barh')


# In[33]:


df2['condition'].value_counts()[20:40].plot(kind='barh')


# In[34]:


#sns.distplot(df2.rating)


# In[35]:


#sns.distplot(df2.usefulCount)


# In[36]:


#df2['drugName'].value_counts()


# In[37]:


# df2['drugName'].value_counts()[:40].plot(kind='barh')


# In[39]:


#check the column-wise distribution of null values: 
print(df2.isnull().sum())


# In[42]:


print(df2.isnull().values.sum()) #total number of missing values in the DataFrame


# In[47]:


df2.groupby('drugName')['rating'].describe()


# In[48]:


df2.groupby('drugName')['rating'].describe().agg({'count':sum})


# In[49]:


df2.groupby('drugName' , sort = False)['rating'].describe()


# In[51]:


grouped = df2.groupby('drugName' , sort = False)['rating'].describe()
grouped.sort_values('count', ascending=False)


# In[52]:


#df2['top_drugName'] = df2['drugName'].value_counts()[:50]
#df3 = df2['drugName'].value_counts()[:50]
#df_topdrug = df3.to_dict() #converts to dictionary


# In[53]:


#print(df_topdrug)


# In[54]:


#print(df_topdrug.keys())


# In[55]:


#print(df3)


# In[56]:


#df2.append(df_topdrug, ignore_index=True)


# In[57]:


#df2['top_drugName'] = df2['drugName'].map(df_topdrug) 
#df2['top_drugName'] = df2.groupby(['drugName'])['rating'].transform('count')


# In[58]:


#print(df2['top_drugName'].dropna())


# In[59]:


#df2['top_drugName'].describe()


# In[62]:


#df2.columns


# In[64]:


#Statistics of rating grouped by your categorical variables: mean, median, max, min. 
    #Also pick your top 5-15 drugs & conditions, and do boxplots
#labels, freq = df2.boxplot('rating','df_drugName',rot = 30)

