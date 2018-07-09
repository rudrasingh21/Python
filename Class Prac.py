class Employee:
 raise_amount = 1.04
 
 def __init__(self, first, last, pay):
  self.fname	= first
  self.lname	= last
  self.pay	= pay
  self.email	= first + '.' + '@gmail.com'
  
 def fullname(self):
  return(self.fname,self.lname)
  
 def apply_raise(self):
  self.pay = int(self.pay * raise_amount)

emp1=Employee('rudra','singh',1000)
emp2=Employee('seema','singh',2000)

print(emp1.pay)

print(

-----------------

class Employee:
 raise_amount = 2
 
 def __init__(self, first, last, pay):
  self.fname	= first
  self.lname	= last
  self.pay	= pay
  self.email	= first + '.' + '@gmail.com'
  
 def fullname(self):
  return(self.fname,self.lname)
  
 def apply_raise(self):
  self.pay = int(self.pay * Employee.raise_amount)

emp1=Employee('rudra','singh',1000)
emp2=Employee('seema','singh',2000)

print(emp1.pay)
print(emp2.pay)

emp1.apply_raise()
print(emp2.pay)

------------------

Class Method:--

class Employee:
 raise_amount = 2
 def __init__(self, first, last, pay):
  self.fname	= first
  self.lname	= last
  self.pay	= pay
  self.email	= first + '.' + '@gmail.com'
  
 def fullname(self):
  return(self.fname,self.lname)
  
 def apply_raise(self):
  self.pay = int(self.pay * Employee.raise_amount)
  
 @classmethod
 def set_raise_amt(cls, amount):
  cls.raise_amount = amount

emp1=Employee('rudra','singh',1000)
emp2=Employee('seema','singh',2000)

>>> print(emp1.pay)
1000
>>> print(emp2.pay)
2000

>>> print(Employee.raise_amount)
2
>>> print(emp1.raise_amount)
2
>>> print(emp2.raise_amount)
2

------------------------------------------------------------------------------------
Getting employee in string and after parsing getting the result using CLASS.

class Employee:
 raise_amount = 2
 def __init__(self, first, last, pay):
  self.fname	= first
  self.lname	= last
  self.pay	= pay
  self.email	= first + '.' + '@gmail.com'
  
 def fullname(self):
  return(self.fname,self.lname)
  
 def apply_raise(self):
  self.pay = int(self.pay * Employee.raise_amount)
  
 @classmethod
 def set_raise_amt(cls, amount):
  cls.raise_amount = amount

Employee.set_raise_amt(1.05)

emp_str_1 = 'John-Doe-70000'		#Getting employees as string
emp_str_2 = 'Steve-Smith-30000'		#Getting employees as string
emp_str_3 = 'Jane-Doe-90000'		#Getting employees as string

first, last, pay = emp_str_1.split('-')		#Splitting string


new_emp_1 = Employee(first, last, pay)		#Creating employee using class based on above split string.

print(new_emp_1.email)				#Printing new_emp_1
print(new_emp_1.pay)				#Printing new_emp_1

-------------------------------------------------------------------------------------------------------
class Employee:
 raise_amount = 2
 def __init__(self, first, last, pay):
  self.fname	= first
  self.lname	= last
  self.pay	= pay
  self.email	= first + '.' + '@gmail.com'
  self.FULL = first + ' ' + last		#Added this as part of this testing
  
 def fullname(self):
  return(self.fname,self.lname)
  
 def apply_raise(self):
  self.pay = int(self.pay * Employee.raise_amount)
  
 @classmethod
 def set_raise_amt(cls, amount):
  cls.raise_amount = amount


emp_str_1 = 'rudra_vik_300'
first,last,pay=emp_str_1.split('_')
new_emp = Employee(first,last,pay)
print(new_emp.FULL)
rudra vik

new_emp.fullname()
('rudra', 'vik')

----------------------------------------------------------

class Employee:
 raise_amount = 2
 def __init__(self, first, last, pay):
  self.fname	= first
  self.lname	= last
  self.pay	= pay
  self.email	= first + '.' + '@gmail.com'
  
 def fullname(self):
  return(self.fname,self.lname)
  
 def apply_raise(self):
  self.pay = int(self.pay * Employee.raise_amount)
  
 @classmethod
 def set_raise_amt(cls, amount):
  cls.raise_amount = amount
  
 @classmethod
 def from_string(cls, emp_str):				New method added 
  first,last,pay = emp_str.split('-')
  return cls(first,last,pay)


>>> emp_str_1 = 'rudra-vikram-300'
>>> new_emp_1 = Employee.from_string(emp_str_1)

>>> print(new_emp_1.fullname())
('rudra', 'vikram')

>>> print(new_emp_1.pay)

---------------------------Static Method------------------------

class Employee:
 num_of_emp = 0
 raise_amt = 2
 
 def __init__(self,first,last,pay):
  self.fname = first
  self.lname = last
  self.pay  = pay
  self.email = first + '.' + last + '@gmail.com'
  
 def fllname(self):
  return (self.fname + ' ' +self.lname)
  
 def apply_raise(self):
  self.pay = int(self.pay * self.raise_amt)
  
 @classmethod
 def set_raise_amount(cls, amount):
  cls.raise_amt = amount


Employee.set_raise_amt(1.05)

emp_str_1 = 'John-Doe-70000'		
emp_str_2 = 'Steve-Smith-30000'		
emp_str_3 = 'Jane-Doe-90000'		

first, last, pay = emp_str_1.split('-')		

new_emp_1 = Employee(first, last, pay)		

print(new_emp_1.email)				
print(new_emp_1.pay)				

Result:-
John.Doe@email.com
70000

  
-----------------Use a CLASS method for splitting :----------------

class Employee:
 num_of_emp = 0
 raise_amt = 1.04
 
 def __init__(self,first,last,pay):
  self.fname = first
  self.lname = last
  self.pay = pay
  self.email = first + '.' + last + '@gmail.com'
  
 def fullname(self):
  return (self.fname,self.lname)
  
 def apply_raise(self):
  self_pay = int(self.pay * self.raise_amt)
  
 @classmethod
 def set_raise_amt(cls, amount):
  cls.raise_amt = amount
  
 @classmethod
 def from_string(cls,emp_str):
  first,last,pay = emp_str.split('-')
  return cls(first,last,pay)

emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'

new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

---------------------Use a STATIC method for splitting :----------------

class Employee:
 num_of_emp = 0
 raise_amt = 1.04
 
 def __init__(self,first,last,pay):
  self.fname = first
  self.lname = last
  self.pay = pay
  self.email = first + '.' + last + '@gmail.com'
 Employee.num_of_emp += 1
 
 def fullname(self):
  return (self.fname,self.lname)
  
 def apply_raise(self):
  self_pay = int(self.pay * self.raise_amt)
  
 @classmethod
 def set_raise_amt(cls, amount):
  cls.raise_amt = amount
  
 @classmethod
 def from_string(cls,emp_str):
  first,last,pay = emp_str.split('-')
  return cls(first,last,pay)
  
 @staticmethod
 def is_workday(day):
  if day.weekday() == 5 or day.weekday() == 6:
    return False
  return True

import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))

note:- Will return true if a weekday , otherwise false.

------------------------Creating a subclass :----------------

class Employee:
 num_of_emp = 0
 raise_amt = 1.04
 
 def __init__(self,first,last,pay):
  self.fname = first
  self.lname = last
  self.pay = pay
  self.email = first + '.' + last + '@gmail.com'
 Employee.num_of_emp += 1
 
 def fullname(self):
  return (self.fname,self.lname)
  
 def apply_raise(self):
  self_pay = int(self.pay * self.raise_amt)

class Developer(Employee):
  pass

dev_1 = Developer('Corey', 'Schafer', 50000)

>>> print(dev_1.email)
Corey.Schafer@gmail.com

