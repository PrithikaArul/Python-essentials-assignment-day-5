#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Program to sort
list1=[0,1,10,4,1,0,56,2,0,1,3,0,56,0,4]
def fun1(x):
    print(x)
    return(x.rsplit(0))
list1.sort(key=fun1)


# In[7]:


list1


# In[ ]:


#Program to merge two lists
list2=[10,20,40,60,70,80]
list3=[5,15,25,35,45,60]
list4=list2+list3
for x in list4:
    list4.sort()
    print(list4,end='')


# In[19]:


list4

