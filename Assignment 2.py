#!/usr/bin/env python
# coding: utf-8

# In[1]:


# PROGRAM TO OBTAIN SUM OF 1ST AND LAST DIGIT OF THE NUMBER


# In[35]:


# TAKE AN INTEGER

int1 = input("Enter the Number :")

#str to list

int2 = list(int1)

# Number should not single digit
if (len(int2) < 2):
    print("Dont Enter SINGLE DIGIT Number")

else:
    # to add 1st and last digit

    first = int(int2[0])
    last = int(int2[-1])

    print("1st digit of number is :" ,first)
    print("last digit of number is :" ,last)

    result = first + last
    print("Final result is :" ,result)


# In[ ]:








# In[ ]:


# PROGRAM TO REVERSE THE GIVEN INTEGER


# In[43]:


# TAKE THE NUMBER

num1 = int(input("Enter the number :"))
print(num1)

# CONVERT THE GIVEN NUMBER INTO THE STRING

num2 = str(num1)
print(type(num2))

# CONVERTING TO LIST

list1 = list(num2)
print(list1)

# reversing the list

new = list1[::-1]
print(new)

#converting list to srting

rev = "".join(new)
result2 = int(rev)
print(result2)
print(type(result2))


# In[ ]:








# In[ ]:


'''program to obtain length (L) and breadth (B) of a rectangle and check whether
its area is greater or perimeter is greater or both are equal.'''


# In[50]:


# take length and breadth of rectangle

l = int(input("Enter Length og Rectangle : " ))
b = int(input("Enter breadth og Rectangle : " ))

# calculating area and perimeter

a = l * b 
print("Arae of Rectangle is : " ,area)
p = 2 * (l + b)
print("Perimeter of Rectangle is :" ,perimeter)

# Printing Conditions

if (a > p):
    print("Area is Greater than Perimeter of Rectangle")
    
elif (p > a):
    print("Perimeter is Greater than Area of Rectangle")

elif (a == p):
    print("Area and Perimeter both are equal")

else:
    pass


# In[ ]:








# In[ ]:


# to check whether a triangle is valid or not 


# In[13]:


# take angles and lengths of a triangle
# 3 Angles :
a1 = int(input("Enter 1st Angle of Triangle :"))
a2 = int(input("Enter 2nd Angle of Triangle :"))
a3 = int(input("Enter 3rd Angle of Triangle :"))

# 3 lenghts :
l1 = int(input("Enter 1st length of Triangle :"))
l2 = int(input("Enter 2nd length of Triangle :"))
l3 = int(input("Enter 3rd length of Triangle :"))

''' sum of all 3 angles is equal to 180 degree and 
sum of any 2 length of triangle is greater than 3rd length then 
condition of triangle is satisfied '''

if (a1 + a2 + a3 == 180 and l1 + l2 >= l3 and l2 + l3 >= l1 and l1 + l3 >= l2):
    print("\nall conditions are satisfied it is triangle")

else:
    print("\nit is not a triangle")


# In[ ]:








# In[ ]:


# to find 2nd largest number


# In[1]:


n1 = int(input("Enter 1st no. :"))
n2 = int(input("Enter 2nd no. :"))
n3 = int(input("Enter 3rd no. :"))

# condition to find 2nd largest number

list1 = [n1, n2, n3]
list1.sort()
print(list1)
print("2nd largest no. is :" ,list1[1])

