#!/usr/bin/env python
# coding: utf-8

# In[64]:


import pandas as pd
import numpy as np


# ## Replace with the path to your file

# In[75]:


df = pd.read_excel('Subject_Report.xlsx')
#todays_date = input("Please enter todays date (YYYY-MM-DD): ")
todays_date = '2023-10-23'


# In[76]:


df.columns = [col.replace(' ', '_') for col in df.columns]
df = df[['INV_CLOSE_DATE','SF-_86_DATE','CE_STATUS_DATE','SUBJECT_NAME']]
df = df.iloc[:-7,:]
df = df.replace(np.nan, '1980/01/02')
# Convert date columns to datetime objects
df['INV_CLOSE_DATE'] = pd.to_datetime(df['INV_CLOSE_DATE'])
df['SF-_86_DATE'] = pd.to_datetime(df['SF-_86_DATE'])
df['CE_STATUS_DATE'] = pd.to_datetime(df['CE_STATUS_DATE'])

# Add 5 years to the date columns
df['INV_CLOSE_DATE'] = df['INV_CLOSE_DATE'] + pd.DateOffset(years=5)
df['SF-_86_DATE'] = df['SF-_86_DATE'] + pd.DateOffset(years=5)
df['CE_STATUS_DATE'] = df['CE_STATUS_DATE'] + pd.DateOffset(years=5)

# Filter rows where all three dates are less than todays date
filtered_df = df[(df['INV_CLOSE_DATE'] < todays_date) & (df['SF-_86_DATE'] < todays_date) & (df['CE_STATUS_DATE'] < todays_date)]

# Create a dataframe with just the names that apply
hitlist_df_names = filtered_df[['SUBJECT_NAME']]

hitlist_df_names.sort_values(by='SUBJECT_NAME', inplace=True)
hitlist_df_names


# In[77]:


#Write to an excel file
hitlist_df_names.to_excel('Investigation_hitlist.xlsx', index=False)





