from sqlmodel import select
from .embedding import get_embedding
from models.user import UserData
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Union
def search(session: AsyncSession, image: str) -> Union[List, Exception]:
    try:
        embedding = get_embedding(image)
        if not isinstance(embedding, list):
            raise ValueError("Embedding must be a list")
        
        stmt = select(UserData.id, UserData.name).order_by(UserData.embedding.op("<->")(embedding)).limit(1)
        result = session.exec(stmt)
        data = result.all()
        
        return dict(data)
        
    except Exception as e:
        # Optionally log the error instead of returning the exception
        return e
