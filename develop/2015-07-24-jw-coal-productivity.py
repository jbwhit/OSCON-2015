
# coding: utf-8

# # Example of how to set up your lab notebook

# ## Analysis in this notebook
# - [Dead end] Does year predict production?
# - Does "hours worked" correlate with production?

# ## Tip
# Standard imports at the top
# 
# Imports should be grouped in the following order:
# 
# 1. magics
# 1. Alphabetical order 
#    1. standard library imports
#    1. related third party imports
#    1. local application/library specific imports
# 

# In[7]:

# Magics first (server issues)
get_ipython().magic(u'matplotlib inline')
# Do below if you want interactive matplotlib plot ()
# %matplotlib notebook 

# https://ipython.org/ipython-doc/dev/config/extensions/autoreload.html
get_ipython().magic(u'load_ext autoreload')
get_ipython().magic(u'autoreload 2')

# %install_ext http://raw.github.com/jrjohansson/version_information/master/version_information.py
get_ipython().magic(u'load_ext version_information')
get_ipython().magic(u'version_information numpy, scipy, matplotlib, pandas')


# In[8]:

# Standard library
import os
import sys
sys.path.append("../src/")

# Third party imports
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Local imports
from simpleexample import example_func


# In[9]:

# Customizations
sns.set() # matplotlib defaults

# Any tweaks that normally go in .matplotlibrc, etc., should explicitly go here
plt.rcParams['figure.figsize'] = (12, 12)
get_ipython().magic(u"config InlineBackend.figure_format='retina'")


# In[10]:

# Find the notebook the saved figures came from
fig_prefix = "../figures/2015-07-16-jw-"


# ## Importing cleaned data
# 
# See `../deliver/coal_data_cleanup.ipynb` for how the raw data was cleaned.

# In[11]:

from IPython.display import FileLink
FileLink("../deliver/coal_data_cleanup.ipynb")


# In[12]:

dframe = pd.read_csv("../data/coal_prod_cleaned.csv")


# # [Dead end] Does year predict production?

# In[13]:

plt.scatter(dframe['Year'], dframe['Production_short_tons'])


# # Does Hours worked correlate with output?

# In[14]:

df2 = dframe.groupby('Mine_State').sum() 


# In[17]:

df2 = df2[df2.index != 'Wyoming']


# In[18]:

sns.jointplot('Labor_Hours', 'Production_short_tons', data=df2, kind="reg", ) 
plt.xlabel("Labor Hours Worked")
plt.ylabel("Total Amount Produced") 
plt.tight_layout()
plt.savefig(fig_prefix + "production-vs-hours-worked.png")


# In[ ]:




# In[ ]:




# ## Advanced example, come back if time!

# In[23]:

get_ipython().magic(u'load_ext autoreload')
get_ipython().magic(u'autoreload 2')


# In[24]:

import sys
sys.path.append("../src/")


# In[26]:

from simpleexample import example_func
example_func()


# In[27]:

example_func()


# In[ ]:



