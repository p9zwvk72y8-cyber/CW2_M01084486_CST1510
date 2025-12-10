import pandas as pd
import sqlite3



def migrate_cyber_incidents(conn,):
    path='/Users/jameslee/Desktop/CW2_M01084486_cst1510/DATA/cyber_incidents.csv'
    df =pd.read_csv(path)
    print(df.head())
    df.to_sql('cyber_incidents',conn,if_exists='append',index=False)
    print('Data loaded successfully')

def get_all_cyber_incidents(conn):
    sql='Select * from cyber_incidents'
    data=pd.read_sql(sql,conn)
    return data
conn = sqlite3.connect('DATA/cyber_incidents.csv')