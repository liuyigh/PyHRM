
# coding: utf-8

# ## Introduction

# Please read a very nice introduction provided by Kapa BioSystems to understand, prepare and troubleshoot
# 
# http://www.kapabiosystems.com/document/introduction-high-resolution-melt-analysis-guide/
# 

# ### Import Python modules for analysis

# In[64]:

get_ipython().magic(u'matplotlib inline')

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# ### Read and Plot Melting Data

# In[65]:

df = pd.read_csv('Sample-HRM-p50-genotyping.csv')
plt.plot(df[[0]],df.ix[:,1:])
plt.show()


# ### Select melting range

# In[74]:

df_melt=df.ix[(df.iloc[:,0]>75) & (df.iloc[:,0]<89)]
df_data=df_melt.ix[:,1:]
plt.plot(df_melt[[0]],df_data)
plt.show()


# ### Normalizing 

# In[73]:

df_norm= (df_data - df_data.min()) / (df_data.max()-df_data.min())*100
plt.plot(df_melt[[0]],df_norm)
plt.show()


# ### Calculate and Show Diff Plot 

# In[68]:

dfdif = df_norm.sub(df_norm['J14'],axis=0)
plt.plot(df_melt[[0]],dfdif)
plt.show()


# ### Clustering

# Use KMeans module from SciKit-Learn to cluster your sample into three groups (WT, KO, HET). Be careful, your samples may have less than three groups. So always check the diff plots first.

# In[69]:

import sklearn.cluster as sc
from IPython.display import display


# In[70]:

mat = dfdif.T.as_matrix()
hc = sc.KMeans(n_clusters=3)
hc.fit(mat)

labels = hc.labels_
results = pd.DataFrame([dfdif.T.index,labels])
display(results.ix[:0,results.ix[1]==0])
display(results.ix[:0,results.ix[1]==1])
display(results.ix[:0,results.ix[1]==2])


# My controls are 
# * WT: I12, J12
# * KO: I13, J13
# * HET: I14, J14
# 
# So you can identify your genotyping results by looking at: to which control they cluster.

# In[ ]:



