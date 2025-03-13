from sqlmodel import Session, select, literal
from models.user import UserData
from .embedding import get_embedding

def search(session: Session, image: str, threshold: float = 0.5):
    try:
        embedding = get_embedding(image)
        if not isinstance(embedding, list):
            raise ValueError("Embedding must be a list")
        
        cosine_similarity = literal(1) - UserData.embedding.op("<=>")(embedding)

        stmt = select(UserData.id, UserData.name, cosine_similarity.label("cosine_similarity")).where(cosine_similarity >= threshold).order_by(cosine_similarity.desc()).limit(1)
        result = session.exec(stmt).all()
        for id, name, cosine_similarity in result:
            return {"id": id, "name": name, "cosine_similarity": cosine_similarity}
        # stmt = select(UserData.id, UserData.name).order_by(UserData.embedding.op("<=>")(embedding)).limit(1) 
        # result = session.exec(stmt).all()
        # for id, name in result:
        #     return {"id": id, "name": name}

        # return dict(result)
    except Exception as e:
        # Optionally log the error
        return e
