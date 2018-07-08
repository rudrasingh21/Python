	
------------------------------------------
lambda, map() and filter()
------------------------------------------

The general syntax of a lambda function is quite simple: 

lambda argument_list: expression	

The following example of a lambda function returns the sum of its two arguments:

>>> sum = lambda x, y : x + y
>>> sum(3,4)
	7
	
The above example might look like a plaything for a mathematician. A formalism which turns an easy to comprehend issue into an abstract harder to grasp formalism. Above all, we could have had the same effect by just using the following conventional function definition: 

>>> def sum(x,y):
...     return x + y
... 
>>> sum(3,4)
	7
	
------------------
The map() Function
------------------

Basic map() function.:-

As we have mentioned earlier, the advantage of the lambda operator can be seen when it is used in combination with the map() function. 
map() is a function which takes two arguments: 

r = map(func, seq)

The following example illustrates the way of working of map():

>>> def fahrenheit(T):
...     return ((float(9)/5)*T + 32)

>>> def celsius(T):
...     return (float(5)/9)*(T-32)
 
>>> temp = (36.5, 37, 37.5, 38, 39)

>>> F = map(fahrenheit, temp)

>>> C = map(celsius, F)

>>> temp_in_Fahren = list(map(fahrenheit, temp))

>>> temp_in_Celsius = list(map(celsius, temp_in_Fahren))

>>> print(temp_in_Fahren)
[97.7, 98.60000000000001, 99.5, 100.4, 102.2]

>>> print(temp_in_Celsius)
[36.5, 37.00000000000001, 37.5, 38.00000000000001, 39.0]

------
In the example above we haven't used lambda. By using lambda, we wouldn't have had to define and name the functions fahrenheit() and celsius().
You can see this in the following interactive session:
------

>>> C = [39.2, 36.5, 37.3, 38, 37.8] 

>>> F = list(map(lambda x: (float(9)/5)*x + 32, C))

>>> print(F)
[102.56, 97.7, 99.14, 100.4, 100.03999999999999]

>>> C = list(map(lambda x: (float(5)/9)*(x-32), F))

>>> print(C)
[39.2, 36.5, 37.300000000000004, 38.00000000000001, 37.8]

------
map() can be applied to more than one list. The lists don't have to have the same length. map() will apply its lambda function to the elements of the argument lists.
------

>>> a = [1, 2, 3, 4]
>>> b = [17, 12, 11, 10]
>>> c = [-1, -4, 5, 9]

>>> list(map(lambda x, y : x+y, a, b))
[18, 14, 14, 14]

>>> list(map(lambda x, y, z : x+y+z, a, b, c))
[17, 10, 19, 23]

>>> list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c))
[37.5, 33.0, 24.5, 21.0]

If one list has less elements than the others, map will stop, when the shortest list has been consumed:

>>> a = [1, 2, 3]
>>> b = [17, 12, 11, 10]
>>> c = [-1, -4, 5, 9]

>>> list(map(lambda x, y, z : 2.5*x + 2*y - z, a, b, c))
[37.5, 33.0, 24.5]
>>> 

----------
Filtering
----------

filter(function, sequence)

offers an elegant way to filter out all the elements of a sequence "sequence", for which the function function returns True.

>>> fibonacci = [0,1,1,2,3,5,8,13,21,34,55]

>>> odd_numbers = list(filter(lambda x: x % 2, fibonacci))

>>> print(odd_numbers)
[1, 1, 3, 5, 13, 21, 55]

>>> even_numbers = list(filter(lambda x: x % 2 == 0, fibonacci))

>>> print(even_numbers)
[0, 2, 8, 34]

>>> # or alternatively:
... 
>>> even_numbers = list(filter(lambda x: x % 2 -1, fibonacci))
>>> print(even_numbers)
[0, 2, 8, 34]
>>> 

--------


