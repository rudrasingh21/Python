------
CLASS:--

1) Class is a blueprint for creating instances.

2) Here each unique employee we will create, as a instance of 	this class.

3) We also have Class veriable. AND Instance variable. 
 


--------
Creating an empty class:-

class Employee:
	pass
	
--------

Creating Instances of Employee class:-

emp_1 = Employee()
emp_2 = Employee()

emp_1 and emp_2 are the instances of the class.

--------

Let's Print:-

print(emp_1)
print(emp_2)

NOTE:- both will be employee object and they both will be unique.
Both will be at different location in the memory.

--------

Using INSTANCE Variable:-

class Employee:
	pass
	
emp_1 = Employee()
emp_2 = Employee()

#INSTANCE VARIABLE

emp_1.first = 'rudra'
emp_1.last  = 'singh'
emp_1.email = 'rudra.singh@gmail.com'
emp_1.pay   = 10000

#INSTANCE VARIABLE

emp_2.first = 'seema'
emp_2.last  = 'singh'
emp_2.email = 'seema.singh@gmail.com'
emp_2.pay   = 20000

print(emp_1.email)
print(emp_2.email)

------
Using Class:-

NOTE:- Class Variable are variable which are shared among Instances with in the class.
	   Class variable will be same for each variable.

class Employee:

	def __init__(self, first, last, pay): 
		self.fname  = first
		self.lname  = last
		self.pay 	= pay
		self.email  = first + '.' + last + '@gmail.com'
		
emp_1 = Employee('rudra','singh',10000)
emp_2 = Employee('seema','singh',20000)

print(emp_1.email)
print(emp_2.email)

# Other Way to print first and last name

print('{} {}'.format(emp_1.first, emp_2.last))

------

NOTE:- Better to create a METHOD for FULL NAME as we are doing this only for a single employee.

class Employee:
	
	def __init__(self, first, last, pay):
		self.fname	= first
		self.lname	= last
		self.pay	= pay
		self.email	= first + '.' + '@gmail.com'
		
##METHOD for FULL NAME
	def fullname(self):
		return '{} {}'.format(self.fname, self.lname)

#Instance

emp_1 = Employee('rudra','singh',10000)
emp_2 = Employee('seema','singh',20000)

print(emp_2.fullname())

------
Calling or RUnning these method using class name:-

print(Employee.fullname(emp_1));

#similer to calling it using Instance
#	emp_2.fullname()
	
	
-------------Class Variable Examples------------

class Employee:
	
	def __init__(self, first, last, pay):
		self.fname	= first
		self.lname	= last
		self.pay	= pay
		self.email	= first + '.' + '@gmail.com'
		
#METHOD for FULL NAME
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
		
#Method for Raise
	def apply_raise(self):
		self.pay	= int(self.pay * 1.04)
		
#Instance

emp_1 = Employee('rudra','singh',10000)
emp_2 = Employee('seema','singh',20000)

print(emp1.pay) --> Will give present pay

emp_1.apply_raise()
print(emp.pay)	--> Will print pay with raise.

------------

class Employee:

	raise_amount	=	1.04	#class Variable
	
	def __init__(self, first, last, pay):
		self.fname	= first
		self.lname	= last
		self.pay	= pay
		self.email	= first + '.' + '@gmail.com'
		
##METHOD for FULL NAME
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
		
#Method for Raise
	def apply_raise(self):
		self.pay	= int(self.pay * Employee.raise_amount)	#We need to access class variable either using class--> Employee.raise_amount or using INSTANCE --> self.raise_amount
		

#Instance

emp_1 = Employee('rudra','singh',10000)
emp_2 = Employee('seema','singh',20000)

print(emp1.pay)

emp_1.apply_raise()		#will raise only for emp1
print(emp.pay)

NOTE:- Y we are using class vaiable using instance!! -->
print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

All will give you the value of raise  i.e. 1.04
		
If we want to access an attribute using instance, it will check whether that instance contain attribute or not ! if not then it will check in the class from where it inharits , contains attrebute or not.

So as above instance emp_1 doesn't have attrebute but emp_1 inherits class Employee which contain the attrebute.

----------
Changing raise_amount:-

Now If we want to change raise amount 

Using Class:-

Employee.raise_amount	=	1.05			#We also can do this by class method is examples given down the line

This will change raise_amount every where.

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Result:-

1.05
1.05
1.05

------

Let's change it only for instance:-

emp_1.raise_amount	=	1.05


print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

Result:-

1.04
1.05
1.04

---------------------------------------------
Regular Methods , CLASS METHODS and STATIC METHODS
---------------------------------------------


