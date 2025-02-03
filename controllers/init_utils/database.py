from sqlmodel import Session, create_engine, SQLModel
import os

host=os.getenv("HOST")
user=os.getenv("POSTGRES_USER")
database=os.getenv("POSTGRES_DB")
password=os.getenv("POSTGRES_PASSWORD")
port=os.getenv("DB_PORT")

# database_connection_string= f"postgresql://{user}:{password}@{host}:{port}/{database}"
database_connection_string = "postgresql://admin:password@localhost:5432/vectordb"

engine = create_engine(database_connection_string)


SQLModel.metadata.drop_all(engine)
SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()
