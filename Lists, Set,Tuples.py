

In the following code snippet,
y points to the same memory location than X. 
We can see this by applying the id() function on x and y. 
But unlike "real" pointers like those in C and C++, things change, when we assign a new value to y. 
In this case y will receive a separate memory location, as we have seen in the chapter "Data Types and Variables" and can see in the following example: 

>>> x = 3
>>> y = x
>>> print(id(x), id(y))
9251744 9251744
>>> y = 4
>>> print(id(x), id(y))
9251744 9251776
>>> print(x,y)
3 4
>>> 

***************************************Lists***********************************

In [1]: list1 = [1, 2, 3, 4]

In [2]: list2 = [5]

In [3]: list1.append(list2)

In [4]: list1
Out[4]: [1, 2, 3, 4, [5]]			#for this Python provides the method 'extend'

In [5]: list1.append(6)

In [6]: list1
Out[6]: [1, 2, 3, 4, [5], 6]


NOTE:- To this purpose, Python provides the method 'extend'. It extends a list by appending all the elements of an iterable like a list, a tuple or a stringto a list:

In [7]: list3   =   [11,12,13,14]

In [8]: list4   =   [15,16]

In [9]: list3.extend(list4)

In [10]: list3
Out[10]: [11, 12, 13, 14, 15, 16]

--------

In [1]: A = list(range(1,6))

In [2]: A
Out[2]: [1, 2, 3, 4, 5]

--------extend

In [13]: list = ["a","b","c"]

In [14]: lang = "python"

In [15]: list.extend(lang)

In [16]: list
Out[16]: ['a', 'b', 'c', 'p', 'y', 't', 'h', 'o', 'n']

------append

In [18]: land2 = "java"

In [19]: list.append(land2)

In [20]: list
Out[20]: ['a', 'b', 'c', 'p', 'y', 't', 'h', 'o', 'n', 'java']

------append

In [21]: lang3 = ["sql","plsql"]

In [24]: list.append(lang3)

In [25]: list
Out[25]: ['a', 'b', 'c', 'p', 'y', 't', 'h', 'o', 'n', 'java', ['sql', 'plsql']]

------extend

In [26]: list.extend(lang3)

In [27]: list
Out[27]: 
['a', 'b', 'c', 'p', 'y', 't', 'h', 'o', 'n', 'java', ['sql', 'plsql'], 'sql', 'plsql']

------extend

>>> lst = ["Java", "C", "PHP"]
>>> t = ("C#", "Jython", "Python", "IronPython")

>>> lst.extend(t)

>>> lst
['Java', 'C', 'PHP', 'C#', 'Jython', 'Python', 'IronPython']
>>> 

--------------
pop and append
--------------

s.append(x) :- This method appends an element to the end of the list "s".

>>> lst = [3, 5, 7]
>>> lst.append(42)
>>> lst
[3, 5, 7, 42]

s.pop(i)	:-	'pop' returns the ith element of a list s. The element will be removed from the list as well.

>>> cities = ["Hamburg", "Linz", "Salzburg", "Vienna"]
>>> cities.pop(0)
'Hamburg'
>>> cities
['Linz', 'Salzburg', 'Vienna']
>>> cities.pop(1)
'Salzburg'
>>> cities
['Linz', 'Vienna']

----------------------------------------------------
Extending and Appending Lists with the '+'-Operator
----------------------------------------------------

There is an alternative to 'append' and 'extend'. '+' can be used to combine lists.

>>> level = ["beginner", "intermediate", "advanced"]
>>> other_words = ["novice", "expert"]

>>> level + other_words
['beginner', 'intermediate', 'advanced', 'novice', 'expert']

------

>>> L = [3, 4]
>>> L = L + [42]
>>> L
[3, 4, 42]

------

Even though we get the same result, it is not an alternative to 'append' and 'extend':
>>> L = [3, 4]
>>> L.append(42)
>>> L
[3, 4, 42]


>>> L = [3, 4]
>>> L.extend([42])
>>> L
[3, 4, 42]

------

>>> list = ['larry', 'curly', 'moe']
  
>>> list.append('shemp')         ## append elem at end

>>> list.insert(0, 'xxx')        ## insert elem at index 0

>>> list.extend(['yyy', 'zzz'])  ## add list of elems at end

>>> print list  				 
## ['xxx', 'larry', 'curly', 'moe', 'shemp', 'yyy', 'zzz']

>>> print list.index('curly')    
## 2

>>> list.remove('curly')         ## search and remove that element
  
>>> list.pop(1)                  ## removes and returns 'larry'

>>> print list  				 
## ['xxx', 'moe', 'shemp', 'yyy', 'zzz']

-------

Python Sorting:-

>>> list
[5, 1, 4, 3, 2, 6]

>>> print sorted(list)
[1, 2, 3, 4, 5, 6]

>>> list = ['larry', 'curly', 'moe']

>>> print sorted(list)
['curly', 'larry', 'moe']

--------

Custom Sorting With key :-

>>> strs = ['ccc', 'aaaa', 'd', 'bb']

>>> print sorted(strs ,key=len)
['d', 'bb', 'ccc', 'aaaa']

--------

sort() method :-

As an alternative to sorted(), the sort() method on a list sorts that list into ascending order, e.g. list.sort(). 

The sort() method changes the underlying list and returns None, so use it like this:

alist.sort()            ## correct
alist = blist.sort()    ## NO incorrect, sort() returns None

**************************************************SET***************************************


Sets :- Sets are lists with no duplicate entries. We can not get values using index.


print(set("my name is Eric and Eric is my name".split()))

{'my', 'and', 'name', 'is', 'Eric'}

-----

a = set(["Jake", "John", "Eric"])
print(a)

b = set(["John", "Jill"])
print(b)

{'Eric', 'Jake', 'John'}
{'Jill', 'John'}

-----

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.intersection(b))
print(b.intersection(a))

{'John'}
{'John'}

------

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.symmetric_difference(b))
print(b.symmetric_difference(a))

{'Eric', 'Jill', 'Jake'}
{'Eric', 'Jake', 'Jill'}

-----

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.difference(b))
print(b.difference(a))

{'Eric', 'Jake'}
{'Jill'}

-----

a = set(["Jake", "John", "Eric"])
b = set(["John", "Jill"])

print(a.union(b))

{'Eric', 'Jake', 'John', 'Jill'}

------

a = ["Jake", "John", "Eric"]
b = ["John", "Jill"]

A = set(a)
B = set(b)

print(A.difference(B))

**************************************************TUPLE***************************************

A tuple is a fixed size grouping of elements, such as an (x, y) co-ordinate. 

Tuples are like lists, except they are immutable and do not change size.

>>> tuple = (1, 2, 'hi')

>>> print len(tuple)
3

>>> print tuple[2]    
hi

>>> tuple[2] = 9	## NO, tuples cannot be changed

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment


>>>tuple = (1, 2, 'bye', 9)  ## this works

------
As above this is different from list.

>>> list =[5,1,4,3,2,6]
>>> list[2] = 9
>>> list
[5, 1, 9, 3, 2, 6]
------

Assigning a tuple to an identically sized tuple of variable names assigns all the
corresponding values. If the tuples are not the same size, it throws an error. 
This feature works for lists too.

>>>(x, y, z) = (42, 13, "hike")

>>>print z  
hike