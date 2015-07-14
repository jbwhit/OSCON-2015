
# coding: utf-8

# # Coal Mining 
# 
# 
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

import pandas as pd
dframe = pd.DataFrame.from_csv("../data/coal_prod_cleaned.csv")


# In[3]:

plt.scatter(dframe.Average_Employees, dframe.Labor_Hours)
plt.xlabel("Number of Employees")
plt.ylabel("Total Hours Worked")
plt.tight_layout()


# In[4]:

plt.scatter(dframe.Labor_Hours, dframe.Production_short_tons, )
plt.xlabel("Total Hours Worked")
plt.ylabel("Total Amount Produced") 
plt.tight_layout()


# In[5]:

colors = sns.color_palette(n_colors=len(dframe.Year.unique())) 


# In[6]:

color_dict = {key: value for key, value in zip(sorted(dframe.Year.unique()), colors)}


# In[15]:

for year in sorted(dframe.Year.unique()[[0, 2, 5, -1]]):
    plt.scatter(dframe[dframe.Year == year].Labor_Hours,
                dframe[dframe.Year == year].Production_short_tons, 
                c=color_dict[year],
                s=50,
                label=year,
               )
plt.xlabel("Total Hours Worked")
plt.ylabel("Total Amount Produced")
plt.legend()
plt.tight_layout()
# plt.savefig("../figures/ex1.png") 


# In[8]:

dframe.head()


# In[9]:

dframe['Productivity'] = dframe['Production_short_tons']/dframe['Labor_Hours']


# In[10]:

df2 = dframe.groupby('Mine_State').sum()


# In[11]:

df2


# In[12]:

df2 = df2[df2.index != 'Wyoming']


# In[13]:

sns.jointplot('Labor_Hours', 'Production_short_tons', data=df2, kind="reg", ) 
plt.xlabel("Labor Hours Worked")
plt.ylabel("Total Amount Produced") 
plt.tight_layout()
plt.savefig("../figures/production-vs-hours-worked.png", dpi=350)


# In[14]:

sns.jointplot('Average_Employees', 'Production_short_tons', data=df2, kind="reg", ) 
plt.xlabel("Average # Employees")
plt.ylabel("Total Amount Produced") 
plt.tight_layout()
plt.savefig("../figures/production-vs-number-employees.png", dpi=350)


# In[ ]:




# In[ ]:



