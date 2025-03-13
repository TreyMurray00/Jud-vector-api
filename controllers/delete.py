from models import UserData
from sqlmodel import Session, select

def delete_user(session: Session, id: int):
    try:
        stmt = select(UserData).where(UserData.id == id)
        result = session.exec(stmt).one()
        session.delete(result)
        session.commit()
    except Exception as e:
        return False
