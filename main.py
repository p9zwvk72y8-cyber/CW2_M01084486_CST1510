from login import register_user, log_in
def menu():
    print('Welcome to the system')
    print('Choose from the oiptions below')
    print('1. Register')
    print('2. Log In')
    print('3. Exit')

def main():
    while True:
        menu()
        choice = input('>')
        if choice == '1':
            register_user()
        elif choice == '2':
            if log_in():
                print("Login successful!")
            else:
                print("Login failed. Invalid username or password.")
           
        elif choice == '3':
            print("Exiting the system.")
            break
        else:
            print("Invalid choice. Please try again.")

main()