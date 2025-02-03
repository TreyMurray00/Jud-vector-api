from sqlmodel import SQLModel, Field,Column
from pgvector.sqlalchemy import Vector
from typing import Optional,List

class UserData(SQLModel, table=True):
    
    model_config = {
        "arbitrary_types_allowed": True
    }

    id: Optional[int] = Field(default=None,primary_key=True)
    name: str
    embedding: Optional[List[float]] = Field(default=None,sa_column=Column(Vector(4096)))