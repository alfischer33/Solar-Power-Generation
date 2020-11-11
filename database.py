import psycopg2
import pandas as pd
from config import config

# returns a given SQL SELECT query to a pandas DataFrame object
def query_to_df(query= "SELECT * FROM power_weather LIMIT 15"):
    
    params=config()

    try:
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        
        cursor.execute(query)
        df = pd.DataFrame(cursor.fetchall())
        df.columns = [i[0] for i in cursor.description]
        df.set_index('id', drop=True, inplace=True)

    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL:", error)

    if(conn):
        cursor.close()
        conn.close()
    return df

#executes a given SQL query in the postgresql database
def execute_query(query):
    
    params=config()

    try:
        conn = psycopg2.connect(**params)
        cursor = conn.cursor()
        
        cursor.execute(query)
        print("Query Executed")
        
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL:", error)

    if(conn):
        conn.commit()
        cursor.close()
        conn.close()