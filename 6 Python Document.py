#!/usr/bin/env python
# coding: utf-8

# # Map, Filter, Reduce, Lambda & Recursion

# ## Tasks Today:
# 
# 1) <b>Lambda Functions</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Saving to a Variable <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Multiple Inputs <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Passing a Lambda into a Function <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; e) Returning a Lambda from a Function <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; f) In-Class Exercise #1 <br>
# 2) <b>Map</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Using Lambda's with Map <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #2 <br>
# 3) <b>Filter</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Using Lambda's with Filter <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #3 <br>
# 4) <b>Reduce</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Syntax <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Using Lambda's with Reduce <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #4 <br>
# 5) <b>Recursion</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Implementing a Base <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Writing a Factorial Function <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #5 <br>
# 6) <b>Generators & Iterators</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Yield Keyword <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Inifinite Generator <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) In-Class Exercise #6 <br>
# 7) <b>Exercises</b> <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; a) Exercise #1 - Filtering Empty Strings <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; b) Exercise #2 - Sorting with Last Name <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; c) Exercise #3 - Conversion to Farhenheit <br>
#  &nbsp;&nbsp;&nbsp;&nbsp; d) Exercise #4 - Fibonacci Sequence <br>

# ## Lambda Functions <br>
# <p>Lambda functions... or "Anonymous Functions" are referring to inline functions with no name. The keyword lambda denotes the no name function, and executes within a single line. Without saving it to a variable; however, it is not able to be used, unless passed in either as a paramater or within list comprehension.<br>Written as "(keyword lambda) (one or more inputs) (colon) (function to be executed)"</p>

# #### Syntax

# In[1]:


def addTwo(x):
    return x + 2

print(addTwo(4))


print((lambda x: x + 2)(4))

a_num = 4
print((lambda x: x + 2)(a_num))


# #### Saving to a Variable

# In[2]:


f_test = lambda x: x + 2


f_test(4)


# #### Multiple Inputs

# In[5]:


print((lambda x, y, z: x * y * z)(3, 5, 8))

x_test = lambda x, y, z: x * y * z
print(x_test(3, 5, 8))


# #### Passing a Lambda into a Function

# In[6]:


def multiply(f, num):
    '''
        f expects a lambda function
        num expects a number
    '''
    return f(num)

multiply(lambda x: x * x, 4)


# #### Returning a Lambda from a Function

# In[7]:


def multiply_tst(num):
    return num * 4


def returnFunc():
    test = 4 
    def multiply(num):
        return num * 2
    return multiply
f_return = returnFunc()
print(returnFunc())
print(f_return(4))


# #### If Statements within Lambdas

# In[9]:


f_condition = lambda num : num * 2 if num > 10 else num + 2

print(f_condition(8))
print(f_condition(12))
print(f_condition(10))


# #### In-Class Exercise #1 <br>
# <p>Write an anonymous function that cubes the arguments passed in and assign the anonymous function to a variable 'f'.</p>

# In[10]:


f = lambda x: x ** 3


result = f(3)  
print(result)  


# ## Map <br>
# <p>The map function allows you to iterate over an entire list while running a function on each item of the list. This is why the map function works well with lambda's, because it simplifies things and you write less lines of code.<br>The syntax for a map function is "map(function to be used, list to be used)"<br>However, you must be careful, as the map function returns a map object, not a list. To turn it into a list we use the list() type conversion.</p>

# #### Syntax

# In[12]:


def squared(num, num2):
    if num < 10 and num2 < 10:
        return num ** 2, num2 **2
    else:
        return num, num2
numbers = [4, 11, 20, 3, 15, 20]
more_nums = [4, 10, 3, 2, 6]

squared_nums_map = list(map(squared, numbers, more_nums))
print(squared_nums_map)


# #### Using Lambda's with Map

# In[16]:


print(list(map(lambda x, y: (x ** 2, y ** 2) if x < 10 and y < 10 else (x,y), numbers, more_nums)))


# #### In-Class Exercise #2 <br>
# <p>Use the map function to double each number and minus it by one in the list by using a lambda function</p>

