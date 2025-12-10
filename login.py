import bcrypt

def hash_password(password):
    binary_password = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(binary_password, salt)
    return(hashed.decode('utf-8'))

def validate_password(password, hash):
    psw = password.encode('utf-8')
    hash_ =hash.encode('utf-8')
    return bcrypt.checkpw(psw, hash_)

def register_user():
    user_name = input("Enter user name: ")
    user_password = input("Enter password: ")
    hash = hash_password(user_password)
    # store users in the repository Data folder
    with open('Data/user.txt', 'a') as f:
        f.write(f'{user_name},{hash}\n')
    print("User registered successfully.")

def log_in():
    user_name = input("Enter user name: ")
    user_password = input("Enter password: ")
    path = 'Data/user.txt'
    with open(path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            name, hash = line.split(',', 1)
            if name == user_name:
                return validate_password(user_password, hash)
    # If we get here no matching user found
    return False