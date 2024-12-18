# Login Module
class LoginModule:
    def __init__(self):
        # Dictionary to store usernames and passwords
        self.user_data = {}

    def register_user(self, username, password):
        """Register a new user."""
        if username in self.user_data:
            print("Username already exists. Please choose a different username.")
        else:
            self.user_data[username] = password
            print(f"User '{username}' registered successfully!")

    def login_user(self, username, password):
        """Verify username and password."""
        if username in self.user_data and self.user_data[username] == password:
            print(f"Welcome, {username}! Login successful.")
        else:
            print("Invalid username or password. Please try again.")

    def change_password(self, username, old_password, new_password):
        """Change the password of an existing user."""
        if username in self.user_data and self.user_data[username] == old_password:
            self.user_data[username] = new_password
            print(f"Password for user '{username}' changed successfully!")
        else:
            print("Invalid username or old password. Cannot change password.")

    def display_users(self):
        """Debugging function to display all registered users (For Admins)."""
        print("Registered Users:", list(self.user_data.keys()))

# Example Usage
login_module=LoginModule()
while True:
    print("\n1. Register User\n2. Login\n3. Change Password\n4. Display Users\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        username = input("Enter username: ")
        password = input("Enter password: ")
        login_module.register_user(username, password)

    elif choice == "2":
        username = input("Enter username: ")
        password = input("Enter password: ")
        login_module.login_user(username, password)

    elif choice == "3":
        username = input("Enter username: ")
        old_password = input("Enter old password: ")
        new_password = input("Enter new password: ")
        login_module.change_password(username, old_password, new_password)

    elif choice == "4":
        login_module.display_users()

    elif choice == "5":
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.") 