# In[17]:


# Sample list of numbers
numbers = [1, 2, 3, 4, 5]

# Using map with lambda function to double each number and subtract one
transformed_numbers = list(map(lambda x: 2 * x - 1, numbers))

# Print the transformed numbers
print(transformed_numbers)


# ## Filter() <br>
# <p>Filter's are similar to the map function, where you're able to pass a function argument and a list argument and filter out something from the list based on the conditions passed. Similar to the map function, it returns a filter object, so you need to type convert it to a list()</p>

# #### Syntax

# In[21]:


names = [ 'Bob', 'Andy', 'Max', 'Evan', 'Angelica']
def a_names(name):
    if name[0].lower() == 'a':
        return True
    elif name[0].lower() == 'b':
        return True
    else:
        return False
new_names_list = list(filter(a_names, names))
print(new_names_list)


# #### Using Lambda's with Filter()

# In[23]:


new_names_lambda = list(filter(lambda name: True if name[0].lower() == 'a' else False, names))
print(new_names_lambda)


# #### In-Class Exercise #3 <br>
# <p>Filter out all the numbers that are below the mean of the list.<br><b>Hint: Import the 'statistics' module</b></p>

# In[24]:


def filter_numbers_above_mean(numbers):
    # Calculate the mean of the list
    mean = sum(numbers) / len(numbers)
    
    # Use filter to keep numbers >= mean
    filtered_numbers = list(filter(lambda x: x >= mean, numbers))
    
    return filtered_numbers

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
filtered_numbers = filter_numbers_above_mean(numbers)
print(filtered_numbers)


# ## Reduce() <br>
# <p>Be very careful when using this function, as of Python 3 it's been moved to the 'functools' library and no longer is a built-in function.<br>The creator of Python himself, says to just use a for loop instead.</p>

# #### Syntax

# In[25]:


from functools import reduce

list_1 = [2, 4, 6, 8, 10]

def addNums(num1, num2):
    return num1 + num2

result_add = reduce(addNums, list_1)

print(result_add)

def subtractNums(num1, num2):
    return num1 - num2
result_sub = reduce(subtractNums, list_1)
print(result_sub)


# #### Using Lambda's with Reduce()

# In[26]:


result_lamb = reduce(lambda x, y: x + y, list_1)
print(result_lamb)


# #### In-Class Exercise #4 <br>
# <p>Use the reduce function to multiply the numbers in the list below together with a lambda function.</p>

# In[27]:


my_list = [1, 2, 3, 4]


# ## Recursion <br>
# <p>Recursion means that a function is calling itself, so it contanstly executes until a base case is reached. It will then push the returning values back up the chain until the function is complete. A prime example of recursion is computing factorials... such that 5! (factorial) is 5*4*3*2*1 which equals 120.</p>

# #### Implementing a Base Case

# In[28]:


def addNums(num):
    if num <= 1:
        print("addNums(1) = 1")
        return num
    else:
        print(f"addNums({num}) = {num} + addNums({num - 1})")
        return num + addNums(num - 1)
addNums(5)


# #### Writing a Factorial Function

# In[32]:


def factorial(num):
    if num <= 1:
        return 1
    else:
        return num + factorial(num - 1)
    
factorial(15)


# #### In-Class Exercise #5 <br>
# <p>Write a recursive function that subtracts all numbers to the argument given.</p>

# In[ ]:


def subtract_down_to_zero(n):
    # Base case: if n is 0, return 0
    if n == 0:
        return 0
    # Recursive case: subtract n from the result of subtract_down_to_zero(n-1)
    else:
        return n - subtract_down_to_zero(n - 1)

# Example usage:
number = 5
result = subtract_down_to_zero(number)
print(f"Result of subtracting down to zero from {number}: {result}")


# ## Generators <br>
# <p>Generators are a type of iterable, like lists or tuples. They do not allow indexing, but they can still be iterated through with for loops. They are created using functions and the yield statement.</p>

