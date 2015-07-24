
# coding: utf-8

# In[13]:

from IPython.display import Image


# In[5]:

from IPython.html.services.config import ConfigManager
from IPython.utils.path import locate_profile
cm = ConfigManager(profile_dir=locate_profile(get_ipython().profile))
cm.update('livereveal', {
              'theme': 'simple',
              'start_slideshow_at': 'selected',
}) 


# In[15]:

get_ipython().magic(u'matplotlib inline')
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
import numpy as np
import pandas as pd


# # IPython Notebook best practices for data science
# 
# ## Jonathan B Whitmore [@JBWhitmore](https://twitter.com/jbwhitmore)
# 
# ### SVDS (Silicon Valley Data Science) [@SVDataScience](https://twitter.com/svdatascience)
# 

# # <s>IPython</s> Jupyter Notebook best practices for data science
# 
# 
# ## Jonathan B Whitmore [@JBWhitmore](https://twitter.com/jbwhitmore)
# 
# ### SVDS (Silicon Valley Data Science) [@SVDataScience](https://twitter.com/svdatascience)
# 

# ## Ju -- Julia

# ## py -- Python

# ## teR -- R
# 
# # Ju--py--ter!

# # Background
# 
# Former astrophysicist
# 
#  - PhD from UC San Diego 2011
#  - 3 year postdoc at Swinburne University in Melbourne, Australia
#  - User of IPython/python since 2007
#  - User of the IPython Notebook since late 2011/early 2012ish

# # Background
# 
# Now a Data Scientist at Silicon Valley Data Science (SVDS): 
# 
#  - Working on small teams (~4-6 people)
#   - 2-3 Data Scientists and 2-3 Data Engineers
# 
#  - Different technical environments
#   - sometimes we can use GitHub, sometimes not
#   - sometime python, sometimes not
#   - Jupyter Notebook has been very popular with fellow Data Scientists

# # Outline
# 
# 1. Quick demo of the Jupyter Notebook
# 1. Intermediate level usage and examples
# 1. Jupyter Notebook for Data Science teamwork 
# 1. Bit of Advanced Usage

# # Quick Demo -- What is the Jupyter notebook?
# 

# In[ ]:




# In[ ]:




# # Problem
# 
# ## How does a team of Data Scientists use the Jupyter Notebooks effectively?
# 
#  - Do we all use one Notebook?
#  - Do we all use different Notebooks?
#  - Do we share all Notebooks?
#  - Should there be a directory on each person's laptop with every Notebook ever?

# # Problem
# 
# ## How do we organize our Jupyter notebooks so that our work is:

#  - collaborative (we work on teams)

#  - reliably captured and transparently shared

#  - clearly deliver insights to our clients

# # Tip: Differentiate the kinds of notebooks into two main categories

# ## 1. Lab notebooks

# ## 2. Deliverable notebooks

# # Lab notebook -- Exploratory Data Analysis
# 
# Think: actual paper laboratory notebooks.
# 
# <img src="../figures/2097753744_184f05d463_z.jpg">
# 
# Source: https://flic.kr/p/4cnx71

# # 1 The Lab notebook
# 
# Let a traditional-paper Lab Notebook be your guide here:
# 
#  - Keeps a historical record of the analysis explored

#  - Meant to be a development or scratch place

#    - Each notebook is controlled by a single Data Scientist

#    - Split the notebooks when they get too long

#    - Split the notebooks by topic if it makes sense.

# # 2 The Deliverable notebook
# 
# For example: 
# 
#  - Analysis that will be referenced (how raw data was transformed into cleaned data)
#  - The fully polished and final outputs of the analysis.
#  - Peer reviewed -- other team members will review before accepted.
#  - These notebooks are controlled by the whole Data Science team.
# 

# # Demo: Simple Example Data Exploration 

# # Tip: Get organized -- High level directories
# 
#  - data # Backed up outside of version control

#  - deliver # Final polished Notebooks for consumption

#  - develop # Lab Notebooks stored here

#  - figures # Figures stored here

#  - src # Scripts/modules stored here

# # Naming things is hard... 
# 
# <img src="../figures/bird-leaf.jpg">
# 
# Source: http://www.huffingtonpost.com/2014/07/25/other-names-for-things_n_5621554.html via https://www.reddit.com/r/AdviceAnimals/comments/1ie4ra/my_friend_couldnt_think_of_the_word_feather/

