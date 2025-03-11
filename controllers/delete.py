from models import UserData
from sqlmodel import Session, select

def delete_user(session: Session, id: int):
    try:
        stmt = select(UserData).where(UserData.id == id)
        result = session.exec(stmt)
        record = result.one()
   
        session.delete(record)
        session.commit()
        return True

    except Exception as e:
        return False
