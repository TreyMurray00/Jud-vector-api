from sqlmodel import Session, create_engine, SQLModel , inspect
import os

host=os.getenv("HOST")
user=os.getenv("POSTGRES_USER")
database=os.getenv("POSTGRES_DB")
password=os.getenv("POSTGRES_PASSWORD")
port=os.getenv("DB_PORT")

database_connection_string= f"postgresql://{user}:{password}@{host}:{port}/{database}"

engine = create_engine(database_connection_string)

# Inspect the database and create the table if it does not exist
inspector = inspect(engine)
print(f"Inspecting database: {database_connection_string}")
if not inspector.has_table("userdata"):
    print("Table not found, creating table 'userdata'")
    SQLModel.metadata.create_all(engine)
    print("Table created")
else:
    print("Table 'userdata' found")
# SQLModel.metadata.drop_all(engine)
# 

def get_session():
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()
