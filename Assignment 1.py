#!/usr/bin/env python
# coding: utf-8

# In[ ]:


'''
Ask 2 numbers from users and store it in num1 and num2
Ask user to press 1 for addition,2 for subtraction,3 for multiplication and 4 for division
based on number given by user do the math operation
'''

# take 2 numbers from user


# In[18]:


num1 = int(input("Enter 1st Number"))
num2 = int(input("Enter 2nd Number"))


math = int(input(''' Press 1 for ADDITION
Press 2 for SUBTRACTION
Press 3 for MULTIPLICATION
Press 4 for Division'''))


if(math == 1):
    result = num1 + num2
elif(math == 2):
    result = num - num2
elif(math == 3):
    result = num1 * num2
elif(math == 4):
    result = num1 / num2
else:
    print("wrong selection")
    
print(result)


# In[ ]:








# In[7]:


num1 = int(input("Enter 1st Number"))
num2 = int(input("Enter 2nd Number"))

def add():
    a = num1 + num2
    print("\nAddition is : ",a)
    
def sub():
    s = num1 - num2
    print("\nSubtraction is :",s)
    
def mul():
    m = num1 * num2
    print("\nMultiplication is :",m)
    
def div():
    d = num1 / num2
    print("\nDivision is :",d)
    
math = int(input('''Press 1 for ADDITION
Press 2 for SUBTRACTION
Press 3 for MULTIPLICATION
Press 4 for Division : '''))

if(math == 1):
    add()
elif(math == 2):
    sub()
elif(math == 3):
    mul()
elif(math == 4):
    div()
else:
    print("wrong selection")


# In[ ]:








# In[12]:


num1 = int(input("Enter 1st Number"))
num2 = int(input("Enter 2nd Number"))

def add():
    a = num1 + num2
    print("\nAddition is : ",a)
    
def sub():
    s = num1 - num2
    print("\nSubtraction is :",s)
    
def mul():
    m = num1 * num2
    print("\nMultiplication is :",m)
    
def div():
    d = num1 / num2
    print("\nDivision is :",d)
    
math = input('''Press + for ADDITION
Press - for SUBTRACTION
Press * for MULTIPLICATION
Press / for Division : ''')

if(math == "+"):
    add()
elif(math == "-"):
    sub()
elif(math == "*"):
    mul()
elif(math == "/"):
    div()
else:
    print("wrong selection")


# In[ ]:








# In[4]:


#remove white space at the beginning & at the ending
str1 ='     Hello     '
print(str1)


# In[3]:


str1 = '     Hello     '

#to remove space at the biginning
while str1[0] == " ":  
    str1 = str1[1:]

#to remove space at the end
while str1[-1] == " ":
    str1 = str1[:-1]
    
print(str1)


# In[ ]:








# In[ ]:


# to count & remove white space


# In[3]:


str1 = '     Hello     '
count1 = 0
count2 = 0

#to remove space at the biginning
while str1[0] == " ":  
    str1 = str1[1:]
    count1 = count1 + 1
     
#to remove space at the end
while str1[-1] == " ":
    str1 = str1[:-1]
    count2 = count2 + 1
    
print(str1)
print('Space at Beginning: ', count1)
print('Space at ending : ', count2)


# In[ ]:








# In[ ]:


# to count the no. of words in a string without inbuilt function


# In[1]:


#string
word = ('GRATITUDE IS ATTITUDE')
n = 0
s = 0

#convert string to list

list1 = list(word)
print(list1)


# In[2]:


# to count total list

for i in word:
    n = n + 1
print(n)


# In[5]:


# to coount total spaces in word

for i in word :
    if(i == " "):
        s = s + 1  
print(s)


# In[6]:


# to count actual characters in the word
total_word = n - s
print(total_word)


# In[ ]:




