import psycopg2
import pandas as pd

def query_to_df(query= "SELECT * FROM power_weather LIMIT 15"):
    try:
        conn = psycopg2.connect(user = "postgres",
                                password = '130303',
                                host = 'localhost',
                                port='5432',
                                database = 'postgres')
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

def execute_query(query):
    try:
        conn = psycopg2.connect(user = "postgres",
                                password = '130303',
                                host = 'localhost',
                                port='5432',
                                database = 'postgres')
        cursor = conn.cursor()
        
        cursor.execute(query)
        print("Query Executed")
        
    except (Exception, psycopg2.Error) as error :
        print ("Error while connecting to PostgreSQL:", error)

    if(conn):
        conn.commit()
        cursor.close()
        conn.close()