#Boolean represent one of two values true or false
print(10<9)

#If the statement returns if condition will work or if would be wrong if condition will not work
a=50
b=4
if b>a:
    print("b is greater than a ")
else:
    print("a is lesser than b")

#Evaluation of variables using a bool function
a="hello"
print(bool(a))

b=0
print(bool(b))

#Anynumber is true except 0
#Any string is true except empty string
#Any list,tuple,set and dictionary is true except empty one
print(bool(''))
print(bool([]))
print(bool(()))
print(bool({}))

#One more value, or object in this case, evaluates to False, and that is if you have an object that is made from a class with a __len__ function that returns 0 or False:
class myclass():
    def __len__(self): #The two underscoeres are important
        return 0

myobj=myclass()
print(bool(myobj))

# __len__ is a python method is a python method to define a length of an object if it returns zero the object
#is considered falsy

#Functions can return boolean value too
def myfnv():
    return True
print(myfnv())
if myfnv():
    print("Yes")
else:
    print("No")

#Python has many built_in-functions that return bool values 
#one such bult-in-function is isinstance()90
x=90
print(isinstance(x,int))

