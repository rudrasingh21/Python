*************
Exception:-
*************

Using Exception we save our program to stop / terminate in middle and execute till end , 
We handle error which occure while execution of program.

x = input("Enter Number1: ")
y = input ("Enter Number2: ")
try:
    z = int(x)/int(y)
except Exception as e:
    print('exception occurd: ',e)
    z = None
print("Division is : ",z)

Output:-
Enter Number1: 16
Enter Number2: 0
exception occurd:  division by zero
Division is :  None

*******************************************

x = input("Enter Number1: ")
y = input ("Enter Number2: ")
try:
    z = int(x)/int(y)
except ZeroDivisionError as e:
    print('Division by zero exception')
    z = None
print("Division is : ",z)

***************************
Find Out Type Of Exception:-
***************************

x = input("Enter Number1: ")
y = input ("Enter Number2: ")
try:
    z = int(x)/int(y)
except ZeroDivisionError as e:
    print('Division by zero exception')
	
except Exception as e:
	print('exception type: ',type(e).__name__)
	z = None
print("Division is : ",z)