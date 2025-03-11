import os
import psycopg2
from dotenv import load_dotenv

def create_extension():
    
    conn = None
    cur = None
    try:
        print("Loading environment variables")
        load_dotenv()
        print("Loading environment variables")

        host=os.getenv("HOST")
        user=os.getenv("POSTGRES_USER")
        database=os.getenv("POSTGRES_DB")
        password=os.getenv("POSTGRES_PASSWORD")
        port=os.getenv("DB_PORT")
        print("Creating Postgres vector plugin if it does not exist")
        conn = psycopg2.connect(
            host=host,
            user=user,
            database=database,
            password=password,
            port=port
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



