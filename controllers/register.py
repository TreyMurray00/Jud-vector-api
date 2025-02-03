
from models import UserData
from .embedding import get_embedding
from sqlmodel import Session

def register_user(session: Session, image: str, id: int, name: str ):
    try:
        embedding = get_embedding(image)
        if not isinstance(embedding,list):
            raise ValueError
        
        new_user = UserData(id = id, name= name , embedding=embedding)

        session.add(new_user)
        session.commit()
        session.close()
        return True
    except Exception as e:
        return e