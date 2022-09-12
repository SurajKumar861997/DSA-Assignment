#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Q1. Write a program to find all pairs of an integer array whose sum is equal to a given number?

def printPairs(arr, n, sum):
     
    mydict = dict()
 

    for i in range(n):
        temp = sum - arr[i]
        if temp in mydict:
            count = mydict[temp]
            for j in range(count):
                print("(", temp, ", ", arr[i],
                      ")", sep = "", end = '\n')
                       
        if arr[i] in mydict:
            mydict[arr[i]] += 1
        else:
            mydict[arr[i]] = 1
 
if __name__ == '__main__':
     
    arr = [ 1, 5, 7, -1, 5 ]
    n = len(arr)
    sum = 6
 
    printPairs(arr, n, sum)


# In[2]:


# Q2. Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverseList(A, start, end):
    while start < end:
        A[start], A[end] = A[end], A[start]
        start += 1
        end -= 1
 

A = [1, 2, 3, 4, 5, 6]
print(A)
reverseList(A, 0, 5)
print("Reversed list is")
print(A)


# In[3]:


# Q3. Write a program to check if two strings are a rotation of each other?

def areRotations(string1, string2):
    size1 = len(string1)
    size2 = len(string2)
    temp = ''
 
    # Check if sizes of two strings are same
    if size1 != size2:
        return 0
 
    # Create a temp string with value str1.str1
    temp = string1 + string1
 
    # Now check if str2 is a substring of temp
    if (temp.count(string2)> 0):
        return 1
    else:
        return 0
 
string1 = "AACD"
string2 = "ACDA"
 
if areRotations(string1, string2):
    print ("Strings are rotations of each other")
else:
    print ("Strings are not rotations of each other")


# In[4]:


# Q4. Write a program to print the first non-repeated character from a string?

NO_OF_CHARS = 256
 
def getCharCountArray(string):
    count = [0] * NO_OF_CHARS
    for i in string:
        count[ord(i)]+= 1
    return count
 

def firstNonRepeating(string):
    count = getCharCountArray(string)
    index = -1
    k = 0
 
    for i in string:
        if count[ord(i)] == 1:
            index = k
            break
        k += 1
 
    return index
 

string = "RakeshKumarBehera"
index = firstNonRepeating(string)
if index == 1:
    print ("Either all characters are repeating or string is empty")
else:
    print ("First non-repeating character is" , string[index])


# In[5]:


# Q5. Read about the Tower of Hanoi algorithm. Write a program to implement it.

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)
 
N = 3
 
TowerOfHanoi(N, 'A', 'C', 'B')


# In[6]:


# Q6. Read about infix, prefix, and postfix expressions. Write a program to convert postfix to prefix expression.

s = "*-A/BC-/AKL"
stack = []
operators = set(['+', '-', '*', '/', '^'])
s = s[::-1]
 
for i in s:
    if i in operators:
 
        a = stack.pop()
        b = stack.pop()
 
        temp = a+b+i
        stack.append(temp)
    else:
        stack.append(i)
 
print(*stack)


# In[7]:


# Q7. Write a program to convert prefix expression to infix expression.

def prefixToInfix(prefix):
    stack = []
     
    i = len(prefix) - 1
    while i >= 0:
        if not isOperator(prefix[i]):
             
            stack.append(prefix[i])
            i -= 1
        else:
           
            str = "(" + stack.pop() + prefix[i] + stack.pop() + ")"
            stack.append(str)
            i -= 1
     
    return stack.pop()
 
def isOperator(c):
    if c == "*" or c == "+" or c == "-" or c == "/" or c == "^" or c == "(" or c == ")":
        return True
    else:
        return False
 
if __name__=="__main__":
    str = "*-A/BC-/AKL"
    print(prefixToInfix(str))


# In[8]:


# Q8. Write a program to check if all the brackets are closed in a given code snippet.

def areBracketsBalanced(expr):
    stack = []
 
    for char in expr:
        if char in ["(", "{", "["]:
 
            stack.append(char)
        else:
 
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if char != ")":
                    return False
            if current_char == '{':
                if char != "}":
                    return False
            if current_char == '[':
                if char != "]":
                    return False
 
    # Check Empty Stack
    if stack:
        return False
    return True
 
 
# Driver Code
if __name__ == "__main__":
    expr = "{()}[]"
 
    # Function call
    if areBracketsBalanced(expr):
        print("closed")
    else:
        print("Not closeded")


# In[9]:


# Q9. Write a program to reverse a stack.

class Stack:
  
    def __init__(self):
        self.Elements = []
          
    def push(self, value):
        self.Elements.append(value)
        
    def pop(self):
        return self.Elements.pop()
      
    def empty(self):
        return self.Elements == []
      
    def show(self):
        for value in reversed(self.Elements):
            print(value)
  
def BottomInsert(s, value):
    
    if s.empty(): 
          
        s.push(value)
          
    else:
        popped = s.pop()
        BottomInsert(s, value)
        s.push(popped)
  
def Reverse(s):
    if s.empty():
        pass
    else:
        popped = s.pop()
        Reverse(s)
        BottomInsert(s, popped)
    
stk = Stack()
  
stk.push(1)
stk.push(2)
stk.push(3)
stk.push(4)
stk.push(5)
  
print("Original Stack")
stk.show()
  
print("\nStack after Reversing")
Reverse(stk)
stk.show()


# In[10]:


# Q10. Write a program to find the smallest number using a stack.

class MinStack(object):

   min=float('inf')

   def __init__(self):
      self.min=float('inf')
      self.stack = []

   def push(self, x):
      if x<=self.min:
         self.stack.append(self.min)
         self.min = x
      self.stack.append(x)

   def pop(self):
      t = self.stack[-1]
      self.stack.pop()
      if self.min == t:
         self.min = self.stack[-1]
         self.stack.pop()

   def top(self):
      return self.stack[-1]

   def getMin(self):
      return self.min

m = MinStack()

m.push(-2)
m.push(0)
m.push(-3)
print(m.getMin())

m.pop()
print(m.top())
print(m.getMin())


# In[ ]:




