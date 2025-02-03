import os
import psycopg2
from dotenv import load_dotenv, set_key

def create_extension():
    # "postgresql://admin:password@localhost:5432/vectordb"
    
    conn = None
    cur = None
    try:

        load_dotenv()
        # Establish the connection: VALUES LOADED FROM .ENV FILE
        conn = psycopg2.connect(
            host="localhost",
            user="admin",
            database="vectordb",
            password="password",
            port=5432
        )
        cur = conn.cursor()
        
        # Execute the SQL command to create the extension
        cur.execute('CREATE EXTENSION IF NOT EXISTS vector;')
        
        # Commit the transaction
        conn.commit()
        print("Setup completed")
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # Ensure the cursor and connection are closed properly
        if cur:
            cur.close()
        if conn:
            conn.close()

# Call the function to create the extension
create_extension()

print("HOST:", os.getenv("HOST"))
print("PORT:", os.getenv("DB_PORT"))
print("POSTGRES_USER:", os.getenv("POSTGRES_USER"))
print("POSTGRES_PASSWORD:", os.getenv("POSTGRES_PASSWORD"))
print("POSTGRES_DB:", os.getenv("POSTGRES_DB"))



