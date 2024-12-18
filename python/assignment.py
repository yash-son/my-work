numbers = []

while True:
    user_input = input("Enter an integer (or 'done' to finish): ")
    
    if user_input.lower() == "done":  # Case-insensitive check for "done"
        break
    
    try:
        number = int(user_input)  # Try to convert input to an integer
        numbers.append(number)  # Add the valid integer to the list
    except ValueError:
        print("Invalid input. Please enter an integer.")
        
if numbers:  # If the list is not empty
    print(f"Maximum: {max(numbers)}")
    print(f"Minimum: {min(numbers)}")
else:
    print("No numbers were entered.")