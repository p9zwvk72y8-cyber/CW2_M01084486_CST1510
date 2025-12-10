import pandas as pd
import sqlite3



def migrate_datasets_metedata(conn,DATA_DIR):
    path = DATA_DIR /'datasets_metadata.csv'
    df =pd.read_csv(path)
    print(df.head())
    df.to_sql('datasets_metadata',conn,if_exists='append',index=False)
    print('Data loaded successfully'   )

def migrate_it_tickets(conn):
    path =' /Users/jameslee/Desktop/CW2_M01084486_cst1510/DATA/it_tickets.csv'
    df =pd.read_csv(path)
    print(df.head())
    df.to_sql('it_tickets',conn,if_exists='append',index=False)
    print('Data loaded successfully'   )