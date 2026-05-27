from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session

from database import SessionLocal

from models import CareerDepartments



router = APIRouter()



def get_db():

    db = SessionLocal()

    try:

        yield db

    finally:

        db.close()



@router.get("/career_departments")

def get_career_departments(

    db:Session = Depends(get_db)

):

    data = db.query(
        CareerDepartments
    ).all()

    return data