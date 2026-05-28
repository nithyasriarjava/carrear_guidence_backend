from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import SessionLocal

from models import UserProgress



router = APIRouter()



def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()



@router.get("/user_progress")

def get_user_progress(

    db: Session = Depends(get_db)

):

    data = db.query(
        UserProgress
    ).all()

    return data