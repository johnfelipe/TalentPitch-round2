#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd

tfm_df = pd.read_csv("Traffic_Flow_Map_Volumes.csv")
colls_df = pd.read_csv("Collisions.csv")

merged_df = pd.merge(tfm_df,colls_df,on='OBJECTID',how='left')

df_final = merged_df["WEATHER"].value_counts().rename_axis('WEATHER_COND').reset_index(name='NUM_ACCIDENTS')

df_final.to_csv("number_of_accidents_by_climates.csv", index=False)

