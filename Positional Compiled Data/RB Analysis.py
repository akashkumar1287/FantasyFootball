#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import re
import os
import time
df = pd.read_csv("RB_Stats.csv")


# In[10]:


df.columns = [c.replace(' ', '') for c in df.columns]


# In[11]:


df.columns


# In[14]:


df.drop("Unnamed:0", axis = 1, inplace = True)


# In[15]:


df.head()


# In[16]:


counts_age = df["Age"].value_counts()
counts_age = counts_age.reset_index()
counts_age.columns = ["Age","Count"]
print(counts_age)


# In[17]:


pt = sns.catplot(y = "Count",
            x = "Age", data = counts_age,
           palette="colorblind",height=5, aspect=2, kind="bar");
plt.style.use("ggplot")
plt.title("Age of Players",
          fontsize=25);


# In[18]:


sns.catplot(x="Age", y="FantasyPoints", data=df,
            aspect=2, kind="bar", palette="cubehelix");
plt.style.use("ggplot")
plt.title("Fantasy Points vs Age",
          fontsize=25);


# In[19]:


sns.catplot(x="Age", y="RushingYds", data=df, aspect=2, kind="bar",palette="bright");
plt.style.use("ggplot")
plt.title("Age vs Rushing Yards",
          fontsize=25);


# In[20]:


counts_rushTD = df["RushingTD"].value_counts()
counts_rushTD = counts_rushTD.reset_index()
counts_rushTD.columns= ["RushingTD","Counts"]
print(counts_rushTD)


# In[21]:


sns.catplot(x="RushingTD", y="FantasyPoints", data=df,
            aspect=2, kind="bar", palette="cubehelix");
plt.style.use("ggplot")
plt.title("Fantasy Points vs RushingTD",
          fontsize=25);


# In[26]:


sns.lmplot(x="RushingYds", y="ReceivingYds",data=df,markers="o",
            scatter_kws={"color": "blue"},
         line_kws={"linewidth":3,"color":"red"},aspect=2);
plt.title("RushingYds vs ReceivingYds");


# In[28]:


sns.catplot(x="FantasyPoints", y="RushingAtt",data=df,
            orient="h",
            kind="violin",height=20,palette="colorblind");
plt.title("FantasyPoints vs Attempts", fontsize=25);

