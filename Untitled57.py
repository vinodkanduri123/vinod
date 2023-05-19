#!/usr/bin/env python
# coding: utf-8

# In[5]:


n1=int(input("Enter a number:"))
n2=int(input("Enter a number:"))
n3=int(input("ENter a number:"))
if n1>n2>n3:
    print("{} is lorgest number".format(n1))
elif n1<n2>n3:
    print("{} is lorgest number".format(n2))
elif n1<n2<n3:
        print("{} is lorgest number".format(n3))
elif n1==n2==n3:
    print("all numbers are equal")


# In[9]:


n=int(input("Enter a number:"))
if n%2==0:
    print("Given number is even number :{}".format(n))
else:
    print("Given number is odd number :{}".format(n))


# In[13]:


age=int(input("Enter the age:"))
if age<18:
    print("your age is not elgible for vote :{}".format(age))
else:
    print("your for elgible for vote your age is :{}".format(age))


# In[16]:


#4.to check given input number is equal to 20,80,500

n=int(input("Enter a number:"))
if n==20:
    print("This number is equal to 20 :{}".format(n))
elif n==80:
    print("This number is equal to 80 :{}".format(n))
elif n==500:
    print("This number is equal to 500:{}".format(n))
else:
    print("This number is not equal to the given numbers :{}".format(n))


# In[34]:


#5.program to check student grades
Telugu=int(input("Enter telugu subject marks:"))
English=int(input("Enter english subject marks :"))
Hindi=int(input("Enter hindi subject marks :"))
Maths=int(input("Enter maths subject marks:"))
Science=int(input("Enter science subject marks:"))
Social=int(input("Enter social subject marks:"))
Total=Telugu+English+Hindi+Maths+Science+Social
Percentage=Total/6
if Percentage >= 90.00 and Percentage <=100.00:
    print("your pass in grade A++ with {} percentage".format(Percentage))
elif Percentage >= 80.00 and Percentage <=89.99:
    print("your pass in Grade A with {} percentage".format(Percentage))
elif Percentage >= 70.00 and Percentage <=79.99:
    print("your pass in Grade B with {} percentage".format(Percentage))
elif Percentage >= 60.00 and Percentage <=69.99:
    print("your pass in Grade C with {} percentage".format(Percentage))
elif Percentage >= 50.00 and Percentage <=59.99:
    print("your pass in Grade D with {} percentage".format(Percentage))
elif Percentage >= 45.00 and Percentage <=49.99:
    print("your pass in Grade E with {} percentage".format(Percentage))
elif  Percentage <=44.99:
    print("your Fail with {} percentage".format(Percentage))
    
    


# In[ ]:





# In[ ]:




