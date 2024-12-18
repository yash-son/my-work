#function defination in python begins with def keyword
x=5
y=6
def myfunc(x,y):
    x=6
    y=8
myfunc(x,y)
print(x,y)
#in python when we are passing a argument we are actually assigning value of that argument to a parameter in 
#python local scope

#but in case of argument is of mutable type(list or dictionary) then changes to that object inside a 
#function will also affect the object outside the function.

#example to clarify this 

def change_number(x):
    x=10
x=5
change_number(5)
print(x) #this will not change the value of variable because argument here is not passed by refrence
#meaning changes to correspondng parameter inside the function will not affect the original passed object

def change_list(list):
    list.append(5)
a=["yash",1]
change_list(a)
print(a)
#while here changes to a corresponding parameter is affecting the actual passes object

#function always returns the return keyword
#In without a "return" returns the None keyword which is equivalent to the NUll keyword in other languages
#None is also logical equivalent to false
a=bool(None)
print(a)

#There is no conecpt of function overloading in python
#No two functions can have same name even if they have set of arguments

#We can provide the default value to the arguments ina python
#These arguments are ptional

def myfunc(x,y=3,z="hello"):
    return x+y
x=myfunc(5,3)
y=myfunc(5)
z=myfunc(5,3,'hello')
k=myfunc(y=3,x=5,z="hello")
print(x,y,z,k)
#All these three will work in the same way

#function can be used as a argument for another function
def square(x):
    return x*x
def applier(q,value):
    return q(value)
x=applier(square,4)
print(x)

