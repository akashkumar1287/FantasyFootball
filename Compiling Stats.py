#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd

csv_file_list = ["2019.csv", "2018.csv", "2017.csv","2016.csv","2015.csv","2014.csv","2013.csv","2012.csv","2011.csv","2010.csv" 
                ,"2009.csv","2008.csv","2007.csv","2006.csv","2005.csv","2004.csv","2003.csv","2002.csv","2001.csv","2000.csv"
                ,"1999.csv","1998.csv","1997.csv","1996.csv","1995.csv","1994.csv","1993.csv","1992.csv","1991.csv","1990.csv"
                ,"1989.csv","1988.csv","1987.csv","1986.csv","1985.csv","1984.csv","1983.csv","1982.csv","1981.csv","1980.csv"
                ,"1979.csv","1978.csv","1977.csv","1976.csv","1975.csv","1974.csv","1973.csv","1972.csv","1971.csv","1979.csv"]

list_of_dataframes = []
for filename in csv_file_list:
    list_of_dataframes.append(pd.read_csv(filename))

df = pd.concat(list_of_dataframes)


# In[3]:


df = df.sort_values('FantasyPoints', ascending = False)
df = df.reset_index(drop=True)
new_df = df.drop(columns = ['Unnamed: 0'])


# In[11]:


FF = pd.read_csv('Total_Players_Stats.csv')
FF = FF.drop(columns = ['Unnamed: 0'])
RB = FF.loc[(FF['Pos'] == 'RB')]
RB = RB.reset_index(drop=True)
RB.to_csv('RB_Stats.csv')


# In[12]:


FF = pd.read_csv('Total_Players_Stats.csv')
FF = FF.drop(columns = ['Unnamed: 0'])
QB = FF.loc[(FF['Pos'] == 'QB')]
QB = QB.reset_index(drop=True)
QB.to_csv('QB_Stats.csv')


# In[13]:


FF = pd.read_csv('Total_Players_Stats.csv')
FF = FF.drop(columns = ['Unnamed: 0'])
WR = FF.loc[(FF['Pos'] == 'WR')]
WR = WR.reset_index(drop=True)
WR.to_csv('WR_Stats.csv')


# In[17]:


FF = pd.read_csv('Total_Players_Stats.csv')
FF = FF.drop(columns = ['Unnamed: 0'])
TE = FF.loc[(FF['Pos'] == 'TE')]
TE = TE.reset_index(drop=True)
TE.to_csv('TE_Stats.csv')

