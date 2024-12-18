# print("Hello, world!")

if 5>2:
    print("5 is greater than 2")
    print("5 is greater than 2")

# if 5>2:
#  print("5 is greater than 2")

x=6 #this is a nteger type variable
y="Hello, World" #this is a string
print(x,y)
#This is a example regarding how to declare variables in python proramming
#Python comment renders the whole line as a comment   

print("hello, world")   
print("Cheers, mate")
#This is 
#a comment
#written in multiple lines

'''This is
a comment
written in multile lines'''

x=5 #x here storing integer data type value
x=int(5.4) #x here storig float data type value
#variables are not of particular data type in python 
#They just store the values of different data types
print(x)

#If we want to change the data type of the variable than that can be done using the type casting
#Example
x=int(3) #x here is 3
y=str(3) #x here is of string data type as '3'
z=float(3) #x here is 3.0
#we can get the data type of the variable using the type() function
print(type(x))
print(type(y))
print(type(z))

x='''"Y'a'sh"'''
print(X)

#Multiple values to mutliple variables in a single line
x,y,z="orange","Apple","Banana"
print(x,y,z)

#One value to multiple variables
x=y=z="Apple"
print(x,y,z)

#Unpacking of values from a list or a tuple
fruits=['apple','banana','pineapple']
x,y,z=fruits #this is called uppacking of list 
print(x,y,z)

x="Python"
y="is"
z="awesome"
print(x,y,z)
print(x+y+z)

x="Python "
y="is "
z="awesome."
print(x+y+z) #This operation on string is called by concatenate

# + opeartion on numbers works as a normal addition opearation
x=9
y=5
print(x+y)

#We can't perform a + opeation on variables of with numerical value and string
x=6
y="string"
# print(x+y)
#The best way to output the variables of different data types is by seperating them by a comma
print(x,y)

#Gloal variables are the variables that can be used by everyone both inside and outside of the function

x="awesome"
# def myfunc():
#     print(f"Python is {x}.")#Here we are accessing the global variable inside a function
# myfunc()
def myfunc():
    x="great"
    print(f"Python is {x}.")
myfunc()
print(f"Python is {x}.")

#using a global keyword we can create a global variable inside a function
x="awesome"
def myfunc():
    global x
    x="great."
myfunc()
print(f"Python is {x}")

#We can get the data type of any variable using the type() function
x=90
print(type(x))
y=1+5j
print(type(y))


x=[1,2,3] #This is a list
x=(1,2,3) #This is a tuple
x=range(2,6) #This is a range data type
# for i in x:
#     print(i,end=" ")
# # or 
print(list(x))
print(type(x)) 

x={"name":"yash","age":21} #This is a dictionary
print(type(x))

x={'yash','shrajal','saksham'} #this is a set
print(type(x))
x=frozenset({'yash','shrajal','saksham'}) #This is a frozenset
print(type(x))

x=False #This is a bool data type #First letter must be capital
print(type(x))

x=b"Hello"#This is bytes data type value
print(type(x))

x=bytearray(5) #this is a bytearray data type value
print(type(x))
print(x)

x=memoryview(bytes(5)) #This is a memoryview datatypes value
print(x)
print(type(x))

x= None #This is NoneType
print(x)
print(type(x))

#We can specify the datatype of the values using the type casting
#In a bool function all non-zero values are true and zero is false

x=bool(5)
print(x)

x=list(("apple","pineapple","banana"))
print(x)
x=set(("apple","pineapple","banana"))
print(x)
x=frozenset(("apple","pineapple","banana"))
print(x)

#int to bytes datatype
x=bytes(5)
print(x)

x=bytearray(5)
print(x)

x=67
y=memoryview(bytes(x))
print(y)

#variables into dictionary
x=dict(name="yash",age=34)
print(x)

x=3
y=2.8
z=2+4j
print(type(x),type(y),type(z))


#different way of representing a floating number
x=-45e-100
print(x)

#We cannot convert complex numbers into another data type
x=34
y=67.0
z=5j

print(float(x))
print(int(y))
print(complex(y))
print(int(z))

#random module in python
import random
print(random.randrange(3,4)) 


#typecast into int data type
x=int(4)
y=int(3.0)
z=int('3')
print(x,y,z)

#typecast in float data type
x=float(3)
y=float(3.8)
z=float('3')
print(x,y,z)


#typecast into string data type
x=str(3)
y=str(4.5)
z=str(b'hello')
print(x,y,z)
print(type(z))

#string
print("Hello, World")
#We can use quotes inside quotes untill they don't match the quotes surronding it
print("My name is 'yash soni'.")
# print('My name is 'yash soni'') #This will give us an error
print('''Here is "yash" and 'shrajal'.''')

#Multi-line string
#multi-line comment is done using three quotes
x='''My 
name is
Yash Soni.
'''
print(x)
#That why we use three quotes for multiline commments too.
#It can be either three singgle or double quotes.

x="hello"
print(x[0])

#Looping through a string
for x in "hello":
    print(x,end=' ')

#end keyword in python
#using the len function we can get the lenght of the string 
x="Hello, World"
print(len(x))

#To check the presense of certain letter or phrase in string we use a in keyword 
x="The best thing in life is freedom!"
print("freedom" in x)


#we can combine a in keyword with if conditioning 
_name="Yash Soni"
if ('Yash' in _name ):
    print("Your firstname is yash.")

#String length
a="Hello, world"
print(len(a))

#USing the len function we can find the length of the string
#To check wether something is present in something or not we use in keyword
s="The best thing in life is freedom!"
# print("freedom" in s)
#We can use the in keyword for conditioning in if else statement
if ("best" in s):
    print("The best thing in life is freedom.")

#To check weither the certain phrase is present string or not we use a ot in keyword
a="The best thing in life is freedom."
# print("expensive" not in a)
# We can use a not in keyword with if coditioning too
if ("expensive" not in a):
    print('"expensive" is not present in a string a')

#We python we can return a slice of a string 
a="Yash Soni"
print(f"The first name of your name is {a[0:4]}.")

#By leaving a first index of a string slicing the slicing by default starts from a 0th position
a="Yash Soni"
print(f"The name is {a[:4]}.")

#By leaving the end index the range will go to the end of the string
s="Yash Soni"
print(f"The last of your name is {s[5:]}.")

#Use the neagtive indices to slice from the end of the string 
#In a negative slicing lower bound more negative value is not included
a="Yash Soni"
print(f"The first name of your name is {a[-7:-5]}.")
print(f"The last name of your name is .{a[-4:]}.")

#To slice from the start of the string 
a="Programming"
print(a[:6])

#To slice to the end of the string
a="Programming"
print(a[6:])

#Python built in methods
#Python upper() method
#It returns the strng in a upper case
a="yash soni"
print(a.upper())

#Python lower() method
#It returns the string in a lower case
a="YASH SONI"
print(a.lower())

#This doesn't works in python
a='yash'
a=a.upper()
print(a)

#strip() method
#It is used to remove a whitespace from beggining or ending of  a string
a=" Hello, World "
a=a.strip()
print(f".{a}.")

#split() method
#This method is used to return a splited subdtrings based on sspecified seperators and also returns substrings as a items of a 
#lst
a="Hello,World"
print(a.split(","))

#replace() method
#It is used to replace a ceratin part of a string with another sring of same length
a="Yash"
print(a.replace("as","a "))

#python strng concatenation
#To combine two or more strings we use + peration and we call it string concatenation
a="Yash"
b="Soni"
c=a+b
print(c)
#As we can see there is no space between Yash and Soni
#To do that we can 
d=a+" "+b
print(d)#Now this is working perfectly 