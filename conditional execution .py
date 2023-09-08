#!/usr/bin/env python
# coding: utf-8

# In[7]:


x = 5
if x < 10:
    print('Smaller')
if x > 20:
    print('Bigger')
print('Finis')


# In[6]:


x = 5
if x == 5 : 
    print('Equals 5')
if x > 4 : 
    print('Greater than 4')
if x >= 5 :
    print('Greater than or Equals 5')
if x < 6 :
    print('Less than 6') 
if x <= 5 :
    print('Less than or Equals 5')
if x != 6 :
    print('Not equal 6')


# In[11]:


x = 42
if x > 1 :
    print('More than one')
    if x < 100 : 
        print('Less than 100') 
print('All done')


# In[12]:


x = 4
if x > 2 :
    print('Bigger')
else :
    print('Smaller')
print('All done')


# In[13]:


if x < 2 :
    print('small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')


# In[14]:


x = 5 
if x < 2 :
    print('small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')


# In[20]:


a= 'hello bob'
try:
    i=int(a)
except:
    i=-1
print('first',i)
a='123'
try:
    i=int(a)
except:
    i=-1
print('second',i)


# In[24]:


r = input('Enter a number:')
try: 
    i = int(r)
except: 
    i = -1
if i > 0 : 
    print('Nice work')
else: 
    print('Not a number')


# In[ ]:


#Exercise


# In[25]:


hours= input("enter hours")
h=int(hours)
rate=input('enter rate')
r=int(rate)
if h<=40:
    print(h*r)
elif h>40:
    print(40*r+(h-40)*1.5*r)
    


# In[ ]:


hours= input("enter hours")
try:
    print('value not found')
except:
    h=int(hours)
rate=input('enter rate')
try:
        print('value not found')
except:
    r=int(rate)
if h<=40:
    print(h*r)
elif h>40:
    print(40*r+(h-40)*1.5*r)


# In[ ]:




