#As we have learned earlier that we canot combine string and numbers like this 
a=45
b="This is a number "
c=a+b #this is not valid as we acn't combine number and a strng using a + operation

#But we can combine using f string or format() method 
#To specify a string as an f-string, simply put an f in front of the 
# string literal, and add curly brackets {} as placeholders for variables and other operations.
age=20
print(f"i am {age}years old.")

#palceholders are defined by curly braces {}
#inside placeholders we can place variables,operations,functions or modifiers to modify a ducument
#Modifiers are palced after colon like .2f
price=59
print(f"The price is {price:.2f}")

#f strings
x=f"My age is {2*10}"
print(x)

#Python escape characters 
#It is used to characters in string that are illegal to it
#It is done by inserting a \ follwed by illegal character to be inserted

# doble quotes as a excape character
print("My name is \"Yash Soni\".")
#Double quote inside a double quote which should generally gve us error but using the escape character we are bypassing it

#Single quote escape character
print('My name is\'Yash Soni\'.')

#new line escape character
print("My name is Yash Soni.\nI am 20 years old.")

#escape character for backspace \
#We know we generally use a \ for escape character so can't just use it normally in a string 
#to d that we use \\
print("This will insert \\(blackslash).")

#Carriage return
print("Hello\rWorld")#\r works same as \n in macos

#To give a tab space
print("Hello\tWorld")

#backspace escape character it is used to clear a space
print("Hello, \bWorld!")

#\x20 escape keyword for creating more space
print("Hello\x20world!")

#We can write a string in parallel with their corresponding ascii value in octal or hexadecimal form
#Suppose we want to create a variable storing a "Hello" string
x="\110\145\154\154\157" #We can do this in this way too
print(x)

#Doing same using corresponding hexidecimal values
#This is done by \x followed by coressponding hexadecimal value ascii
x="\x48\x65\x6c\x6c\x6f"
print(x)

#Find method
#It is used to find wether the substring is present or not in a string
#If present it returns the starting index of the sub-string and if not it returns -1
#Exaple
a="hello,world"
print(a.find("hello"))

#format method
#It is used to insert the varibles through palcehlders
name="Yash Soni"
age=21
print("My name is {} and i am {} years old.".format(name,age))

#join() method
#It is used to join a differnt values from a list through some seperator like " " or ","
a=['Yash','Soni']
print(" ".join(a))

#count() method
#Used to count a umber of occurences of a given sub-string in a string
#Example
a='banana'
print(a.count('a'))

#startswith() and endswith() method
#if a string starts or end with certain subtring it returns true or false respectively
a="assignment01.pdf"
if a.endswith(".pdf"):
    print("The file is of pdf type.")

#capatalize() method
#It is used to capatalize a first letter of a string
a='yash soni'
print(a.capitalize())

#title() method
#It is used to capatalize a first letter of a every word in a string 
a="yash soni"
print(a.title())

