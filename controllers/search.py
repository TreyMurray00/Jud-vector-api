from sqlmodel import Session, select
from .embedding import get_embedding
from models.user import UserData

async def search(session: Session, image: str):
    try:
        embedding = get_embedding(image)
        if not isinstance(embedding,list):
            raise ValueError
        # session.scalars()
        statement = select(UserData).where(UserData.id == 0)
        
        data = await session.exec(statement).all()
        session.close()
        # data = await session.exec(
        #     select(UserData).order_by(UserData.embedding.op("<->")(embedding))
        # ).all()
        return data
        
    except Exception as e:
        return e