# # Naming things is hard... 
# 
# 
# ## Tip:  Name the develop/lab-notebooks with the following convention:
# 
#  - **[ISO 8601 date]**-[DS-initials]-[2-4 word description].ipynb
#  - **2015-07-13**-jw-coal-yearly-productivity.ipynb

# # Naming things is hard... 
# 
# 
# ## Tip:  Name the develop/lab-notebooks with the following convention:
# 
#  - [ISO 8601 date]-**[DS-initials]**-[2-4 word description].ipynb
#  - 2015-07-13-**jw**-coal-yearly-productivity.ipynb

# # Naming things is hard... 
# 
# 
# ## Tip:  Name the develop/lab-notebooks with the following convention:
# 
#  - [ISO 8601 date]-[DS-initials]-**[2-4 word description]**.ipynb
#  - 2015-07-13-jw-**coal-yearly-productivity**.ipynb

# # Beware, semi-controversial recommendations coming...

# # Tip: Use post-save hooks
# 
# We get around these difficulties by committing:
# 
#  - `.ipynb`
#  - `.py`
#  - `.html` 
# 
# of every notebook: development or deliverable.

# Add the following code to: `ipython_notebook_config.py` 
# 
# ```python 
# import os
# from subprocess import check_call
# 
# def post_save(model, os_path, contents_manager):
#     """post-save hook for converting notebooks to .py and .html files."""
#     if model['type'] != 'notebook':
#         return # only do this for notebooks
#     d, fname = os.path.split(os_path)
#     check_call(['ipython', 'nbconvert', '--to', 'script', fname], cwd=d)
#     check_call(['ipython', 'nbconvert', '--to', 'html', fname], cwd=d)
# 
# c.FileContentsManager.post_save_hook = post_save
# ```
# Modified code from: https://github.com/ipython/ipython/issues/8009 by github user: https://github.com/minrk

# ## What does this do?
# 
# Now everytime you save a Notebook 
# 
#  - `first-notebook.ipynb`
# 
# Two files are now created/updated:
#  - `first-notebook.py` 
#  - `first-notebook.html`

# #Tip: Version Control
# 
#  - Commit all the files
#    - `.ipynb`, `.py`, and `.html`
#    - and the figures
#  
# 

# # Source control is for source... so what's with this output?
# 
# <img src="../figures/confused-brad.gif">
# 
# Source: http://i.imgur.com/zo4EMKC.gif

# # Standard Pull-request workflow
# 
# Github has been making great strides in making this work well -- still progress to be made
# 
# ## Pull request Demo

# # Benefits
# 
# Lab notebook
# 
#  1. Record of analysis including dead-ends
#  1. Ability to easily peer review analysis and dead-ends
#  1. Project managers can easily see and read the analysis with GitHub `.ipynb` or `.html` without installing `ipython`
# 

# # Advanced Usage

# 
# 
# 
# 
# # Tip: Run on a server
# 
# Useful link about how to setup a remote server: 
# 
#  - http://ipython.org/ipython-doc/1/interactive/public_server.html
# 
# 
# # Create a server profile
# 
# ```bash
# ipython profile create nbserver 
# ```
# 
# Which creates the following files: 
# 
#  - ~/.ipython/profile_nbserver/ipython_config.py
#  - ~/.ipython/profile_nbserver/ipython_kernel_config.py
#  - ~/.ipython/profile_nbserver/ipython_console_config.py
#  - ~/.ipython/profile_nbserver/ipython_qtconsole_config.py
#  - ~/.ipython/profile_nbserver/ipython_notebook_config.py
#  - ~/.ipython/profile_nbserver/ipython_nbconvert_config.py
# 

# # Demo
# 
#  - server
#  - sql magic
# 

# # Resources
# 
#  - Jupyter slides: https://github.com/damianavila/RISE
#  
# ## Wishlist
# 
#  - nbdiff: http://nbdiff.org/ (GitHub repo: https://github.com/tarmstrong/nbdiff)

# # Thank you!
# 
# # Please send comments/questions
# 
# ## Jonathan B Whitmore 
#   - Twitter: [@JBWhitmore](https://twitter.com/jbwhitmore)
#   - Github: [jbwhit](https://github.com/jbwhit)
#   
# ### SVDS (Silicon Valley Data Science) [@SVDataScience](https://twitter.com/svdatascience)
# 

# In[ ]:



