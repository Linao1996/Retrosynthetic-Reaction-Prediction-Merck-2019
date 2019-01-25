
# coding: utf-8

# In[1]:


import matplotlib.pyplot as plt
import scipy.stats as stats
import lightgbm as lgb
import seaborn as sns
import xgboost as xgb
import pandas as pd
import numpy as np
import matplotlib
import warnings
import sklearn
import scipy
import numpy
import json
import sys
import csv
import os
import re

pd.set_option('display.max_columns', 50)
warnings.filterwarnings('ignore')
sns.set(color_codes=True)
plt.style.available
from utils import split_train_line, split_test_line


# In[2]:


with open('../input/training/train.txt', 'r') as f:
    train_lines = f.readlines()
del train_lines[0]
len(train_lines)


# In[3]:


with open('../input/training/test.txt', 'r') as f:
    test_lines = f.readlines()
del test_lines[0]
len(test_lines)


# In[4]:


# train_reactions = []
# for line in train_lines:
#     train_reactions.append(split_train_line(line))
# train = pd.DataFrame(train_reactions)
#
# train.shape
#
#
# # In[5]:
#
#
# train.head()


# In[6]:


test_reaction = []
for line in test_lines:
    test_reaction.append(split_test_line(line))
test = pd.DataFrame(test_reaction)
# test.head()
test.shape

