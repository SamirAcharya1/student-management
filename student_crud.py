import psycopg2
DB_NAME = "postgres"
DB_USER = "postgres.umkvljxuhwauyghgsshh"
DB_PASSWORD = "h1dHawHCXQiIC3KI"
DB_HOST = "aws-0-ap-southeast-1.pooler.supabase.com"
DB_PORT = "5432"


def db_connection():
    try:
        conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT)
        return conn
    except Exception as e:
        print("Error connecting to the database: ", e)
        return None

def insert_tables(name, age):
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO teacher (name, age) VALUES(%s, %s) RETURNING id", (name, age))
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    insert_tables("Sayujya", 99)

