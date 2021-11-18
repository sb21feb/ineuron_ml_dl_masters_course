#!/usr/bin/env python
# coding: utf-8

# ## Q1.1 Write a Python Program to implement your own myreduce() function which works exactly like Python's built-in function reduce()

# In[1]:


def myreduce(func, my_list):
    result = my_list[0]
    for i in my_list[1:]:
        result = func(result, i)
    return result


# In[2]:


def sum(x,y): 
    return x + y


# In[4]:


print (myreduce(sum,[2, 5, 8, 4]))


# ## Q1.2 Write a Python Program to implement your own myfilter() function which works exactly like Python's built-in function filter()

# In[7]:


def myfilter(anyfunc, sequence):
    result = []
    for item in sequence:
        if anyfunc(item):
            result.append(item)
    return result


# In[8]:


# test myfilter function
def ispositive(x):
    if (x <= 0): 
        return False 
    else: 
        return True


# In[9]:


print(myfilter(ispositive,[1,-1,3,4,-6]))


# ## Q2 Implement List comprehensions to produce the following lists. Write List comprehensions to produce the following Lists
# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
# 
# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
# 
# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
# 
# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] [[2, 3, 4, 5], [3, 4, 5, 6], [4, 5, 6, 7], [5, 6, 7, 8]]
# 
# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]

# In[10]:


random_letters = [letter for letter in 'ACADGILD']
print(random_letters)


# In[11]:


list = ['x','y','z']
result = [item*num for item in list for num in range(1,5)]
print(result)


# In[12]:


result = [item*num for num in range(1,5) for item in list]
print(result)


# In[13]:


numeric_list = [2,3,4]
result = [ [item+num] for item in numeric_list for num in range(0,3)]
print(result)


# In[14]:


numeric_list2 = [2,3,4,5]
result = [[item+num for item in numeric_list2] for num in range(0,4)]
print(result)


# In[15]:


input_list=[1,2,3]
result = [ (b,a) for a in input_list for b in input_list]
print(str(result))


# In[ ]:




