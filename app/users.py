import bcrypt



def is_valid_hash(psw, hash):
    """Check if a password matches a bcrypt hash."""
    hash_ = hash.encode('utf-8')
    byte_psw = psw.encode('utf-8')
    is_valid = bcrypt.checkpw(byte_psw, hash_)
    return is_valid


def hash_password(password: str) -> str:
    """Hash a password for storing."""
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed.decode('utf-8')


def verify_password(stored_password: str, provided_password: str) -> bool:
    """Verify a stored password against one provided by user."""
    return bcrypt.checkpw(provided_password.encode('utf-8'), stored_password.encode('utf-8'))


def set_user(conn, name, hash):
    """Insert a new user into the database."""
    curr = conn.cursor()
    sql = "INSERT INTO users (username, password_hash) VALUES (?, ?)"
    param = (name, hash)
    curr.execute(sql, param)
    conn.commit()


def get_all_users(conn):
    """Retrieve all users from the database."""
    curr = conn.cursor()
    sql = "SELECT * FROM users"
    curr.execute(sql)
    all_users = curr.fetchall()
    for i in all_users:
        print(i)


def get_user(conn, name_):
    """Retrieve a single user by username."""
    curr = conn.cursor()
    sql = "SELECT * FROM users WHERE username = ?"
    param = (name_,)
    curr.execute(sql, param)
    user = curr.fetchone()
    return user


def update_user_password(conn, user_name, new_password):
    """Update a user's password."""
    curr = conn.cursor()
    sql = "UPDATE users SET password_hash = ? WHERE username = ?"
    params = (new_password, user_name)
    curr.execute(sql, params)
    conn.commit()


def delete_user(conn, user_name):
    """Delete a user from the database."""
    curr = conn.cursor()
    sql = "DELETE FROM users WHERE username = ?"
    params = (user_name,)
    curr.execute(sql, params)
    conn.commit()
    print(f"User {user_name} deleted successfully.")


def migrate_user(conn):
    """Migrate users from legacy file to database."""
    with open('Data/user.txt', 'r') as f:
        lines = f.readlines()
    for line in lines:
        name, hash = line.strip().split(',', 1)
        set_user(conn, name, hash)


def user_registration(conn):
    """Register a new user interactively."""
    user_name = input("Enter user name: ")
    user_password = input("Enter password: ")
    hash = hash_password(user_password)
    set_user(conn, user_name, hash)
    print("User registered successfully.")


def user_login(conn, name, password):
    """Verify user login credentials."""
    user = get_user(conn, name)
    if user is None:
        return False
    user_id, name_db, hash_db = user
    if name == name_db:
        return verify_password(hash_db, password)
    return False