# #### Yield Keyword <br>
# <p>The yield keyword denotes a generator, it doesn't return so it won't leave the function and reset all variables in the function scope, instead it yields the number back to the caller.</p>

# In[34]:


def my_range(stop, start, step = 2):
    while start < stop:
        yield start 
        start += step
        
for i in my_range(20, start = 2):
    my_generator_value = i
    print(my_generator_value)
    
my_range(20, start = 2)


# #### Infinite Generator

# In[ ]:


# bad, never create infinite loops


# #### In-Class Exercise #6 <br>
# <p>Create a generator that takes a number argument and yields that number squared, then prints each number squared until zero is reached.</p>

# In[ ]:


def squared_numbers_generator(n):
    while n > 0:
        squared = n ** 2
        yield squared
        print(f"Number squared: {squared}")
        n -= 1

# Example usage:
number = 5
gen = squared_numbers_generator(number)

# Iterate over the generator and print each yielded value
for squared in gen:
    pass  # Do nothing with the generator values except iterating and printing

# Once the generator is exhausted, it has reached zero and no more values are yielded
print("Generator has reached zero.")


# # Exercises

# ### Exercise #1 <br>
# <p>Filter out all of the empty strings from the list below</p>
# 
# `Output: ['Argentina', 'San Diego', 'Boston', 'New York']`

# In[35]:


places = [" ","Argentina", " ", "San Diego","","  ","","Boston","New York"]

def filter_empty_strings(lst):
    return list(filter(lambda s: s != '', lst))

# Example list
my_list = ['Argentina', '', 'San Diego', '', 'Boston', 'New York', '']

# Filter empty strings
filtered_list = filter_empty_strings(my_list)
print(filtered_list)



# ### Exercise #2 <br>
# <p>Write an anonymous function that sorts this list by the last name...<br><b>Hint: Use the ".sort()" method and access the key"</b></p>
# 
# `Output: ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']`

# In[36]:


author = ["Joel Carter", "Victor aNisimov", "Andrew P. Garfield","David hassELHOFF","Gary A.J. Bernstein"]
# List of names
names = ['Victor aNisimov', 'Gary A.J. Bernstein', 'Joel Carter', 'Andrew P. Garfield', 'David hassELHOFF']

# Sort names by last name
names.sort(key=lambda x: x.split()[-1].lower())

# Print sorted names
print(names)



# ### Exercise #3 <br>
# <p>Convert the list below from Celsius to Farhenheit, using the map function with a lambda...</p>
# 
# `Output: [('Nashua', 89.6), ('Boston', 53.6), ('Los Angelos', 111.2), ('Miami', 84.2)]
# `

# In[37]:


# F = (9/5)*C + 32
places = [('Nashua',32),("Boston",12),("Los Angelos",44),("Miami",29)]
# List of tuples containing city and temperature in Celsius
cities = [('Nashua', 32), ('Boston', 12), ('Los Angelos', 44), ('Miami', 29)]

# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(temp_celsius):
    return (temp_celsius * 9/5) + 32

# Use map with lambda to convert Celsius to Fahrenheit for each tuple
cities_fahrenheit = list(map(lambda city_temp: (city_temp[0], celsius_to_fahrenheit(city_temp[1])), cities))

# Print the result
print(cities_fahrenheit)


# ### Exercise #4 <br>
# <p>Write a recursion function to perform the fibonacci sequence up to the number passed in.</p>
# 
# `Output for fib(5) => 
# Iteration 0: 1
# Iteration 1: 1
# Iteration 2: 2
# Iteration 3: 3
# Iteration 4: 5
# Iteration 5: 8`

# In[38]:


def fib(n):
    # Base case: fib(0) and fib(1) are both 1
    if n == 0 or n == 1:
        return 1
    
    # Recursive case: fib(n) = fib(n-1) + fib(n-2)
    result = fib(n-1) + fib(n-2)
    
    # Print the iteration number and the Fibonacci number
    print(f"Iteration {n}: {result}")
    
    # Return the Fibonacci number
    return result

# Example usage:
fib(5)


# In[ ]:




