from models import UserData
from sqlmodel import Session, select
from .embedding import get_embedding

def update_user(session: Session, id: int, name: str = "", image: str = ""):
    try:
        #generate embeddings from image and update the record
        embedding = None
        if image != "":
            embedding = get_embedding(image)
            if embedding is None:
                raise ValueError("No face detected")
        
        stmt = select(UserData).where(UserData.id == id)
        result = session.exec(stmt)
        record = result.one()
        if name != "":
            record.name = name
        if embedding is not None:
            record.embedding = embedding
    
        session.add(record)
        session.commit()
        return True
    
    except Exception as e:
        return False
