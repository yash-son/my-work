if x<10
  print("x is less than 10") #this is a syntax error

x*y=z#this is a semantic error

#run time error
x=10/0
print(x)

#logical error
def calculate_area(r):
  area=2*3.14*r #this is wrong because area=2pir^2
  return area
print(calculate_area(4))

#type error
x=5
y='yash' 
print(x+y) #this will generate type error

#NameError
#When a variable or function is not founded in a current scope
print(k)

#Index Error
#When index is out of range for list,tupleor other sequence
list={1,2,3,4,5,6}
print(list[6])

#KeyError
#When key is not founded in a dictionary
d={'name':'yash','age':45}
print(d[id])

#ValueError
#When a invalid argument is performed such as trying to convert into integer data type
#where string is not conataining a number
a=int("yash")
print(a)

#AttributeError
#When a attribute or method is not founded for an object
l=[1,2,3,4]
print(l.lower())

#ZeroDivisionError
#Error that is caused by division of number by zero
a=10/0
print(a)

#exception
# Even if a statement or expression is syntactically correct, it may
# cause an error when an attempt is made to execute it. Errors
# detected during execution are called exceptions


#Exception handling

# If an exception occurs during execution of the try clause, the
#rest of the clause is skipped.
#Then if its type matches the exception named after the except
#keyword, the except clause is executed, and then execution
#continues after the try statement.

#example1
try:
  a=int(input("enter a number:"))
except ValueError:
  print("Not a correct number! Please enter again.")


try:
  a=10/0
except ZeroDivisionError:
  print("There is a zero as divisor")
  

#Running Multiple Error
try:
  a=int(input("enter the number"))
  b=10/a
except ValueError:
  print('Ivalid input please enter again')
except ZeroDivisionError:
  print("There is a zero division error here")

