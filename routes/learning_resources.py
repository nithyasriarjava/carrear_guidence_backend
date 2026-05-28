from fastapi import APIRouter, Depends

from sqlalchemy.orm import Session

from database import SessionLocal

from models import LearningResources

router = APIRouter()



def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()



@router.get("/learning_resources")

def get_learning_resources(

    db: Session = Depends(get_db)

):

    return db.query(
        LearningResources
    ).all()