class Employee:

	raise_amount	=	1.04	#class Variable
	
	def __init__(self, first, last, pay):			#---- Regular Method
		self.fname	= first
		self.lname	= last
		self.pay	= pay
		self.email	= first + '.' + '@gmail.com'
		
##METHOD for FULL NAME 								#---- Regular Method
	def fullname(self):
		return '{} {}'.format(self.first, self.last)
		
#Method for Raise
	def apply_raise(self):							#---- Regular Method
		self.pay	= int(self.pay * Employee.raise_amount)	#We need to access class variable either using class
															#--> Employee.raise_amount or using INSTANCE --> self.raise_amount

#As below , in regular methods we use (self) but in class methods , we pass a variable i.e. (cls) in below example.
		
	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amount = amount
		

#Instance

emp_1 = Employee('rudra','singh',10000)
emp_2 = Employee('seema','singh',20000)

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)

#All will give you the value of raise  i.e. 

1.04
1.04
1.04

------

Now if we want to change it to 5 % then --> USE CLASS METHOD

Employee.set_raise_amt(1.05)

#Now All will give you the value of raise  i.e. 

1.05
1.05
1.05

NOTE :- Because set_raise_amt is a class method so it is changing all values. Works same as Employee.raise_amount	=	1.05 works.

----------------------------------------------------------------------------
Getting employee in string and after parsing getting the result using CLASS.
----------------------------------------------------------------------------


class Employee:
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

Employee.set_raise_amt(1.05)

emp_str_1 = 'John-Doe-70000'		#Getting employees as string
emp_str_2 = 'Steve-Smith-30000'		#Getting employees as string
emp_str_3 = 'Jane-Doe-90000'		#Getting employees as string

first, last, pay = emp_str_1.split('-')		#Splitting string

new_emp_1 = Employee(first, last, pay)		#Creating employee using class based on above split string.

print(new_emp_1.email)				#Printing new_emp_1
print(new_emp_1.pay)				#Printing new_emp_1


Result:-
John.Doe@email.com
70000

-----------------------------------------------------------------------------------------
In above we need to parse every time , So better to create class for that as given below.

Meaning Using Class method as alternative Constructor.
-----------------------------------------------------------------------------------------

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod								#New Method for parsing
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

   
emp_str_1 = 'John-Doe-70000'
emp_str_2 = 'Steve-Smith-30000'
emp_str_3 = 'Jane-Doe-90000'


new_emp_1 = Employee.from_string(emp_str_1)

print(new_emp_1.email)
print(new_emp_1.pay)

Result:-
John.Doe@email.com
70000

-----------------------------------------------------------------------------------
Regular Method:- Passed instances as first arguement, we call it self.

Class Method:- Automatically pass the class as cls in example, as a first arguement.

Static Method:- Don't Pass anything automatically. Don't pass instance or class.
-----------------------------------------------------------------------------------

Eg:- 
We want a function that will take in a date and return :-

------------------
STATIC METHOD For above:-
------------------

class Employee:

    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount

    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)

    @staticmethod						#STATIC METHOD
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


import datetime
my_date = datetime.date(2016, 7, 11)

print(Employee.is_workday(my_date))

Result:-
#Will return 
False 
#if saturday or sunday.

---------------------------------------------------------
Python OOP Tutorial 4: Inheritance - Creating Subclasses
---------------------------------------------------------

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
		
 class Developer(Employee):		--Subclass #Inheritance - of class Employee in subclass Developer.
	pass


dev_1 = Developer('Corey', 'Schafer', 50000)		#Using Subclass
dev_2 = Developer('Test', 'Employee', 60000)		##Using Subclass

print(dev_1.email)
print(dev_2.email)

Output:-
Corey.schafer@gmail.com
Test.Employee@gmail.com

------
NOTE:- Because Developer class is Inherit class , so first code will look into Developer class for execution but it is empty , so it will go to Employee class because Developer class inharits from Employee class and will give output accordingly.
------

print(dev_1.pay)
dev_1.apply_raise()
print(dev_1.pay)

Output:-
50000
52000

----------------------------------

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):						#class Developer inherits from Employee.
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)		#Use first, last, pay from Employee Class.
		#Employee.__init__(self,first,last,pay) --- Other Way to do. Useful while doing multiple inharits.
        self.prog_lang = prog_lang				#Additional parameter prog_lang, we need to define here.

		
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

print(dev_1.email)
print(dev_1.prog_lang)

Output:-
Corey.schafer@gmail.com
Python

-----------------------


class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_1)

mgr_1.print_emps()

--------------------------------------------------__repr__ and __str__-----------------------------------------------------



-----------------------------------------------------------------------------------------------------------------------------

