
#Write something in a file
#test.txt does not exist
f = open("D:\\Study\\Hadoop\\Python\\PyCharm\\test.txt","w")
f.write("I Love Python")
f.close()

#Append a file
f = open("D:\\Study\\Hadoop\\Python\\PyCharm\\test.txt","a")
f.write("\nI Love C++")
f.close()

#Reading file line by line
f = open("D:\\Study\\Hadoop\\Python\\PyCharm\\funny.txt","r")
print(f.read())
f.close()

#OutPut
I Love Python
I Love C++
I Love Java too

#Reading file
f = open("D:\\Study\\Hadoop\\Python\\PyCharm\\funny.txt","r")
for line in f:
    tokens=line.split(' ')
    print(str(tokens))
f.close()

#OutPut
['I', 'Love', 'Python\n']
['I', 'Love', 'C++\n']
['I', 'Love', 'Java', 'too']


#Reading file and get count of line by storing it in another file

f = open("D:\\Study\\Hadoop\\Python\\PyCharm\\funny.txt","r")
f_out = open("D:\\Study\\Hadoop\\Python\\PyCharm\\funny_WC.txt","w")
for line in f:
    tokens=line.split(' ')
    f_out.write("Word Count is "+str(len(tokens))+" for "+line)
f.close()
f_out.close()

#OutPut:-
Word Count is 3 for I Love Python
Word Count is 3 for I Love C++
Word Count is 4 for I Love Java too

r+ :- Read and write mode
w+ :- Read and write mode as well create if file if not exist:

WITH Statement:-
                Using WITH statement you don't need to close() it explectily:

with open("D:\\Study\\Hadoop\\Python\\PyCharm\\funny.txt","r") as f:
    print(f.read())