from login import register_user, log_in

DB_PATH = 'Data/telligence_platform.db'


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



import sqlite3
import pandas as pd
conn = sqlite3.connect('DATA/telligence_platform.db')


def add_user(conn, name, hash):
    curr = conn.cursor()
    sql =(""" INSERT INTO users (username,password_hash) VALUES (?,?)""")
    param = (name,hash)
    curr.execute(sql,param)
    conn.commit()

def get_users(conn,name):
    curr = conn.cursor()
    sql = (""" SELECT * FROM users """)
    param = (name,)
    curr.execute(sql,param)
    user = curr.fetchone()
    return (user)

def migrate_user_data():
    with open('Data/users.txt','r')as f:
        users = f.readlines()
    for user in users:
        name, hash = user.strip().split(',',1)
        add_user(conn,name,hash)
    conn.close()


