
# coding: utf-8

# # Coal Mining 
# Coal mining data from eia.gov
# 
# Combining and cleaning the raw csv files into a cleaned data set and coherent database.
# 
# Generally a good idea to have a separate data folder with the raw data.
# 
# When you clean the raw data, leave the raw in place, and create cleaned version with the steps included (ideal situation for Notebook). 

# In[1]:

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()

import numpy as np
import pandas as pd


# In[2]:

df = pd.DataFrame.from_csv("../data/coal_prod_cleaned.csv")


# In[3]:

df.head()


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



