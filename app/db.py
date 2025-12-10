#3dp.
#conn = sqlite3.connect('DATA/telligence_platform.db')
import sqlite3

def get_connection():
    conn= sqlite3.connect('DATA/telligence_platform.db',check_same_thread=False)

    return conn
