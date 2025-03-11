from models import UserData
from sqlmodel import Session, select

async def delete_user(session: Session, id: int):
    try:
        stmt = select(UserData).where(UserData.id == id)
        result = session.exec(stmt).first()
        if result:
            session.delete(result)
            session.commit()
            return True
        else:
            return False
    except Exception as e:
        return False
