from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session

from database import SessionLocal
from models import Career
from schemas import CareerResponse


router=APIRouter()


def get_db():

    db=SessionLocal()

    try:

        yield db

    finally:

        db.close()



@router.get(

"/careers",

response_model=list[CareerResponse]

)

def get_careers(

db:Session=Depends(get_db)

):


    careers=db.query(

        Career

    ).all()


    return careers