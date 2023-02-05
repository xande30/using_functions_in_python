#!/usr/bin/env python
# coding: utf-8

# # Notebook Import And Packages

# In[3]:


import matplotlib.pyplot as plt
import numpy as np

get_ipython().run_line_magic('matplotlib', 'inline')


# # Example 1 - A Simple Cost Function
# $f(x) = x^2 + x + a$

# In[23]:


def f(x):
    return x ** 2 + x + 1
def df(x):
    return 2 * x + 1


# In[41]:


x_1 = np.linspace(start = -3, stop=3,num=500)


# # Slope & Derivatives

# In[44]:


plt.figure(figsize=[15,5])
plt.subplot(1,2,1)


plt.xlim(-3, 3)
plt.ylim((0,8))
plt.title('Cost Function', fontsize=16)
plt.xlabel('x', fontsize=16)
plt.ylabel('f(x)', fontsize=16)
plt.plot(x_1,f(x_1), color='#00FF00', linewidth=6)
plt.grid()
plt.style.use('dark_background')
plt.plot(x_1,f(x_1))
plt.subplot(1,2,2)

plt.xlim(-3, 3)
plt.ylim((0,8))
plt.title('Investition Budget', fontsize=16)
plt.xlabel('x',fontsize=16)
plt.ylabel('df(x_1)', fontsize=16)
plt.plot(x_1,df(x_1),color='#00FF00', linewidth=5)
plt.grid()
plt.style.use('dark_background')
plt.show()


# 

# In[18]:





# In[ ]:




