from fastapi import APIRouter,Depends

from sqlalchemy.orm import Session

from database import SessionLocal

from models import UserProgress

from schemas import UserProgressResponse


router=APIRouter()


def get_db():

    db=SessionLocal()

    try:

        yield db

    finally:

        db.close()



@router.get(

"/user_progress",

response_model=list[UserProgressResponse]

)

def get_user_progress(

db:Session=Depends(get_db)

):


    progress=db.query(

        UserProgress

    ).all()


    return progress