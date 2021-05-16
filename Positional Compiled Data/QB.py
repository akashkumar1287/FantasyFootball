#!/usr/bin/env python
# coding: utf-8

# In[275]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy as sp
import re
import os
import time
df = pd.read_csv("QB_Stats.csv")


# In[276]:


df.Age


# In[277]:


df.FantasyPoints


# In[278]:


df.shape


# In[256]:


df.columns = [c.replace(' ', '') for c in df.columns]


# In[257]:


df.columns


# In[258]:


df.drop("Unnamed:0", axis = 1, inplace = True)


# In[259]:


df.head()


# In[260]:


df.isnull().sum()


# In[261]:


counts_age = df["Age"].value_counts()
counts_age = counts_age.reset_index()
counts_age.columns = ["Age","Count"]
print(counts_age)


# In[262]:


pt = sns.catplot(y = "Count",
            x = "Age", data = counts_age,
           palette="colorblind",height=5, aspect=2, kind="bar");
plt.style.use("ggplot")
plt.title("Age of Players",
          fontsize=25);


# In[263]:


sns.catplot(x="Age", y="FantasyPoints", data=df,
            aspect=2, kind="bar", palette="cubehelix");
plt.style.use("ggplot")
plt.title("Fantasy Points vs Age",
          fontsize=25);


# In[264]:


sns.catplot(x="Age", y="PassingYds", data=df, aspect=2, kind="bar",palette="bright");
plt.style.use("ggplot")
plt.title("Age vs Passing Yards",
          fontsize=25);


# In[265]:


counts_PassTD = df["PassingTD"].value_counts()
counts_PassTD = counts_PassTD.reset_index()
counts_PassTD.columns= ["PassingTD","Counts"]
print(counts_PassTD)


# In[266]:


sns.catplot(x="PassingTD", y="FantasyPoints", data=df,
            aspect=2, kind="bar", palette="cubehelix");
plt.style.use("ggplot")
plt.title("Fantasy Points vs PassingTD",
          fontsize=25);


# In[267]:


sns.lmplot(x="Age", y="FantasyPoints",data=df,markers="v",
            scatter_kws={"color": "blue"},
         line_kws={"linewidth":3,"color":"red"},aspect=2);
plt.title("Age vs FantasyPoints");


# In[300]:


sns.catplot(x="FantasyPoints", y="Att",data=df,
            orient="h",
            kind="violin",height=20,palette="colorblind");
plt.title("FantasyPoints vs Attempts", fontsize=25);

