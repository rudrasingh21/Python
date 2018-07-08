
---------------
Dictionaries:-
---------------

Dictionaries don't support the sequence operation of the sequence data types like strings, tuples and lists. Dictionaries belong to the built-in mapping type.

Examples of Dictionaries:-

>>> city_population = {"New York City":8550405, "Los Angeles":3971883, "Toronto":2731571, "Chicago":2720546, "Houston":2296224, "Montreal":1704694, "Calgary":1239220, "Vancouver":631486, "Boston":667137}

If we want to get the population of one of those cities, all we have to do is to use the name of the city as an index:

>>> city_population["New York City"]
8550405

>>> city_population["Toronto"]
2731571

---------

If you look at the way, we have defined our dictionary, you might get the impression that we have an ordering in our dictionary, i.e. thefirst one "New York City", the second one "Los Angeles" and so on. 

But be aware of the fact that there is no ordering in dictionaries. That's the reason, why the output of the city dictionary, doesn't reflect the "original ordering":

---------

>>> city = {'Toronto': 2615060, 'Ottawa': 883391, 'Los Angeles': 3792621, 'Chicago': 2695598, 'New York City': 8175133, 'Boston': 62600, 'Washington': 632323, 'Montreal': 11854442}

Therefore it is neither possible to access an element of the dictionary by a number, like we did with lists:

>>> city[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in 
KeyError: 0

--------------------
Adding Entry in DIR
--------------------

>>>city ["A"] = 1111

>>>city

{'A': 1111,
 'Boston': 667137,
 'Calgary': 1239220,
 'Chicago': 2720546,
 'Houston': 2296224,
 'Los Angeles': 3971883,
 'Montreal': 1704694,
 'New York City': 8550405,
 'Toronto': 2731571,
 'Vancouver': 631486}
 
 ----------------------
 Altering Values in DIR
 ----------------------
 
In [21]: food
Out[21]: {'egg': 'yes', 'ham': 'yes', 'spam': 'no'}
 
In [22]: food ["A"] = "Amla"

In [23]: food
Out[23]: {'A': 'Amla', 'egg': 'yes', 'ham': 'yes', 'spam': 'no'}


----------Change Value of spam from no to yes.

In [25]: food ["spam"] = "Yes"

In [26]: food
Out[26]: {'A': 'Amla', 'egg': 'yes', 'ham': 'yes', 'spam': 'Yes'}

-----------------

In [27]: en_de = {"red" : "rot", "green" : "grün", "blue" : "blau", "yellow":"gelb"}

In [28]: print(en_de["red"])
rot

In [29]: print(en_de)
{'blue': 'blau', 'green': 'grün', 'red': 'rot', 'yellow': 'gelb'}

---------------------------

Operators on Dictionaries:-

---------------------------

len(d)		:-	returns the number of stored entries, i.e. the number of (key,value) pairs.

del d[k]	:-	deletes the key k together with his value

k in d		:-	True, if a key k exists in the dictionary d

k not in d	:-	True, if a key k doesn't exist in the dictionary d

------

In [2]: en_de
Out[2]: {'blue': 'blau', 'green': 'grün', 'red': 'rot', 'yellow': 'gelb'}

In [4]: len(en_de)
Out[4]: 4

------

In [6]: en_de
Out[6]: {'blue': 'blau', 'green': 'grün', 'red': 'rot', 'yellow': 'gelb'}

In [7]: "blau" in en_de
Out[7]: False

In [8]: "blue" in en_de
Out[8]: True

In [9]: "a" in en_de
Out[9]: False

------

In [6]: en_de
Out[6]: {'blue': 'blau', 'green': 'grün', 'red': 'rot', 'yellow': 'gelb'}

In [12]: del en_de["blue"]

In [13]: en_de
Out[13]: {'green': 'grün', 'red': 'rot', 'yellow': 'gelb'}

------

In [12]: del en_de["blue"]

In [13]: en_de
Out[13]: {'green': 'grün', 'red': 'rot', 'yellow': 'gelb'}

In [14]: "green" in en_de
Out[14]: True

In [15]: "green" not in en_de
Out[15]: False

------

Iterating over a Dictionary:-

No method is needed to iterate over the keys of a dictionary:

In [1]: d = {"a":123, "b":34, "c":304, "d":99}

In [2]: for i in d: print(i)
a
c
d
b

------Alternate:-

But it's possible to use the method keys(), but we will get the same result:

In [3]: d = {"a":123, "b":34, "c":304, "d":99}

In [4]: for i in d.keys(): print(i)
a
c
d
b

-------

The method values() is a convenient way for iterating directly over the values:

In [5]: for i in d.values(): print(i)
123
304
99
34

-----------------------------------
Turn Lists into Dictionaries:-
-----------------------------------


In [1]: A
Out[1]: ['PIZZA', 'BURGER', 'PASTA', 'SALAD']

In [2]: B
Out[2]: ['ITALY', 'GERMANY', 'SPAIN', 'USA']

In [3]: z = zip (B,A)

In [4]: z
Out[4]: <zip at 0x7fe08c346988>

In [5]: country_dished = list(z)

In [6]: print(country_dishes)
[('ITALY', 'PIZZA'), ('GERMANY', 'BURGER'), ('SPAIN', 'PASTA'), ('USA', 'SALAD')]

In [7]: Dic_country_dishes = dict(country_dishes)

In [8]: print(Dic_country_dishes)
{'GERMANY': 'BURGER', 'USA': 'SALAD', 'ITALY': 'PIZZA', 'SPAIN': 'PASTA'}

----------Other Way:--

In [24]: dict(zip(B,A))
Out[24]: {'GERMANY': 'BURGER', 'ITALY': 'PIZZA', 'SPAIN': 'PASTA', 'USA': 'SALAD'}

--------

>>> l1 = ["a","b","c"]
>>> l2 = [1,2,3]
>>> c = zip(l1, l2)
>>> for i in c:
...     print(i)
... 
('a', 1)
('b', 2)
('c', 3)





