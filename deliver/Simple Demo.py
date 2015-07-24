
# coding: utf-8

# In[ ]:

get_ipython().magic(u'matplotlib inline')


# In[ ]:

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns


# In[ ]:

# Customizations
sns.set() # matplotlib defaults

# Any tweaks that normally go in .matplotlibrc, etc., should explicitly go here
plt.rcParams['figure.figsize'] = (12, 8)
get_ipython().magic(u"config InlineBackend.figure_format='retina'")


# ## Load some data into a pandas Dataframe

# In[ ]:

from IPython.display import IFrame


# In[ ]:

IFrame("http://www.eia.gov/coal/data.cfm", width=700, height=350)


# In[ ]:

dframe = pd.read_csv("../data/coal_prod_cleaned.csv")


# In[ ]:

# Tip use .head()
dframe.head()


# In[ ]:

_7


# In[ ]:

_i7


# In[ ]:

plt.scatter(dframe.Average_Employees, dframe.Labor_Hours)
plt.xlabel("Number of Employees")
plt.ylabel("Total Hours Worked")


# In[ ]:

plt.scatter(dframe.Labor_Hours, dframe.Production_short_tons, )
plt.xlabel("Total Hours Worked")
plt.ylabel("Total Amount Produced") 


# In[ ]:

years = sorted(dframe.Year.unique())
colors = sns.color_palette(n_colors=len(years))
color_dict = {key: value for key, value in zip(years, colors)} 


# In[ ]:

color_dict 


# In[ ]:

for year in sorted(dframe.Year.unique()[[0,2, 5, -1]]):
    plt.scatter(dframe[dframe.Year == year].Labor_Hours,
                dframe[dframe.Year == year].Production_short_tons, 
                c=color_dict[year],
                s=50,
                label=year,
               )
plt.xlabel("Total Hours Worked")
plt.ylabel("Total Amount Produced")
plt.legend()


# ## Notebook extensions
# 
# Check out http://nbviewer.ipython.org/github/quantopian/qgrid/blob/master/qgrid_demo.ipynb for more (including demo)
# 

# In[ ]:

import qgrid # Best practices is to put imports at the top of the Notebook.
qgrid.nbinstall(overwrite=True)


# In[ ]:

qgrid.show_grid(dframe[['MSHA_ID', 'Year', 'Mine_Name', 'Mine_State', 'Mine_County']], remote_js=True)


# ## SQL queries
# 
# An updated implementation SQL magic command from Christian Perez at SVDS https://github.com/cfperez/ipython-sql

# In[ ]:

get_ipython().magic(u'load_ext sql')
get_ipython().magic(u'reload_ext sql')


# In[ ]:

get_ipython().magic(u'config SqlMagic.autopandas=True')


# In[ ]:

coalproduction = dframe.copy()


# ## Create table in sqlite database
# 
# %% magics 

# In[ ]:

get_ipython().run_cell_magic(u'sql', u'sqlite://', u'PERSIST coalproduction')


# ## Query database 

# In[ ]:

get_ipython().run_cell_magic(u'sql', u'sqlite://', u'\nSELECT DISTINCT company_type \nFROM coalproduction \nWHERE msha_id = 5000030')


# In[ ]:

dbtest = get_ipython().magic(u'sql SELECT * FROM coalproduction ')


# In[ ]:

dbtest[['Company_Type', 'Mine_Basin']].head()


# In[ ]:

type(dbtest)


# In[ ]:



