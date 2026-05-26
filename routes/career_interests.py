from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session

from database import SessionLocal

from models import CareerInterest

from schemas import CareerInterestResponse


router=APIRouter()


def get_db():

    db=SessionLocal()

    try:

        yield db

    finally:

        db.close()



@router.get(

"/career-interests",

response_model=list[CareerInterestResponse]

)

def get_career_interests(

db:Session=Depends(get_db)

):


    interests=db.query(

        CareerInterest

    ).all()


    return interests