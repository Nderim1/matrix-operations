
# coding: utf-8

# In[2]:


# Run this cell but don't modify it.

#
# %get_ipython().run_line_magic('load_ext', 'autoreload')
# %get_ipython().run_line_magic('autoreload', '2')
from matrix import Matrix, zeroes, identity


# In[3]:


# some functionality already exists... here's a demo

m1 = Matrix([
    [1, 2],
    [3, 4]
])

m2 = Matrix([
    [2, 5],
    [6, 1]
])

print("m1 is")
print(m1)

print("m2 is")
print(m2)

print("we've also provided you with a function called zeros")
print("here's what happens when you call zeros(4,2)")
print(zeroes(4,2))

print("we've also provided you with a function called identity")
print("here's identity(3)")
print(identity(3))

print("but not everything works yet!")
print("for example, matrix addition...")
print("run the cell below to see what happens when we try...")


# In[8]:


m1 = Matrix([
    [1, 2, 3],
    [3, 4, 4],
    [1, 2, 9],
    [1, 2, 3]
])

m2 = Matrix([
    [2, 5, 4],
    [6, 1, 4],
    [3, 4,-5],
    [1, 2, 3]
])

m3 = Matrix([
    [1,3,4,5],
    [1,2,3,4],
    [1,2,3,4]
])

m3 = m1 + m2
print("m1 + m2 is")
print(m3)

# det = m1.determinant()
# print(det)

# trace = m1.trace()
# print(trace)

# inv = m1.inverse()
# print(inv)

# sm = m1+m2
# print(sm)

#print(-m2)
print(m3*m1)

print(4*m1)
print(2*m3)
# In[4]:


# Try running this code. You should get an assertion error. 
# You will continue to get assertion errors until all the 
# methods in matrix.py are correctly implemented.

# You can open matrix.py by selecting File > Open... 
# and then selecting matrix.py

import test


# In[ ]:


# open matrix.py (File > Open...) and start
# implementing matrix methods! 

# when your code passes all the tests you can submit by 
# pressing the SUBMIT button in the lower right corner 
# of this page.

