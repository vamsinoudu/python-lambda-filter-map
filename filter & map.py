#!/usr/bin/env python
# coding: utf-8

# In[2]:


even_odd_lambda = lambda n:"even"if n%2==0 else "odd"
print(even_odd_lambda(2))
print(even_odd_lambda(5))



# In[7]:


def even_odd(n):
    if n%2==0:
        return "even"
    else:
        return "odd"
print(even_odd(66))


# In[14]:


sum_lambda = lambda num :num/num
print(sum_lambda(2))


# In[18]:


#maximum of 2 numbers
max_fun = lambda m,n:f"{m} is maximum if m>n else f" {n} maximum"
print(max_fun(10,20))


# In[19]:


(lambda num :num*num)(20)


# In[20]:


name ="New"
name_2 ="Delhi"
new_name = lambda x,y:x.title()+y.title()
new_name(name,name_2)


# In[26]:


def fun(num):
    if num % 2 != 0:
        return True
    else:
        return False
new_list = [4,5,6,7,8,9]

for i in new_list:
    print(fun(i))
    
# filter

print(list(filter(fun,new_list)))


# In[31]:


msg = "otp received is 1245"
list(filter(lambda x :x.isdecimal(),msg))
tuple(filter(lambda x :x.isdecimal(),msg))
set(filter(lambda x :x.isdecimal(),msg))


# In[32]:


"".join(list(filter(lambda x :x.isdecimal(),msg)))


# In[103]:


seq = (52,-3,34+1j,45.1,-1)
list(filter(lambda y:isinstance(y,float),seq))
list(filter(lambda y:isinstance(y,complex),seq))
    


# In[2]:


# map = (function ,sequence)
# multiplying all number with 2
x_list =[2,4,6,8,10]
list(map(lambda x:x*2,x_list))


# In[3]:


# converting into integer from float

seq = [2.2,3.4,2,6,88.34]
list(map(int,seq))


# In[5]:


animal_name =["Cow","Lion","Tiger"]
list(map(lambda animal:animal.title(),animal_name))


# In[18]:


# adding a,b elements:
a =[1,2,3]
b =[2,3,4]
list(map(lambda s1,s2 :s1+s2,a,b))


# In[21]:


# adding a,b elements:
a =[1,2,3,0]
b =[2,3,4,5]
list(map(lambda s1,s2:s1+s2,a,b))


# In[27]:


# substract b,a elements:
a =[1,2,3,0]
b =[2,3,4,5]
list(map(lambda b2,b1 :b2-b1,b,a))


# In[22]:



# substract a,b elements:
a =[1,2,3,0]
b =[2,3,4,5]
list(map(lambda s1,s2:s1-s2,a,b))


# In[23]:


# multiplying a,b elements:
a =[1,2,3,0]
b =[2,3,4,5]
list(map(lambda m1,m2:m1*m2,a,b))


# In[24]:


# Dividing a,b elements:
a =[1,2,3,0]
b =[2,3,4,5]
list(map(lambda v1,v2:v1/v2,a,b))


# In[41]:


# Divide b,a elements:
#Zero division error:

a =[1,2,3,0]
b =[2,3,4,5]
try:
    list(map(lambda b2,b1:b2/b1,b,a))
except:
    print("occured error")


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:


a

