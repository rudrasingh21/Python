
A module is a file containing Python definitions and statements. 
The file name is the module name with the suffix .py appended. 
Within a module, the module’s name (as a string) is available as the value of the global variable __name__.

------------------------
MODULES in simple Words:-
------------------------

Modules is a way to reuse code written by someone else.

If you want to use math module , Just import it:-

>>>import math

>>> math.sqrt(16)
4.0

=>Check how many functions are present in math module.

>>> dir(math)
['__doc__', '__loader__', '__name__', '__package__', '__spec__', 'acos', 'acosh', 'asin', 'asinh', 'atan', 'atan2', 'atanh', 'ceil', 'copysign', 'cos', 'cosh', 'degrees', 'e', 'erf', 'erfc', 'exp', 'expm1', 'fabs', 'factorial', 'floor', 'fmod', 'frexp', 'fsum', 'gamma', 'gcd', 'hypot', 'inf', 'isclose', 'isfinite', 'isinf', 'isnan', 'ldexp', 'lgamma', 'log', 'log10', 'log1p', 'log2', 'modf', 'nan', 'pi', 'pow', 'radians', 'sin', 'sinh', 'sqrt', 'tan', 'tanh', 'tau', 'trunc']

>>> math.pi
3.141592653589793

>>> math.log10(100)

---------------------
Functions_test_Module:-
---------------------

def calcu_triangle_area(base,height):
    return 1/2*(base*height)

def calcu_sqr_area(length):
    return length*length
	
-------------

>>>import Functions_test_Module
>>>area = Functions_test_Module.calcu_sqr_area(5)
>>>print(area)

>>>import Functions_test_Module as f
>>>area = f.calcu_sqr_area(2)
>>>print(area)

#If module you want to import is not in the same dir ,
# use
>>>import sys

>>>sys.path.append("c:\Code") #path
>>>import Functions_test_Module as f
>>>area = f.calcu_triangle_area(5)
>>>print(area)

#installing Module
>>>import matplotlib

import error: module not found

>>>pip install matplotlib

This will install module successfully.