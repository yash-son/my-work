# Taking input from the user 
print("Enter two numbers for arithmetic, comparison, and bitwise operations:") 
num1 = float(input("Enter the first number: ")) 
num2 = float(input("Enter the second number: ")) 


# Convert to integers for bitwise operations 
int1 = int(num1) 
int2 = int(num2) 


# Demonstrating Arithmetic Operators 
print("\nArithmetic Operators:") 
print(f"{num1} + {num2} = {num1 + num2}") 
print(f"{num1} - {num2} = {num1 - num2}") 
print(f"{num1} * {num2} = {num1 * num2}") 
print(f"{num1} / {num2} = {num1 / num2 if num2 != 0 else 'undefined (division by zero)'}") 
print(f"{num1} % {num2} = {num1 % num2 if num2 != 0 else 'undefined (modulus by zero)'}") 
print(f"{num1} ** {num2} = {num1 ** num2}") 
print(f"{num1} // {num2} = {num1 // num2 if num2 != 0 else 'undefined (floor division by zero)'}") 

  

# Demonstrating Comparison Operators 
print("\nComparison Operators:") 
print(f"{num1} > {num2} = {num1 > num2}") 
print(f"{num1} < {num2} = {num1 < num2}") 
print(f"{num1} == {num2} = {num1 == num2}") 
print(f"{num1} != {num2} = {num1 != num2}") 
print(f"{num1} >= {num2} = {num1 >= num2}") 
print(f"{num1} <= {num2} = {num1 <= num2}") 


# Logical Operators 
print("\nLogical Operators:") 
bool1 = bool(int(input("Enter a value (0 or 1) for logical operations (first operand): "))) 
bool2 = bool(int(input("Enter another value (0 or 1) for logical operations (second operand): "))) 
print(f"{bool1} and {bool2} = {bool1 and bool2}") 
print(f"{bool1} or {bool2} = {bool1 or bool2}") 
print(f"not {bool1} = {not bool1}") 


# Demonstrating Bitwise Operators 
print("\nBitwise Operators (using integers):") 
print(f"{int1} & {int2} = {int1 & int2}") 
print(f"{int1} | {int2} = {int1 | int2}") 
print(f"{int1} ^ {int2} = {int1 ^ int2}") 
print(f"~{int1} = {~int1}") 
print(f"{int1} << 1 = {int1 << 1}") 
print(f"{int1} >> 1 = {int1 >> 1}") 

  

# Membership Operators 
print("\nMembership Operators:") 
sample_list = [1, 2, 3, 4, 5] 
elem = int(input(f"Enter a number to check membership in {sample_list}: ")) 
print(f"{elem} in {sample_list} -> {elem in sample_list}") 
print(f"{elem}not in {sample_list} -> {elem not in sample_list}") 


# Identity Operators 
print("\nIdentity Operators:") 
x1 = [1, 2, 3] 
x2 = [1, 2, 3] 
x3 = x1 
print(f"x1 is x2 -> {x1 is x2}") 
print(f"x1 is x3 -> {x1 is x3}") 
print(f"x1 is not x2 -> {x1 is not x2}") 


# Demonstrating Operator Precedence 
print("\nOperator Precedence Demonstration:") 
expression = "10 + 3 * 2 ** 2 - 5 / 2" 
print(f"Evaluating: {expression}") 
result = eval(expression) 
print(f"Result: {result}") 